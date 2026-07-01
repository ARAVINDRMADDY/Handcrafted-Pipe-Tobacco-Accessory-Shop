import os, re, collections

imgs = collections.defaultdict(list)
for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            for m in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', content):
                imgs[m.group(1)].append(f)
                
for k, v in sorted(imgs.items(), key=lambda x: len(x[1]), reverse=True):
    if len(v) > 1:
        print(f"{k}: {len(v)} times in {set(v)}")
