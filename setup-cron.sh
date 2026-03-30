#!/bin/bash
# 设置OpenClaw记忆自动同步cron任务

CRON_JOB="0 * * * * /root/.openclaw/workspace/sync-memory.sh"
CRON_FILE="/etc/cron.d/openclaw-sync"

echo "设置OpenClaw记忆自动同步..."
echo "将创建cron任务：每小时同步一次"

# 创建cron文件
echo "# OpenClaw记忆自动同步 - 每小时一次" > "$CRON_FILE"
echo "$CRON_JOB" >> "$CRON_FILE"
echo "" >> "$CRON_FILE"

# 设置权限
chmod 644 "$CRON_FILE"

echo "Cron任务已创建：$CRON_FILE"
echo "内容："
cat "$CRON_FILE"

echo ""
echo "注意：你需要先完成以下步骤："
echo "1. 在GitHub/GitLab/Gitee创建远程仓库"
echo "2. 运行以下命令添加远程仓库："
echo "   cd /root/.openclaw/workspace"
echo "   git remote add origin <你的仓库URL>"
echo "3. 首次提交："
echo "   git add ."
echo "   git commit -m '初始化记忆同步'"
echo "   git push -u origin master"
echo ""
echo "之后系统会自动每小时同步一次。"