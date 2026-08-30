#!/usr/bin/env python3
"""Render the kk-paper-skills overview poster. Run from anywhere."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / "skill-overview.png"

W, H = 2880, 1780
BG = (246, 243, 236)
NAVY = (22, 36, 64)
NAVY2 = (36, 54, 92)
INK = (28, 32, 38)
MUTED = (92, 98, 108)
WHITE = (255, 255, 255)
LINE = (220, 214, 204)
GOLD = (201, 162, 79)

GROUPS = [
    {
        "title": "选题检索",
        "hint": "先学再定思路",
        "color": (38, 122, 128),
        "items": [
            ("research-gap", "多维趋势找研究缺口"),
            ("topic-framing", "模糊想法收敛成选题"),
            ("conf-search", "顶会论文检索"),
            ("lit-search", "顶刊与相关工作检索"),
            ("nature-reader", "中英对照精读翻译"),
        ],
    },
    {
        "title": "实验",
        "hint": "代码跑出写作原料",
        "color": (176, 112, 36),
        "items": [
            ("auto-experiment", "自动实验循环"),
            ("experiment-status", "训练进度与记录"),
            ("gpu-monitor", "GPU 空闲与占用"),
        ],
    },
    {
        "title": "写作排版",
        "hint": "定真假再写故事再润色",
        "color": (46, 102, 76),
        "items": [
            ("paper-skill", "框架、模板、防造假占位"),
            ("research-paper-writing", "章节初稿与 CV 叙事"),
            ("scipilot-writing-skill", "逐句润色、去 AI 味"),
            ("latex-writer", "LaTeX 编译与公式排版"),
            ("scientific-visualization", "实验图与消融图"),
        ],
    },
    {
        "title": "改稿",
        "hint": "风格流水线与版本对比",
        "color": (92, 68, 140),
        "items": [
            ("yfnskills", "袁老师风格起草润色 rebuttal"),
            ("kkstoryline", "故事线升级加逐句润色"),
            ("paragraph-compare-polish", "同段落多版本对比推荐"),
            ("paper-version-compare", "多方案排名与主线抉择"),
        ],
    },
    {
        "title": "审稿",
        "hint": "五团并行，父进程综合",
        "color": (154, 58, 58),
        "items": [
            ("reviewforge-openreview", "OpenReview 五人审 + 总评"),
            ("aaai-review-simulator", "会议向 Fatal / Major / Minor"),
            ("academic-paper-reviewer", "期刊向 + 魔鬼代言人"),
            ("scholar-evaluation", "逐维打分"),
            ("peer-review", "八维评分加雷达图"),
        ],
    },
    {
        "title": "投稿收尾",
        "hint": "核验、选刊、回复、汇报",
        "color": (64, 84, 112),
        "items": [
            ("cite-verify", "参考文献真假核验"),
            ("journal-match", "按范围与影响力选期刊"),
            ("nature-response", "rebuttal 与修回信"),
            ("nature-paper2ppt", "论文转组会中文 PPT"),
            ("progress-report", "研究进展结构化汇报"),
        ],
    },
]

MODES = [
    "接稿吃透",
    "找创新点",
    "写初稿",
    "润色四列表",
    "五团审稿",
    "十步终检",
    "一致性检查",
    "实验闭环",
]


def font(path, size, index=0):
    return ImageFont.truetype(path, size, index=index)


def pick_fonts():
    hei = "/System/Library/Fonts/Hiragino Sans GB.ttc"
    st = "/System/Library/Fonts/STHeiti Medium.ttc"
    menlo = "/System/Library/Fonts/Menlo.ttc"
    title = font(hei, 62, 0)
    sub = font(hei, 28, 0)
    group = font(hei, 34, 0)
    hint = font(hei, 22, 0)
    skill = font(menlo, 22, 0)
    desc = font(hei, 22, 0)
    chip = font(hei, 22, 0)
    footer = font(hei, 22, 0)
    badge = font(hei, 24, 0)
    # fallback if Menlo missing
    try:
        skill.getmask("kk")
    except Exception:
        skill = font(st, 22, 0)
    return title, sub, group, hint, skill, desc, chip, footer, badge


def rounded(draw, box, r, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)


def text_w(draw, text, fnt):
    return int(draw.textlength(text, font=fnt))


def main():
    title_f, sub_f, group_f, hint_f, skill_f, desc_f, chip_f, footer_f, badge_f = pick_fonts()
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # header
    rounded(d, (0, 0, W, 210), 0, NAVY)
    d.rectangle((0, 210, W, 218), fill=GOLD)

    d.text((72, 42), "KK Paper Skills", font=title_f, fill=WHITE)
    d.text((72, 122), "写 AI / CV 论文的本地技能工作台  ·  一句话说要干什么，路由转发", font=sub_f, fill=(210, 216, 228))

    # right-side stats
    stats = [("28", "技能"), ("1", "总路由"), ("8", "模式")]
    x = W - 72
    for num, lab in reversed(stats):
        box_w = 150
        x -= box_w + 18
        rounded(d, (x, 48, x + box_w, 158), 18, NAVY2)
        tw = text_w(d, num, title_f)
        d.text((x + (box_w - tw) / 2, 52), num, font=title_f, fill=GOLD)
        lw = text_w(d, lab, badge_f)
        d.text((x + (box_w - lw) / 2, 118), lab, font=badge_f, fill=(200, 208, 220))

    # router chip under header
    router = "总路由  kk-paper-router"
    rw = text_w(d, router, badge_f) + 48
    rx = 72
    rounded(d, (rx, 236, rx + rw, 288), 16, NAVY)
    d.text((rx + 24, 246), router, font=badge_f, fill=WHITE)

    # mode chips
    mx = rx + rw + 20
    my = 236
    for mode in MODES:
        mw = text_w(d, mode, chip_f) + 36
        if mx + mw > W - 72:
            break
        rounded(d, (mx, my, mx + mw, 288), 16, WHITE, outline=LINE, width=2)
        d.text((mx + 18, 248), mode, font=chip_f, fill=INK)
        mx += mw + 12

    # group grid 2 x 3
    left, top = 72, 324
    right, bottom = W - 72, H - 88
    gap = 28
    cols, rows = 3, 2
    cw = (right - left - gap * (cols - 1)) / cols
    rh = (bottom - top - gap * (rows - 1)) / rows

    for i, g in enumerate(GROUPS):
        r, c = divmod(i, cols)
        x0 = left + c * (cw + gap)
        y0 = top + r * (rh + gap)
        x1, y1 = x0 + cw, y0 + rh
        rounded(d, (x0, y0, x1, y1), 24, WHITE, outline=LINE, width=2)
        rounded(d, (x0 + 10, y0 + 18, x0 + 22, y1 - 18), 6, g["color"])
        d.text((x0 + 40, y0 + 28), g["title"], font=group_f, fill=INK)
        d.text((x0 + 40, y0 + 76), g["hint"], font=hint_f, fill=MUTED)
        nlab = f"{len(g['items'])} 个技能"
        nw = text_w(d, nlab, hint_f)
        d.text((x1 - 36 - nw, y0 + 34), nlab, font=hint_f, fill=g["color"])

        inner_top = y0 + 124
        inner_bot = y1 - 28
        n = len(g["items"])
        row_h = min(92, (inner_bot - inner_top) / max(n, 1))
        for j, (name, desc) in enumerate(g["items"]):
            yy = inner_top + j * row_h
            row_box = (x0 + 36, yy, x1 - 24, yy + row_h - 10)
            rounded(d, row_box, 12, (248, 246, 241))
            cy = yy + (row_h - 10) / 2
            d.ellipse((x0 + 52, cy - 7, x0 + 66, cy + 7), fill=g["color"])
            d.text((x0 + 82, yy + 12), name, font=skill_f, fill=NAVY)
            d.text((x0 + 82, yy + 46), desc, font=desc_f, fill=MUTED)

    # footer
    foot = "技能互通 · 接稿吃透档案全程流转 · 不编造数据、引用与官方政策"
    fw = text_w(d, foot, footer_f)
    d.text(((W - fw) / 2, H - 58), foot, font=footer_f, fill=MUTED)

    img.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT}  {img.size[0]}x{img.size[1]}")


if __name__ == "__main__":
    main()
