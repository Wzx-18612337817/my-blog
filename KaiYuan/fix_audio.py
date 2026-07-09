with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 修复第1052行（索引1051）的错误内容
if len(lines) > 1051:
    lines[1051] = '   />