#!/usr/bin/env bash
# 把 kk-paper-skills 拉到当前论文项目，装成项目级局部 skills，并写好路由规则。
# 在论文项目根目录执行，不要在本仓库根目录当论文项目装。
set -euo pipefail

REPO_URL="${KK_PAPER_SKILLS_REPO:-https://github.com/songkang688/kk-paper-skills.git}"
REPO_NAME="kk-paper-skills"
CACHE_DIR=""
PROJECT=""
MODE="link"

usage() {
  cat <<'EOF'
用法:
  ./install.sh                      在当前目录装成局部 skills
  ./install.sh --project /path      装到指定论文项目
  ./install.sh --copy               复制进 .agents/skills（默认同名软链）
  ./install.sh --source /path       不重新 clone，用已有仓库当源

环境变量:
  KK_PAPER_SKILLS_REPO   覆盖仓库地址，默认 github.com/songkang688/kk-paper-skills
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --project) PROJECT="${2:-}"; shift 2 ;;
    --source) CACHE_DIR="${2:-}"; shift 2 ;;
    --copy) MODE="copy"; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "未知参数: $1" >&2; usage; exit 1 ;;
  esac
done

if [[ -z "$PROJECT" ]]; then
  PROJECT="$(pwd)"
fi
PROJECT="$(cd "$PROJECT" && pwd)"

is_suite_root() {
  local d="$1"
  [[ -f "$d/kk-paper-router/SKILL.md" && -f "$d/install.sh" ]]
}

if is_suite_root "$PROJECT" && [[ -z "${KK_PAPER_SKILLS_ALLOW_SELF:-}" ]]; then
  echo "当前目录就是 kk-paper-skills 仓库本身。请到论文项目根目录再跑，或加 --project /你的论文项目" >&2
  exit 1
fi

clone_or_pull() {
  local dest="$1"
  if [[ -d "$dest/.git" ]]; then
    echo "已有本地仓库，正在拉取更新: $dest"
    git -C "$dest" pull --ff-only
    return
  fi
  mkdir -p "$(dirname "$dest")"
  echo "正在从远程拉取 $REPO_URL"
  if command -v gh >/dev/null 2>&1 && [[ "$REPO_URL" == *github.com/songkang688/kk-paper-skills* ]]; then
    if gh repo clone songkang688/kk-paper-skills "$dest"; then
      return
    fi
    echo "gh clone 未成功，改用 git clone（私有库需要已登录或已配 SSH）"
  fi
  git clone "$REPO_URL" "$dest"
}

if [[ -z "$CACHE_DIR" ]]; then
  if is_suite_root "$(pwd)" && [[ "$(pwd)" != "$PROJECT" ]]; then
    CACHE_DIR="$(pwd)"
  else
    CACHE_DIR="$PROJECT/.$REPO_NAME"
    clone_or_pull "$CACHE_DIR"
  fi
else
  CACHE_DIR="$(cd "$CACHE_DIR" && pwd)"
  if ! is_suite_root "$CACHE_DIR"; then
    echo "--source 不是 kk-paper-skills 仓库: $CACHE_DIR" >&2
    exit 1
  fi
fi

SKILLS_DST="$PROJECT/.agents/skills"
CLAUDE_DST="$PROJECT/.claude/skills"
RULES_DST="$PROJECT/.cursor/rules"
mkdir -p "$SKILLS_DST" "$CLAUDE_DST" "$RULES_DST"

installed=0
for skill_dir in "$CACHE_DIR"/*/; do
  [[ -f "${skill_dir}SKILL.md" ]] || continue
  name="$(basename "$skill_dir")"
  target="$SKILLS_DST/$name"
  if [[ "$MODE" == "copy" ]]; then
    rm -rf "$target"
    mkdir -p "$target"
    # 解引用软链，保证项目里是完整文件
    rsync -a --delete --exclude '.git' --exclude '.DS_Store' "$skill_dir" "$target/"
  else
    rel="$(python3 -c 'import os,sys; print(os.path.relpath(sys.argv[1], sys.argv[2]))' "$CACHE_DIR/$name" "$SKILLS_DST")"
    ln -sfn "$rel" "$target"
  fi
  ln -sfn "../../.agents/skills/$name" "$CLAUDE_DST/$name"
  installed=$((installed + 1))
done

if [[ "$installed" -eq 0 ]]; then
  echo "源仓库里没有找到带 SKILL.md 的目录: $CACHE_DIR" >&2
  exit 1
fi

cp "$CACHE_DIR/templates/kk-paper-router.mdc" "$RULES_DST/kk-paper-router.mdc"

write_if_missing_or_marker() {
  local dest="$1"
  local src="$2"
  local marker="kk-paper-router"
  if [[ ! -f "$dest" ]]; then
    cp "$src" "$dest"
    return
  fi
  if grep -q "$marker" "$dest"; then
    echo "已有 $dest，里面已经提到路由，不覆盖"
    return
  fi
  {
    echo ""
    echo ""
    cat "$src"
  } >> "$dest"
  echo "已把路由说明追加进 $dest"
}

write_if_missing_or_marker "$PROJECT/AGENTS.md" "$CACHE_DIR/templates/AGENTS.md"
write_if_missing_or_marker "$PROJECT/CLAUDE.md" "$CACHE_DIR/templates/CLAUDE.md"

if [[ -f "$PROJECT/.gitignore" ]] && ! grep -qxF ".$REPO_NAME/" "$PROJECT/.gitignore"; then
  printf '\n# kk-paper-skills 本地克隆（skills 已链到 .agents/skills）\n.%s/\n' "$REPO_NAME" >> "$PROJECT/.gitignore"
fi

echo
echo "安装完成: $installed 个 skill → $SKILLS_DST"
echo "Claude Code 兼容链: $CLAUDE_DST"
echo "Cursor 每次先走路由: $RULES_DST/kk-paper-router.mdc"
echo "Codex / Cursor 还会读: $PROJECT/AGENTS.md"
echo "源仓库: $CACHE_DIR"
echo
echo "之后在这个项目里直接说要干什么即可，不必再点 skill 名。"
