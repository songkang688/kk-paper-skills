# Git 使用说明

本仓库地址：https://github.com/songkang688/kk-paper-skills

论文项目里日常用不到这些命令。对 Agent 说那句「去远程 github 帮我拉取并安装局部 skills」即可，脚本会自己 clone 或 pull。下面给要自己动手，或要维护本仓库的人。

## 第一次拿到仓库

HTTPS（已登录 `gh` 或配好凭据）：

```bash
git clone https://github.com/songkang688/kk-paper-skills.git
```

SSH：

```bash
git clone git@github.com:songkang688/kk-paper-skills.git
```

GitHub CLI（私有库最省事）：

```bash
gh repo clone songkang688/kk-paper-skills
```

这只是把源仓库放到磁盘上。要让当前论文项目用起来，还要再跑 `install.sh --project <论文项目>`，或让 Agent 按 `docs/install.md` 装局部 skills。不要把本仓库根目录当成论文项目去装。

## 装到某个论文项目（局部）

```bash
cd /path/to/your-paper
curl -fsSL https://raw.githubusercontent.com/songkang688/kk-paper-skills/main/install.sh | bash
```

效果是：论文项目里出现 `.kk-paper-skills`（一次完整 clone），各 skill 软链到 `.agents/skills/`，并写好路由规则。源仓库继续独立更新，论文项目不必把整套 skill 提交进去。

## 以后更新

在论文项目里：

```bash
git -C .kk-paper-skills pull --ff-only
```

或再跑一遍 `install.sh`，它会先 pull 再重写链接。

在本仓库的工作副本里（你改规则、改路由时）：

```bash
git pull --ff-only
git add -A
git commit -m "说明为什么改"
git push
```

不要用 `git pull` 默认的 merge 提交把历史打乱。快进不了时先看分歧，再决定 rebase 还是合并。

## 换机器

新电脑上对 Agent 再说一遍安装那句话，或在论文项目根目录重跑 `install.sh`。凭据要先有：`gh auth login`，或把 SSH key 加到 GitHub。

本机用户级那套 `~/.agents/skills` 是另一条线，跟项目局部互不影响。项目规则只认项目里的 `.agents/skills`。

## 常见情况

- **私有库 clone 失败**：先 `gh auth login`，或改用 `git@github.com:songkang688/kk-paper-skills.git`。
- **想跟论文仓库一起提交 skill**：`install.sh --copy`，再决定要不要把 `.agents/skills` 纳入论文仓库。默认软链加 `.kk-paper-skills/` 进 gitignore，是为了不把整套 skill 原样塞进每篇论文。
- **已经全局装过**：局部安装仍然要做。Cloud Agent 和别人克隆你的论文项目时，看不到你家里的 `~/.cursor/skills`。
- **不要 force push 到 main**，除非你明确知道自己在覆盖什么。
