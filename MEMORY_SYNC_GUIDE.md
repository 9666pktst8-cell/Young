# OpenClaw记忆同步配置指南

## 方案概述
使用Git进行记忆同步，支持版本控制、冲突解决和跨设备访问。

## 步骤1：创建远程仓库

### GitHub（推荐）
1. 访问 https://github.com/new
2. 仓库名称：例如 `openclaw-memory`
3. 描述：OpenClaw记忆同步仓库
4. 选择公开或私有（建议私有）
5. 点击创建

### GitLab
1. 访问 https://gitlab.com/projects/new
2. 类似步骤

### Gitee（国内访问快）
1. 访问 https://gitee.com/projects/new
2. 类似步骤

## 步骤2：配置本地仓库

```bash
# 进入工作区目录
cd /root/.openclaw/workspace

# 添加远程仓库（替换为你的仓库URL）
git remote add origin https://github.com/你的用户名/openclaw-memory.git

# 首次提交和推送
git add .
git commit -m "初始化OpenClaw记忆同步"
git push -u origin master
```

## 步骤3：设置自动同步

```bash
# 运行自动同步设置脚本
/root/.openclaw/workspace/setup-cron.sh
```

这会设置每小时自动同步一次。

## 步骤4：测试同步

```bash
# 手动运行同步脚本测试
/root/.openclaw/workspace/sync-memory.sh

# 查看同步日志
tail -f /root/.openclaw/sync.log
```

## 手动同步命令

```bash
# 手动同步
cd /root/.openclaw/workspace
git add .
git commit -m "手动同步 $(date '+%Y-%m-%d %H:%M:%S')"
git push origin master

# 从其他设备拉取更新
git pull origin master
```

## 同步内容
- `memory/` - 所有记忆文件
- `MEMORY.md` - 长期记忆
- `AGENTS.md` - 代理配置
- `SOUL.md` - 个性配置
- `USER.md` - 用户信息
- `TOOLS.md` - 工具配置
- `skills/` - 技能目录

## 注意事项

### 1. 敏感信息
- 检查 `memory/` 目录中是否有敏感信息
- 建议使用私有仓库
- 可以在 `.gitignore` 中添加忽略规则

### 2. 冲突处理
如果多个设备同时修改：
```bash
# 拉取最新更改
git pull origin master

# 如果有冲突，手动解决
# 然后提交
git add .
git commit -m "解决合并冲突"
git push origin master
```

### 3. 备份
定期检查同步状态：
```bash
# 查看同步日志
cat /root/.openclaw/sync.log

# 检查git状态
cd /root/.openclaw/workspace
git status
git log --oneline -5
```

## 恢复记忆
在新设备上恢复记忆：
```bash
# 克隆仓库
git clone https://github.com/你的用户名/openclaw-memory.git /root/.openclaw/workspace

# 或者如果已有目录
cd /root/.openclaw/workspace
git pull origin master
```

## 故障排除

### 问题：推送被拒绝
```bash
# 先拉取最新更改
git pull --rebase origin master
git push origin master
```

### 问题：认证失败
```bash
# 使用SSH方式（推荐）
git remote set-url origin git@github.com:你的用户名/openclaw-memory.git

# 或者使用个人访问令牌
git remote set-url origin https://你的令牌@github.com/你的用户名/openclaw-memory.git
```

### 问题：文件权限
```bash
chmod +x /root/.openclaw/workspace/sync-memory.sh
chmod +x /root/.openclaw/workspace/setup-cron.sh
```

## 高级配置

### 更频繁的同步
编辑cron任务：
```bash
# 每30分钟同步一次
*/30 * * * * /root/.openclaw/workspace/sync-memory.sh

# 每5分钟同步一次（谨慎使用）
*/5 * * * * /root/.openclaw/workspace/sync-memory.sh
```

### 同步通知
可以在同步脚本中添加通知功能，如发送邮件或消息。

---

**配置完成后，你的OpenClaw记忆将每小时自动同步到云端，支持跨设备访问和版本控制。**