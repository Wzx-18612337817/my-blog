import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 使用正则表达式修复音频标签问题
content = re.sub(r'(<audio[^>]*>.*?