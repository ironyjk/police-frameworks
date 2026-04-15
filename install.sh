#!/usr/bin/env bash
set -e

REPO="https://github.com/ironyjk/police-frameworks.git"
TARGET="${HOME}/.claude/skills/police-frameworks"

echo "Police Frameworks installer"
echo "  target: ${TARGET}"

if [ -d "${TARGET}" ]; then
  echo "  existing install found — pulling latest"
  cd "${TARGET}"
  git pull --ff-only
else
  mkdir -p "${HOME}/.claude/skills"
  git clone "${REPO}" "${TARGET}"
fi

echo ""
echo "Installed frameworks:"
for d in "${TARGET}"/*/; do
  name=$(basename "$d")
  if [ -f "${d}SKILL.md" ]; then
    echo "  - ${name}"
  fi
done

echo ""
echo "Done. Use /police to route a situation, or invoke a framework directly (e.g. /sara, /peace-model)."
