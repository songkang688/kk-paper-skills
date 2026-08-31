# 安装协议（给 Agent 和人看）

用户只要说这一句，就按下面做，不要中途停下来问要不要全局装还是局部装。默认装到**当前论文项目**，不写进 `~/.cursor/skills`。

> 去远程 github 帮我拉取 kk-paper-skills 到本地并安装局部 skills
> https://github.com/songkang688/kk-paper-skills

## 你要做的四件事

1. 确认当前工作区是论文项目根目录，不是本仓库自己。
2. 跑安装脚本（优先这一条，不要手写一长串 ln）。
3. 确认项目里已经有路由规则：`.cursor/rules/kk-paper-router.mdc`、`AGENTS.md`、`CLAUDE.md`。
4. 用一句话告诉用户装好了、下次直接说要干什么。

## 一条命令

在论文项目根目录：

```bash
curl -fsSL https://raw.githubusercontent.com/songkang688/kk-paper-skills/main/install.sh | bash
```

仓库已经在本地时：

```bash
bash /path/to/kk-paper-skills/install.sh --project "$(pwd)"
```

本机已有 clone、只想重装链接：

```bash
bash /path/to/kk-paper-skills/install.sh --project "$(pwd)" --source /path/to/kk-paper-skills
```

私有库先登录 GitHub。有 `gh` 时脚本会优先走 `gh repo clone`。没有就用 `git clone`，需要 SSH key 或已缓存的 HTTPS 凭据。

## 装完之后项目里会长出什么

```text
<论文项目>/
├── .kk-paper-skills/                 # 本仓库的本地克隆，默认写进 .gitignore
├── .agents/skills/<各 skill>/        # Cursor 与 Codex 都认，默认软链到上面
├── .claude/skills/<各 skill>/        # Claude Code 认，软链到 .agents/skills
├── .cursor/rules/kk-paper-router.mdc # Cursor：每次会话先走路由
├── AGENTS.md                         # Codex 与 Cursor 开跑前会读
└── CLAUDE.md                         # Claude Code 与 Cursor 始终会读
```

不要只往 `.cursor/skills/` 里装。Codex 和 Claude Code 官方不扫那个目录。

## 更新

同一句话把「拉取」改成「更新」，或再跑一遍 `install.sh`。脚本发现 `.kk-paper-skills` 已存在就 `git pull --ff-only`，再重写链接和规则。
