with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 将第1052行的错误内容替换为正确的
lines = content.split('\n')
if len(lines) > 1051:
    # 检查是否需要修复
    if 'parameter' in lines[1051]:
        # 替换为正确的内容
        lines[1051] = '   />