with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 修复第1052行的重复闭合标签问题
lines = content.split('\n')
if len(lines) > 1051:
    # 第1052行是索引1051
    if '/>