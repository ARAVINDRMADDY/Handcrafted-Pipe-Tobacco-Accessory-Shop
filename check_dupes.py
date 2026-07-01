from collections import Counter
import re

with open('home-2.html', 'r', encoding='utf-8') as f:
    content = f.read()

images = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
counts = Counter(images)

duplicates = False
for img, count in counts.items():
    if count > 1:
        print(f'Duplicate found: {img} ({count} times)')
        duplicates = True

if not duplicates:
    print('No duplicates found in home-2.html')
