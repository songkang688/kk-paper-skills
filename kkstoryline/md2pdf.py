#!/usr/bin/env python3
"""
md -> PDF for kkstoryline / yfnskills deliverables. Portable: no machine-specific paths.

Goal: a *designed* deliverable, not a raw markdown dump. The converter understands
a small set of presentation components so an agent can assemble a professional PDF
(cover, callouts, flow diagrams, styled tables, sentence cards) from plain markdown,
and it renders CJK + English from system fonts so nothing turns into tofu boxes.

Pipeline is always two stages:
    1. markdown -> HTML   (python-markdown, or markdown-it-py as a fallback)
    2. HTML -> PDF        (first renderer found, see RENDERERS below)

Presentation features (all optional, all degrade gracefully):
    * Frontmatter (--- ... ---) at the top becomes a cover page with a diagonal
      two-colour split. Keys: title, subtitle, header (running header + kicker),
      stamp, and any number of meta_<label> lines shown as footer lines.
    * Palette is NOT fixed. Override per document with `primary:` and `accent:`
      (any hex) in the frontmatter; defaults are a professional navy + terracotta.
    * "::: note <title>" ... ":::"  -> highlighted callout box.
    * "::: flow" ... ":::"          -> horizontal step/flow diagram; one step per
      line as "title | subtitle", steps joined by arrows.
    * "::: card <title>" ... ":::"  -> rounded sentence card; put one bold-labelled
      line per field (改前/改后/改前翻译/改后翻译/为什么改).
    * Tables get a coloured header row and zebra striping automatically.

Renderer resolution order (first hit wins):
    MD2PDF_ENGINE env var  ->  PATH lookup  ->  per-OS install locations
Supported renderers: any Chromium-family browser, wkhtmltopdf, weasyprint.

Usage:
    python md2pdf.py <file.md | directory> [--serif] [--keep-html]
    python md2pdf.py --check          # report what this machine can use

Writes <name>.pdf next to <name>.md. Exit code 0 only if every file converted.
"""
from __future__ import annotations

import argparse
import html as _html
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

# --------------------------------------------------------------------------
# palette (defaults; override per document via frontmatter primary:/accent:)
# --------------------------------------------------------------------------
PRIMARY_DEFAULT = "#22384f"   # deep navy
ACCENT_DEFAULT = "#c0472f"    # terracotta / orange


def _norm_hex(value: str, fallback: str) -> str:
    v = (value or "").strip()
    if re.fullmatch(r"#?[0-9a-fA-F]{3}", v):
        v = v.lstrip("#")
        v = "".join(c * 2 for c in v)
        return "#" + v
    if re.fullmatch(r"#?[0-9a-fA-F]{6}", v):
        return "#" + v.lstrip("#")
    return fallback


def _rgb(hexs: str) -> tuple[int, int, int]:
    h = hexs.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def _rgba(hexs: str, alpha: float) -> str:
    r, g, b = _rgb(hexs)
    return f"rgba({r},{g},{b},{alpha})"


def _mix_white(hexs: str, ratio: float) -> str:
    """Lighten a colour toward white by ratio (0..1). Used for tints."""
    r, g, b = _rgb(hexs)
    r = round(r + (255 - r) * ratio)
    g = round(g + (255 - g) * ratio)
    b = round(b + (255 - b) * ratio)
    return f"#{r:02x}{g:02x}{b:02x}"


# --------------------------------------------------------------------------
# stage 0: frontmatter + component preprocessing
# --------------------------------------------------------------------------

def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Peel a leading '---\\n ... \\n---' block into a flat dict.

    Deliberately not a real YAML parser: this only needs flat 'key: value' lines
    so the script keeps its zero-dependency promise. Any line without a colon is
    ignored. Everything after the closing '---' is the document body.
    """
    if not text.lstrip().startswith("---"):
        return {}, text
    m = re.match(r"^\s*---[ \t]*\n(.*?)\n---[ \t]*\n?", text, re.S)
    if not m:
        return {}, text
    fm: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, text[m.end():]


def _fence(text: str, kind: str, repl) -> str:
    """Rewrite '::: <kind> <title>' ... ':::' fences via repl(title, body)."""
    pattern = r"^:::[ \t]*" + kind + r"[ \t]*([^\n]*)\n(.*?)\n:::[ \t]*$"
    return re.sub(pattern, lambda m: repl(m.group(1).strip(), m.group(2).strip("\n")),
                  text, flags=re.S | re.M)


def preprocess_notes(text: str) -> str:
    """'::: note <title>' -> highlighted callout box."""
    def repl(title: str, body: str) -> str:
        body = re.sub(r"\n(?=\s*\*\*)", "\n\n", body)
        head = f'<div class="note-hd">{_html.escape(title)}</div>\n' if title else ""
        return (f'\n<div class="note" markdown="1">\n{head}'
                f'<div class="note-bd" markdown="1">\n\n{body}\n\n</div>\n</div>\n')
    return _fence(text, "note", repl)


def preprocess_flow(text: str) -> str:
    """'::: flow' -> horizontal step diagram; one step per line 'title | subtitle'."""
    def repl(_title: str, body: str) -> str:
        parts = []
        for raw in body.splitlines():
            line = raw.strip().lstrip("-").strip()
            if not line:
                continue
            if "|" in line:
                t, d = line.split("|", 1)
            else:
                t, d = line, ""
            t, d = _html.escape(t.strip()), _html.escape(d.strip())
            if parts:
                parts.append('<div class="flow-arrow">&#10132;</div>')
            desc = f'<div class="flow-d">{d}</div>' if d else ""
            parts.append(f'<div class="flow-step"><div class="flow-t">{t}</div>{desc}</div>')
        return '\n<div class="flow">' + "".join(parts) + "</div>\n"
    return _fence(text, "flow", repl)


def preprocess_cards(text: str) -> str:
    """'::: card <title>' -> rounded sentence card, one bold-labelled line per field."""
    def repl(title: str, body: str) -> str:
        body = re.sub(r"\n(?=\s*\*\*)", "\n\n", body)
        head = f'<div class="scard-hd">{_html.escape(title)}</div>\n' if title else ""
        return (f'\n<div class="scard" markdown="1">\n{head}'
                f'<div class="scard-bd" markdown="1">\n\n{body}\n\n</div>\n</div>\n')
    return _fence(text, "card", repl)


def build_cover(fm: dict[str, str]) -> str:
    """Diagonal two-colour cover page from frontmatter, or '' when no title."""
    title = fm.get("title", "").strip()
    if not title:
        return ""
    kicker = _html.escape((fm.get("header") or "").strip())
    subtitle = _html.escape(fm.get("subtitle", "").strip())
    stamp = _html.escape(fm.get("stamp", "").strip())
    lines = []
    for key, val in fm.items():
        if key.startswith("meta_") and val:
            label = _html.escape(key[len("meta_"):].strip())
            lines.append(f'<div class="cov-line"><span class="cov-k">{label}</span>'
                         f'<span class="cov-v">{_html.escape(val)}</span></div>')
    footer = f'<div class="cov-foot">{"".join(lines)}</div>' if lines else ""
    stamp_html = f'<div class="cov-stamp">{stamp}</div>' if stamp else ""
    bottom = ('<div class="cov-bottom"><div class="cov-rule"></div>'
              f'{footer}</div>') if (footer or True) else ""
    return (
        '<section class="cover"><div class="cov-tri"></div>'
        f'{stamp_html}'
        '<div class="cov-top">'
        f'{f"<div class=cov-kicker>{kicker}</div>" if kicker else ""}'
        f'<h1 class="cov-title">{_html.escape(title)}</h1>'
        f'{f"<p class=cov-sub>{subtitle}</p>" if subtitle else ""}'
        '</div>'
        f'{bottom}'
        '</section>'
    )


# --------------------------------------------------------------------------
# stage 1: markdown -> HTML
# --------------------------------------------------------------------------

def render_markdown(text: str) -> str:
    """Convert markdown to HTML with whichever parser is installed."""
    try:
        import markdown  # python-markdown
        return markdown.markdown(
            text,
            # nl2br is deliberately absent: it would freeze hard-wrapped
            # paragraphs into ragged <br> breaks. md_in_html lets markdown run
            # inside the component <div markdown="1"> wrappers.
            extensions=["tables", "fenced_code", "sane_lists", "attr_list",
                        "toc", "md_in_html"],
            output_format="html5",
        )
    except ImportError:
        pass
    try:
        from markdown_it import MarkdownIt  # markdown-it-py
        return MarkdownIt("commonmark").enable("table").render(text)
    except ImportError:
        pass
    sys.exit(
        "no markdown parser found. Install either:\n"
        "    pip install markdown\n"
        "    pip install markdown-it-py"
    )


def parser_name() -> str:
    try:
        import markdown
        return f"python-markdown {markdown.__version__}"
    except ImportError:
        pass
    try:
        import markdown_it
        return f"markdown-it-py {getattr(markdown_it, '__version__', '?')}"
    except ImportError:
        return "NONE"


# --------------------------------------------------------------------------
# stage 2: HTML -> PDF
# --------------------------------------------------------------------------
RENDERERS = [
    ("chromium", ["chrome", "google-chrome", "google-chrome-stable", "chromium",
                  "chromium-browser", "msedge", "microsoft-edge",
                  "microsoft-edge-stable", "brave-browser"]),
    ("wkhtmltopdf", ["wkhtmltopdf"]),
    ("weasyprint", ["weasyprint"]),
]

FALLBACK_PATHS = {
    "Windows": [
        r"%ProgramFiles%\Microsoft\Edge\Application\msedge.exe",
        r"%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe",
        r"%ProgramFiles%\Google\Chrome\Application\chrome.exe",
        r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe",
        r"%LocalAppData%\Google\Chrome\Application\chrome.exe",
        r"%ProgramFiles%\BraveSoftware\Brave-Browser\Application\brave.exe",
    ],
    "Darwin": [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    ],
    "Linux": [
        "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
        "/usr/bin/microsoft-edge", "/snap/bin/chromium",
        "/opt/google/chrome/chrome",
    ],
}


def find_renderer() -> tuple[str, str] | tuple[None, None]:
    override = os.environ.get("MD2PDF_ENGINE")
    if override:
        exe = shutil.which(override) or (override if os.path.isfile(override) else None)
        if exe:
            name = Path(exe).stem.lower()
            for kind, names in RENDERERS:
                if any(n in name for n in names) or kind in name:
                    return kind, exe
            return "chromium", exe   # assume browser-like
        print(f"warning: MD2PDF_ENGINE={override} not found, falling back", file=sys.stderr)

    for kind, names in RENDERERS:
        for n in names:
            exe = shutil.which(n)
            if exe:
                return kind, exe

    for raw in FALLBACK_PATHS.get(platform.system(), []):
        exe = os.path.expandvars(raw)
        if "%" not in exe and os.path.isfile(exe):
            return "chromium", exe

    return None, None


def html_to_pdf(kind: str, exe: str, html_path: Path, pdf_path: Path) -> None:
    url = html_path.resolve().as_uri()
    if pdf_path.exists():
        pdf_path.unlink()
    if kind == "chromium":
        # Chrome 150+ writes the PDF within a second or two but then refuses to
        # exit (both old --headless and --headless=new hang here). Blocking on
        # subprocess.run would stall for the whole timeout, so launch it in the
        # background, poll the output file, and kill Chrome once the size stops
        # changing. --headless=new honours print-color-adjust:exact, so the
        # coloured cover / table headers actually print.
        profile = tempfile.mkdtemp(prefix="md2pdf_profile_")
        cmd = [exe, "--headless=new", "--disable-gpu", "--no-first-run",
               "--no-pdf-header-footer", "--disable-extensions",
               f"--user-data-dir={profile}", f"--print-to-pdf={pdf_path}", url]
        proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        last, stable = -1, 0
        for _ in range(150):                       # up to ~60s
            if proc.poll() is not None:
                break
            if pdf_path.exists():
                size = pdf_path.stat().st_size
                if size > 0 and size == last:
                    stable += 1
                    if stable >= 3:
                        break
                else:
                    stable = 0
                last = size
            time.sleep(0.4)
        if proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
        shutil.rmtree(profile, ignore_errors=True)
        return
    if kind == "wkhtmltopdf":
        cmd = [exe, "--enable-local-file-access", "--quiet",
               str(html_path), str(pdf_path)]
    elif kind == "weasyprint":
        cmd = [exe, str(html_path), str(pdf_path)]
    else:
        raise RuntimeError(f"unknown renderer kind: {kind}")
    subprocess.run(cmd, timeout=240, capture_output=True)


# --------------------------------------------------------------------------
# styling
# --------------------------------------------------------------------------
SANS = ("'Segoe UI', 'Helvetica Neue', Arial, "
        "'Microsoft YaHei', 'PingFang SC', 'Hiragino Sans GB', "
        "'Noto Sans CJK SC', 'Source Han Sans SC', 'WenQuanYi Micro Hei', sans-serif")
SERIF = ("'Times New Roman', Georgia, "
         "'Songti SC', 'SimSun', 'Noto Serif CJK SC', 'Source Han Serif SC', serif")
MONO = "Consolas, Menlo, 'DejaVu Sans Mono', 'Courier New', monospace"

CSS = """
@page {{ size: A4; margin: 17mm 15mm; }}
@page {{ @top-right {{ content: "{header}"; color: {mute}; font-size: 8pt;
                      font-family: {body_font}; }} }}
@page :first {{ margin: 0; @top-right {{ content: ""; }} }}
html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
body {{ font-family: {body_font}; font-size: 10.5pt; line-height: 1.62;
        color: {ink}; margin: 0; word-wrap: break-word; background: #fff; }}

/* ---- cover (diagonal split) ---- */
.cover {{ position: relative; height: 100vh; box-sizing: border-box;
          padding: 34mm 22mm 20mm; background: {primary}; color: #fff;
          display: flex; flex-direction: column;
          page-break-after: always; break-after: page; overflow: hidden; }}
.cov-tri {{ position: absolute; inset: 0; z-index: 0; background: {accent};
            clip-path: polygon(100% 42%, 100% 100%, 20% 100%); }}
.cov-top {{ position: relative; z-index: 1; margin-top: 8mm; }}
.cov-bottom {{ position: relative; z-index: 1; margin-top: auto; }}
.cov-kicker {{ font-family: {sans}; letter-spacing: .24em; font-size: 10pt;
               font-weight: 700; color: rgba(255,255,255,.85);
               text-transform: uppercase; }}
.cov-title {{ font-family: {serif}; font-size: 34pt; line-height: 1.18;
              color: #fff; margin: 12mm 0 6mm; border: none; padding: 0; }}
.cov-sub {{ font-family: {sans}; font-size: 13pt; color: rgba(255,255,255,.92);
            line-height: 1.6; max-width: 120mm; margin: 0; }}
.cov-rule {{ border-top: 1px solid rgba(255,255,255,.35); margin-bottom: 7mm;
             max-width: 120mm; }}
.cov-foot {{ font-family: {sans}; font-size: 9pt; color: rgba(255,255,255,.82);
             line-height: 1.85; max-width: 120mm; }}
.cov-line .cov-k {{ font-weight: 700; color: #fff; }}
.cov-line .cov-k::after {{ content: "："; }}
.cov-stamp {{ position: absolute; top: 30mm; right: 20mm; transform: rotate(-8deg);
              border: 2px solid rgba(255,255,255,.9); color: #fff; font-family: {sans};
              font-weight: 800; font-size: 12pt; letter-spacing: .05em;
              padding: 5px 12px; border-radius: 4px; z-index: 2; }}

/* ---- headings ---- */
h1 {{ font-family: {serif}; font-size: 20pt; margin: 0 0 .55em; color: {primary};
      padding-bottom: .22em; border-bottom: 3px solid {accent}; }}
h2 {{ font-size: 14.5pt; margin: 1.5em 0 .5em; color: {primary};
      padding-bottom: .16em; border-bottom: 1px solid {line}; }}
h3 {{ font-size: 12pt; margin: 1.25em 0 .4em; color: {primary}; }}
h4 {{ font-size: 11pt; margin: 1em 0 .35em; color: #333; }}
h1, h2, h3, h4 {{ page-break-after: avoid; break-after: avoid; }}
p, li {{ orphans: 2; widows: 2; }}

/* ---- callout note ---- */
.note {{ background: {note_bg}; border-left: 4px solid {accent}; border-radius: 4px;
         padding: 9px 14px; margin: 12px 0; page-break-inside: avoid; }}
.note-hd {{ font-family: {sans}; font-weight: 700; color: {primary};
            font-size: 10pt; margin-bottom: 3px; }}
.note-bd p {{ margin: 0 0 5px; }}
.note-bd p:last-child {{ margin-bottom: 0; }}

/* ---- flow / step diagram ---- */
.flow {{ display: flex; flex-wrap: wrap; align-items: stretch; gap: 6px 4px;
         margin: 12px 0; page-break-inside: avoid; }}
.flow-step {{ flex: 1 1 0; min-width: 90px; background: {step_bg};
              border: 1px solid {step_bd}; border-top: 3px solid {accent};
              border-radius: 6px; padding: 8px 10px; }}
.flow-t {{ font-family: {sans}; font-weight: 700; color: {primary}; font-size: 10pt; }}
.flow-d {{ font-size: 8.6pt; color: #444; margin-top: 2px; line-height: 1.4; }}
.flow-arrow {{ display: flex; align-items: center; color: {accent};
               font-size: 15pt; font-weight: 700; padding: 0 1px; }}

/* ---- sentence cards ---- */
.scard {{ border: 1px solid {line}; border-radius: 7px; background: #fff;
          margin: 9px 0; padding: 0; overflow: hidden;
          page-break-inside: avoid; break-inside: avoid; }}
.scard-hd {{ background: {card_hd}; color: {primary}; font-family: {sans};
             font-weight: 700; font-size: 9pt; letter-spacing: .03em;
             padding: 5px 12px; border-bottom: 1px solid {line}; }}
.scard-bd {{ padding: 8px 12px 4px; }}
.scard-bd p {{ margin: 0 0 6px; line-height: 1.55; }}
.scard-bd strong {{ display: inline-block; min-width: 4.6em; color: {accent};
                    font-weight: 700; margin-right: 4px; }}

/* ---- tables: coloured header + zebra ---- */
table {{ border-collapse: collapse; width: 100%; margin: .8em 0; font-size: 8.9pt;
         table-layout: fixed; }}
th, td {{ border: 1px solid {line}; padding: 5px 7px; text-align: left; vertical-align: top; }}
th {{ background: {primary}; color: #fff; font-weight: 600; border-color: {primary}; }}
tbody tr:nth-child(even) {{ background: {zebra}; }}
tr {{ page-break-inside: avoid; break-inside: avoid; }}

code {{ font-family: {mono_font}; font-size: 9.2pt; background: {zebra};
        padding: 1px 4px; border-radius: 3px; }}
pre {{ background: {zebra}; border: 1px solid {line}; border-radius: 4px;
       padding: 9px 11px; white-space: pre-wrap; word-break: break-all;
       font-size: 9pt; page-break-inside: avoid; }}
pre code {{ background: none; padding: 0; }}
blockquote {{ margin: .8em 0; padding: .3em 0 .3em 12px;
              border-left: 3px solid {accent}; color: #444; }}
ul, ol {{ padding-left: 1.6em; margin: .5em 0; }}
hr {{ border: none; border-top: 1px solid {line}; margin: 1.6em 0; }}
a {{ color: {primary}; text-decoration: none; }}
strong {{ font-weight: 600; }}
"""

HTML = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{title}</title>
<style>{css}</style></head><body>
{cover}
{body}
</body></html>
"""


def _visual_len(cell_html: str) -> int:
    text = re.sub(r"<[^>]+>", "", cell_html)
    return sum(2 if "\u4e00" <= ch <= "\u9fff" or "\u3000" <= ch <= "\u303f" else 1
               for ch in text)


def add_colgroups(html: str, floor_pct: float = 7.0) -> str:
    """Insert a content-derived <colgroup> into every table.

    table-layout:fixed is the only reliable way to stop a narrow CJK column from
    collapsing to one glyph per line. Fixed layout ignores content, so widths are
    supplied here; sqrt of the longest cell keeps one long column from starving
    the others.
    """
    def one(match: re.Match) -> str:
        table = match.group(0)
        rows = re.findall(r"<tr[^>]*>(.*?)</tr>", table, re.S)
        if not rows:
            return table
        widths: list[int] = []
        for row in rows:
            for i, c in enumerate(re.findall(r"<(?:th|td)[^>]*>(.*?)</(?:th|td)>", row, re.S)):
                v = _visual_len(c)
                if i < len(widths):
                    widths[i] = max(widths[i], v)
                else:
                    widths.append(v)
        if len(widths) < 2:
            return table
        raw = [max(1.0, w) ** 0.5 for w in widths]
        pct = [max(floor_pct, 100.0 * r / sum(raw)) for r in raw]
        scale = 100.0 / sum(pct)
        cols = "".join(f'<col style="width:{p * scale:.1f}%">' for p in pct)
        return re.sub(r"<table[^>]*>", lambda m: m.group(0) + f"<colgroup>{cols}</colgroup>",
                      table, count=1)

    return re.sub(r"<table[^>]*>.*?</table>", one, html, flags=re.S)


def build_css(fm: dict[str, str], serif: bool) -> str:
    primary = _norm_hex(fm.get("primary", ""), PRIMARY_DEFAULT)
    accent = _norm_hex(fm.get("accent", ""), ACCENT_DEFAULT)
    return CSS.format(
        body_font=SERIF if serif else SANS, sans=SANS, serif=SERIF, mono_font=MONO,
        primary=primary, accent=accent,
        note_bg=_rgba(accent, 0.08), card_hd=_rgba(accent, 0.12),
        step_bg=_mix_white(primary, 0.94), step_bd=_mix_white(primary, 0.72),
        zebra=_mix_white(primary, 0.955), line="#e4e4e4",
        ink="#1b1b1b", mute="#6a6a6a", header=fm.get("header", ""),
    )


# --------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------

def convert(md_path: Path, kind: str, exe: str, serif: bool, keep_html: bool) -> bool:
    md_path = md_path.resolve()
    pdf_path = md_path.with_suffix(".pdf")
    # utf-8-sig, not utf-8: PowerShell's Out-File -Encoding UTF8 writes a BOM,
    # and a leading BOM stops a first-line "# heading" from being recognised.
    raw = md_path.read_text(encoding="utf-8-sig")
    fm, text = split_frontmatter(raw)
    text = preprocess_cards(preprocess_flow(preprocess_notes(text)))
    body = add_colgroups(render_markdown(text))
    html = HTML.format(
        title=fm.get("title") or md_path.stem,
        css=build_css(fm, serif),
        cover=build_cover(fm),
        body=body,
    )

    if keep_html:
        html_path = md_path.with_suffix(".html")
    else:
        fd, tmp = tempfile.mkstemp(suffix=".html", prefix="md2pdf_")
        os.close(fd)
        html_path = Path(tmp)
    html_path.write_text(html, encoding="utf-8")

    try:
        html_to_pdf(kind, exe, html_path, pdf_path)
    except subprocess.TimeoutExpired:
        print(f"  TIMEOUT  {md_path.name}")
        return False
    except Exception as exc:                      # noqa: BLE001 - report and continue
        print(f"  ERROR    {md_path.name}: {exc}")
        return False

    if not keep_html:
        try:
            html_path.unlink()
        except OSError:
            pass

    if pdf_path.exists() and pdf_path.stat().st_size > 0:
        print(f"  OK       {md_path.name} -> {pdf_path.name}  ({pdf_path.stat().st_size:,} bytes)")
        return True
    print(f"  FAILED   {md_path.name}")
    return False


def report_environment() -> int:
    kind, exe = find_renderer()
    print(f"platform : {platform.system()} {platform.release()}")
    print(f"python   : {sys.version.split()[0]}")
    print(f"parser   : {parser_name()}")
    print(f"renderer : {kind or 'NONE'}{'  ' + exe if exe else ''}")
    if kind and parser_name() != "NONE":
        print("\nready")
        return 0
    print("\nNOT ready. Fix whichever line says NONE:")
    if parser_name() == "NONE":
        print("  parser  : pip install markdown")
    if not kind:
        print("  renderer: install any Chromium-family browser, or wkhtmltopdf,")
        print("            or weasyprint; or set MD2PDF_ENGINE to its full path")
    return 1


def main() -> None:
    ap = argparse.ArgumentParser(description="md -> PDF for kkstoryline / yfnskills deliverables")
    ap.add_argument("target", nargs="?", help="a .md file or a directory of .md files")
    ap.add_argument("--serif", action="store_true", help="serif stack (paper-like)")
    ap.add_argument("--keep-html", action="store_true", help="keep the intermediate .html")
    ap.add_argument("--check", action="store_true", help="report this machine's capability")
    args = ap.parse_args()

    if args.check:
        sys.exit(report_environment())
    if not args.target:
        ap.error("target is required unless --check is given")

    kind, exe = find_renderer()
    if not kind:
        sys.exit("no HTML-to-PDF renderer found; run with --check for guidance")
    print(f"renderer: {kind} ({exe})")

    target = Path(args.target)
    if target.is_dir():
        files = sorted(target.glob("*.md"))
    elif target.is_file():
        files = [target]
    else:
        sys.exit(f"not found: {target}")
    if not files:
        sys.exit(f"no .md files under {target}")

    ok = sum(convert(f, kind, exe, args.serif, args.keep_html) for f in files)
    print(f"\n{ok}/{len(files)} converted")
    sys.exit(0 if ok == len(files) else 1)


if __name__ == "__main__":
    main()
