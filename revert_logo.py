import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]
text_logo = '<span class="text-2xl font-semibold tracking-tight text-brand-dark dark:text-brand-light uppercase">Pipe<span class="text-accent">Craft</span></span>'

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use regex to catch all variations of the logo image
    content = re.sub(
        r'<img src="img/logo_new\.png"[^>]*>',
        text_logo,
        content
    )
    content = re.sub(
        r'<img src="img/logo_brand_1782900422178\.png"[^>]*>',
        text_logo,
        content
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Reverted all image logos to text logos.")
