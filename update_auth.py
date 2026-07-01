import re
import os

auth_files = ['login.html', 'register.html']

for filename in auth_files:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove logo from header
    content = re.sub(
        r'<div class="flex-shrink-0">\s*<a href="index\.html"[^>]*>\s*<div class="flex flex-col">\s*<img[^>]*logo_brand[^>]*>\s*</div>\s*</a>\s*</div>',
        '',
        content
    )
    
    # Place logo at the center of the form (before "Welcome Back" / "Create Account")
    # Finding the text-center div inside the form container
    # <div class="text-center mb-6">
    logo_html = '''<div class="flex justify-center mb-6">
          <a href="index.html">
            <img src="img/logo_brand_1782900422178.png" alt="PipeCraft Logo" class="h-[50px] w-auto drop-shadow-md">
          </a>
        </div>
        <div class="text-center mb-6">'''
    content = content.replace('<div class="text-center mb-6">', logo_html)
    
    # CTA button hover color green -> primary/secondary theme color
    # hover:bg-[#059669]
    content = content.replace('hover:bg-[#059669]', 'hover:bg-brand-dark dark:hover:bg-gray-700')
    
    # Top padding issue in login/signup page. The container has `p-4 pt-[90px]`.
    # Let's adjust it to `p-4 mt-[90px] mb-8` and remove h-screen overflow-hidden to allow scrolling, or adjust padding.
    # The user says "in top has a padding issue need to align it properly."
    # The body has `h-screen overflow-hidden flex flex-col`. This makes it unscrollable, maybe that's the issue?
    # Actually, the user's screenshot for the padding issue might show the form overlapping the header or cut off.
    # Let's change `pt-[90px]` to just `pt-28`.
    content = content.replace('pt-[90px]', 'pt-28')
    content = content.replace('h-screen overflow-hidden', 'min-h-screen overflow-x-hidden')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Auth pages updated.")
