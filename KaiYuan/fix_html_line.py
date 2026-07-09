with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 定义正确的闭合标签
slash = '/'
gt = '>'
closing_tag = '   ' + slash + gt

# 修复第1052行（索引1051）
if len(lines) > 1051:
    if 'parameter' in lines[1051]:
        lines[1051] = closing_tag + '\n'

# 写入修复后的内容
with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("修复完成！")