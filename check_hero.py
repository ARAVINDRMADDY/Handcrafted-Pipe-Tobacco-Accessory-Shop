import re

with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'<section class="relative min-h-\[50vh\].*?</section>', content, re.DOTALL)
if m:
    print(m.group(0))
else:
    print('Hero section not found')
