import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]

# We'll use these generated images to de-duplicate
generated_images = [
    "img/pipe_1_1782900347403.png",
    "img/pipe_2_1782900357954.png",
    "img/pipe_3_1782900368281.png",
    "img/craft_1_1782900381474.png",
    "img/craft_2_1782900391780.png"
]
unsplash_urls = [
    "https://images.unsplash.com/photo-1596700755913-9092490df111?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "https://images.unsplash.com/photo-1540955931751-24835eebccfb?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "https://images.unsplash.com/photo-1590845947698-8924d7409b56?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "https://images.unsplash.com/photo-1517488629431-6427e0ee1e5f?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "https://images.unsplash.com/photo-1588674990920-c75c802422b4?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "https://images.unsplash.com/photo-1516962080544-eac695c93791?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
]
all_replacements = generated_images + unsplash_urls
replacement_idx = 0

def get_next_img():
    global replacement_idx
    img = all_replacements[replacement_idx % len(all_replacements)]
    replacement_idx += 1
    return img

logo_html = '<img src="img/logo_brand_1782900422178.png" alt="PipeCraft Logo" class="h-[40px] w-auto drop-shadow-md">'

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace Text Logo with Image Logo
    # The text logo is: <span class="text-2xl font-semibold tracking-tight text-brand-dark dark:text-brand-light uppercase">Pipe<span class="text-accent">Craft</span></span>
    # Or variations
    content = re.sub(
        r'<span class="text-2xl[^>]*>Pipe<span class="text-accent">Craft</span></span>',
        logo_html,
        content
    )

    # 2. Header Reorder (Login/Register buttons next to LTR/Theme toggles)
    # The buttons are in a div with "hidden xl:flex items-center gap-4"
    # It looks like:
    # <button type="button" onclick="window.location.href='login.html'" ...>...</button>
    # <a href="register.html" ...>...</a>
    # <div class="h-8 w-px bg-gray-200 dark:bg-gray-800 mx-2"></div>
    # <button id="theme-toggle" ...>...</button>
    # <button id="rtl-toggle" ...>...</button>
    
    # We want to place Login/Register AFTER the toggles.
    # Let's find the whole block.
    header_pattern = re.compile(
        r'(<button type="button" onclick="window\.location\.href=\'login\.html\'"[^>]*>.*?</button>\s*<a href="register\.html"[^>]*>.*?</a>\s*<div class="h-8 w-px bg-gray-200 dark:bg-gray-800 mx-2"></div>\s*)(<button id="theme-toggle".*?</button>\s*<button id="rtl-toggle".*?</button>)',
        re.DOTALL
    )
    content = header_pattern.sub(r'\2\n          <div class="h-8 w-px bg-gray-200 dark:bg-gray-800 mx-2"></div>\n          \1', content)
    # Remove the extra divider that moved with \1
    content = re.sub(r'<div class="h-8 w-px bg-gray-200 dark:bg-gray-800 mx-2"></div>\s*</div>', '</div>', content)

    # De-duplicate images inside each file.
    # For a file, we find all img tags. If an img src appears more than once, replace the 2nd, 3rd, etc. with get_next_img()
    seen_imgs = set()
    
    def repl_img(m):
        src = m.group(1)
        if src in seen_imgs:
            new_src = get_next_img()
            return m.group(0).replace(src, new_src)
        else:
            seen_imgs.add(src)
            return m.group(0)

    content = re.sub(r'<img[^>]+src=["\']([^"\']+)["\']', repl_img, content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied global HTML updates.")
