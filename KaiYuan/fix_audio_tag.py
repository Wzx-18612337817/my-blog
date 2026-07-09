with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 将错误的内容替换为正确的音频标签闭合
content = content.replace(' />