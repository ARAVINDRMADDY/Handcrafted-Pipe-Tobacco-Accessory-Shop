import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

header_match = re.search(r'<nav.*?</nav>', c, re.DOTALL)
if header_match:
    print(header_match.group(0))
