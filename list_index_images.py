import re
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()
    for m in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', c):
        print(m.group(1))
