#!/bin/bash
# 测试GitHub连接和推送

echo "测试GitHub连接..."
echo "仓库URL: https://github.com/9666pktst8-cell/Young.git"
echo ""

cd /root/.openclaw/workspace

# 测试网络连接
echo "1. 测试网络连接..."
if curl -s --head https://github.com | grep "200 OK" > /dev/null; then
    echo "✓ 可以访问GitHub"
else
    echo "✗ 无法访问GitHub"
fi

echo ""
echo "2. 检查git配置..."
git config --list | grep -E "(user|remote)"

echo ""
echo "3. 尝试推送..."
echo "注意：如果提示输入用户名密码，可以使用以下方式："
echo ""
echo "选项A: 使用SSH密钥（推荐）"
echo "   git remote set-url origin git@github.com:9666pktst8-cell/Young.git"
echo "   需要将SSH公钥添加到GitHub账户"
echo ""
echo "选项B: 使用个人访问令牌"
echo "   git remote set-url origin https://你的令牌@github.com/9666pktst8-cell/Young.git"
echo "   在GitHub设置中生成令牌"
echo ""
echo "选项C: 使用HTTPS+凭据缓存"
echo "   git config --global credential.helper store"
echo "   然后运行 git push，输入用户名和令牌"
echo ""
echo "现在尝试推送（可能需要认证）..."
git push -u origin master 2>&1 | head -20