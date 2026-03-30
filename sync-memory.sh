#!/bin/bash
# OpenClaw记忆自动同步脚本

set -e

WORKSPACE_DIR="/root/.openclaw/workspace"
LOG_FILE="/root/.openclaw/sync.log"
MAX_LOG_SIZE=10485760  # 10MB

# 创建日志目录
mkdir -p "$(dirname "$LOG_FILE")"

# 日志轮转
if [ -f "$LOG_FILE" ] && [ $(stat -c%s "$LOG_FILE") -gt $MAX_LOG_SIZE ]; then
    mv "$LOG_FILE" "${LOG_FILE}.old"
fi

# 日志函数
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "开始同步OpenClaw记忆..."

cd "$WORKSPACE_DIR"

# 检查git状态
if ! git status &>/dev/null; then
    log "错误：不是git仓库或git未初始化"
    exit 1
fi

# 添加所有更改
git add .

# 检查是否有更改
if git diff --cached --quiet; then
    log "没有更改需要提交"
    exit 0
fi

# 提交更改
COMMIT_MSG="记忆更新 $(date '+%Y-%m-%d %H:%M:%S')"
git commit -m "$COMMIT_MSG"

# 推送到远程仓库
if git push origin master; then
    log "同步成功: $COMMIT_MSG"
else
    log "推送失败，尝试拉取并合并..."
    git pull --rebase origin master
    git push origin master
    log "同步成功（经过合并）"
fi

log "同步完成"