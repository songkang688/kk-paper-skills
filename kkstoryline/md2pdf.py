#!/usr/bin/env python3
"""
md -> PDF for yfnskills deliverables. Portable: no machine-specific paths.

Pipeline is always the same two stages:
    1. markdown -> HTML   (python-markdown, or markdown-it-py as a fallback)
    2. HTML -> PDF        (first renderer found, see RENDERERS below)

Two stages instead of one direct converter because the skill's output routinely
mixes Chinese prose and English paper text inside the same table, and a browser
renders both from system fonts with no font configuration at all. LaTeX-based
routes need per-machine CJK font setup, which is exactly what breaks when you
move to another computer.

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
# stage 1: markdown -> HTML
# --------------------------------------------------------------------------

def render_markdown(text: str) -> str:
    """Convert markdown to HTML with whichever parser is installed."""
    try:
        import markdown  # python-markdown
        return markdown.markdown(
            text,
            # nl2br is deliberately absent: it would freeze hard-wrapped
            # paragraphs into ragged <br> breaks instead of reflowing them.
            extensions=["tables", "fenced_code", "sane_lists", "attr_list", "toc"],
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
# Each renderer: (kind, list of executable names to look for on PATH)
RENDERERS = [
    ("chromium", ["chrome", "google-chrome", "google-chrome-stable", "chromium",
                  "chromium-browser", "msedge", "microsoft-edge",
                  "microsoft-edge-stable", "brave-browser"]),
    ("wkhtmltopdf", ["wkhtmltopdf"]),
    ("weasyprint", ["weasyprint"]),
]

# Fallback locations for GUI browsers that are usually not on PATH.
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
    """Return (kind, executable path)."""
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
    if kind == "chromium":
        profile = tempfile.mkdtemp(prefix="md2pdf_profile_")
        cmd = [exe, "--headless", "--disable-gpu", "--no-first-run",
               "--no-pdf-header-footer", f"--user-data-dir={profile}",
               f"--print-to-pdf={pdf_path}", url]
    elif kind == "wkhtmltopdf":
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
# Font stacks list several CJK families per platform so the same file renders on
# Windows, macOS and Linux without editing anything.
SANS = ("'Segoe UI', 'Helvetica Neue', Arial, "
        "'Microsoft YaHei', 'PingFang SC', 'Hiragino Sans GB', "
        "'Noto Sans CJK SC', 'Source Han Sans SC', 'WenQuanYi Micro Hei', sans-serif")
SERIF = ("'Times New Roman', Georgia, "
         "'SimSun', 'Songti SC', 'Noto Serif CJK SC', 'Source Han Serif SC', serif")
MONO = "Consolas, Menlo, 'DejaVu Sans Mono', 'Courier New', monospace"

CSS = """
@page {{ size: A4; margin: 18mm 16mm; }}
html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
body {{ font-family: {body_font}; font-size: 10.5pt; line-height: 1.62;
        color: #1b1b1b; margin: 0; word-wrap: break-word; }}
h1 {{ font-size: 19pt; margin: 0 0 .5em; padding-bottom: .25em; border-bottom: 2px solid #333; }}
h2 {{ font-size: 14.5pt; margin: 1.5em 0 .5em; padding-bottom: .18em; border-bottom: 1px solid #ccc; }}
h3 {{ font-size: 12pt; margin: 1.25em 0 .4em; }}
h4 {{ font-size: 11pt; margin: 1em 0 .35em; }}
h1, h2, h3, h4 {{ page-break-after: avoid; break-after: avoid; }}
p, li {{ orphans: 2; widows: 2; }}
table {{ border-collapse: collapse; width: 100%; margin: .8em 0; font-size: 8.9pt;
         table-layout: fixed; }}
th, td {{ border: 1px solid #bbb; padding: 4.5px 6px; text-align: left; vertical-align: top; }}
th {{ background: #f0f0f0; font-weight: 600; }}
tr {{ page-break-inside: avoid; break-inside: avoid; }}
code {{ font-family: {mono_font}; font-size: 9.2pt; background: #f4f4f4;
        padding: 1px 4px; border-radius: 3px; }}
pre {{ background: #f6f6f6; border: 1px solid #e0e0e0; border-radius: 4px;
       padding: 9px 11px; white-space: pre-wrap; word-break: break-all;
       font-size: 9pt; page-break-inside: avoid; }}
pre code {{ background: none; padding: 0; }}
blockquote {{ margin: .8em 0; padding: .3em 0 .3em 12px;
              border-left: 3px solid #c8c8c8; color: #444; }}
ul, ol {{ padding-left: 1.6em; margin: .5em 0; }}
hr {{ border: none; border-top: 1px solid #ddd; margin: 1.6em 0; }}
a {{ color: #0b5fa5; text-decoration: none; }}
strong {{ font-weight: 600; }}
"""

HTML = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{title}</title>
<style>{css}</style></head><body>
{body}
</body></html>
"""


def _visual_len(cell_html: str) -> int:
    """Rough rendered width of a cell, counting CJK as two Latin characters."""
    text = re.sub(r"<[^>]+>", "", cell_html)
    return sum(2 if "\u4e00" <= ch <= "\u9fff" or "\u3000" <= ch <= "\u303f" else 1
               for ch in text)


def add_colgroups(html: str, floor_pct: float = 7.0) -> str:
    """Insert a content-derived <colgroup> into every table.

    table-layout:fixed is the only reliable way to stop a narrow CJK column from
    collapsing to one glyph per line (min-width and word-break:keep-all both
    fail: the emergency-break rule overrides keep-all). Fixed layout ignores
    content, so the widths have to be supplied here. sqrt of the longest cell
    keeps one very long column from starving the others.
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


# --------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------

def convert(md_path: Path, kind: str, exe: str, serif: bool, keep_html: bool) -> bool:
    # Absolute, always: a browser given a relative --print-to-pdf target resolves
    # it against its own working directory and silently writes nothing.
    md_path = md_path.resolve()
    pdf_path = md_path.with_suffix(".pdf")
    # utf-8-sig, not utf-8: PowerShell's Out-File -Encoding UTF8 writes a BOM,
    # and a leading BOM stops a first-line "# heading" from being recognised.
    body = add_colgroups(render_markdown(md_path.read_text(encoding="utf-8-sig")))
    html = HTML.format(
        title=md_path.stem,
        css=CSS.format(body_font=SERIF if serif else SANS, mono_font=MONO),
        body=body,
    )

    if keep_html:
        html_path = md_path.with_suffix(".html")
    else:
        fd, tmp = tempfile.mkstemp(suffix=".html", prefix="md2pdf_")
        os.close(fd)
        html_path = Path(tmp)
    html_path.write_text(html, encoding="utf-8")

    if pdf_path.exists():
        pdf_path.unlink()
    try:
        html_to_pdf(kind, exe, html_path, pdf_path)
    except subprocess.TimeoutExpired:
        print(f"  TIMEOUT  {md_path.name}")
        return False
    except Exception as exc:                      # noqa: BLE001 - report and continue
        print(f"  ERROR    {md_path.name}: {exc}")
        return False

    # Some browser builds keep writing after the process exits, so wait for the
    # size to stop changing. Bail out early when nothing appears at all, rather
    # than burning the whole budget on a file that will never exist.
    last, stable = -1, 0
    for i in range(75):
        if pdf_path.exists():
            size = pdf_path.stat().st_size
            if size > 0 and size == last:
                stable += 1
                if stable >= 2:
                    break
            else:
                stable = 0
            last = size
        elif i >= 12:
            break
        time.sleep(0.4)

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
    ap = argparse.ArgumentParser(description="md -> PDF for yfnskills deliverables")
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
