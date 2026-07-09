f = open('index.html', 'r', encoding='utf-8')
content = f.read()
f.close()

# 找到并修复错误的行
lines = content.split('\n')
if len(lines) > 1051:
    # 第1052行是索引1051
    line = lines[1051]
    # 如果这行包含错误的内容，修复它
    if 'parameter' in line:
        lines[1051] = '   />