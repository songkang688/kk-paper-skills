#!/usr/bin/env bash
# md -> PDF wrapper for yfnskills deliverables (macOS / Linux convenience).
#
#   ./md2pdf.sh <file.md | directory> [--serif] [--keep-html]
#   ./md2pdf.sh --check
#
# Locates a Python interpreter, makes sure a markdown parser is importable, then
# calls md2pdf.py. All the real work and all platform detection live in the .py,
# so `python3 md2pdf.py <target>` works identically without this wrapper.
set -euo pipefail

if [ $# -eq 0 ]; then
  echo "usage: $0 <file.md | directory> [--serif] [--keep-html] | --check" >&2
  exit 2
fi

PY=""
for n in python3 python; do
  if command -v "$n" >/dev/null 2>&1; then PY="$n"; break; fi
done
if [ -z "$PY" ]; then
  echo "python not found. Install Python 3 (brew install python / apt install python3)." >&2
  exit 1
fi

if ! "$PY" -c "import markdown" >/dev/null 2>&1 && \
   ! "$PY" -c "import markdown_it" >/dev/null 2>&1; then
  echo "installing a markdown parser..."
  # --user avoids needing root; harmless inside a virtualenv where it is ignored.
  "$PY" -m pip install --quiet --user markdown || {
    echo "no markdown parser and pip install failed (offline?). Run: $PY -m pip install markdown" >&2
    exit 1
  }
fi

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec "$PY" "$DIR/md2pdf.py" "$@"
