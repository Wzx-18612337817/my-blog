with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 修复第1052行（索引1051）
if len(lines) > 1051:
    # 替换错误的内容为正确的闭合标签
    lines[1051] = '   />