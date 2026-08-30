# 产物命名（venue + 时间戳）

每次干活的输出目录和报告文件必须带投稿目标和时间戳，方便同一稿多投、多次修改互不覆盖。

## 格式

```
<前缀>_<venue>_<YYYYMMDD-HHMM>
```

- **venue**：官方短名。IEEE TIP → `TIP`，ICASSP → `ICASSP`，Pattern Recognition → `PR`。空格改下划线，只留字母数字和下划线，不用中文全称、不用空格、不用斜杠。
- **时间戳**：开工那一刻的本地时间，精确到分钟，例 `20260831-0021`。
- **没给 venue 先问再动手**。禁止 `unknown`、`tmp`、默认名、光写时间戳。吃透档案或用户消息里已经有目标 venue 的，直接用，不必再问。
- 同一分钟开两次，后面加 `-2`、`-3`。

## 各模式对照

| 模式 | 路径 |
|---|---|
| kkstoryline | 论文旁边 `kkstoryline_work_<venue>_<YYYYMMDD-HHMM>/` |
| 润色（超两段） | `polish_reports/<venue>_<YYYYMMDD-HHMM>-润色对照.md` |
| 审稿 | `paper_reviews/<venue>_<YYYYMMDD-HHMM>/` |
| 终检 | `final_check/<venue>_<YYYYMMDD-HHMM>-终检报告.md` |
| 找创新点 | `ideation/<主题>_<venue>_<YYYYMMDD-HHMM>/` |
| yfnskills 任务夹 | 在它自己的 `polish-vN/` 等名字前加同一套前缀，或把整个任务夹放进 `yfn_<venue>_<YYYYMMDD-HHMM>/` |

## 例外

`paper_context/<稿件名>/` 是跨轮次吃透档案，目录不加时间戳，否则后续模式找不到。但 `00-anchor.md` 必须写目标 venue，换 venue 时在档案里记一行，不另开目录。

## 续跑

用户说从某步继续、重跑某步时，先按 venue 找最新那份时间戳目录。指定了完整目录名就用指定的。旧的光秃名 `kkstoryline_work/` 若还在，当历史目录读，新跑一律用带 venue 和时间戳的名字。
