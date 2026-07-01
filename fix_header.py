import re
import os

files = [f for f in os.listdir('.') if f.endswith('.html')]

# We want the desktop action buttons to be exactly this order:
# Login, Register, RTL toggle, Theme toggle
desktop_actions_html = '''
        <div class="hidden xl:flex items-center gap-4">
          <button type="button" onclick="window.location.href='login.html'" class="bg-accent border-2 border-accent text-white hover:bg-brand-dark dark:hover:bg-gray-700 px-6 py-2.5 text-xs uppercase tracking-wider font-semibold transition-all duration-300 flex items-center gap-2">
            <span>Login</span>
            <i class="fas fa-arrow-right text-[10px] rtl:rotate-180"></i>
          </button>
          
          <a href="register.html" class="bg-transparent border-2 border-gray-300 dark:border-gray-700 text-brand-dark dark:text-brand-light hover:border-accent dark:hover:border-accent hover:text-accent dark:hover:text-accent px-6 py-2.5 text-xs uppercase tracking-wider font-medium transition-all duration-300 flex items-center gap-2">
            <span>Register</span>
            <i class="fas fa-arrow-right text-[10px] rtl:rotate-180"></i>
          </a>

          <button id="rtl-toggle" class="text-xs font-medium text-gray-500 dark:text-gray-400 hover:text-accent transition-colors duration-300 ms-2" title="Toggle RTL">
            LTR
          </button>

          <button id="theme-toggle" class="relative w-[72px] h-[34px] flex items-center bg-gray-200 dark:bg-[#1E293B] rounded-full p-1 transition-colors duration-300 focus:outline-none border border-gray-300 dark:border-gray-700 overflow-hidden" title="Toggle Theme">
            <span class="text-[9px] font-medium text-gray-500 absolute end-2.5 dark:opacity-0 transition-opacity duration-300 tracking-wider">LIGHT</span>
            <span class="text-[9px] font-medium text-accent absolute start-2.5 opacity-0 dark:opacity-100 transition-opacity duration-300 tracking-wider">DARK</span>
            
            <div class="w-[24px] h-[24px] bg-white dark:bg-brand-dark border border-gray-200 dark:border-gray-600 rounded-full shadow-sm transform transition-transform duration-300 flex items-center justify-center rtl:dark:-translate-x-[38px] ltr:dark:translate-x-[38px] dark:translate-x-[38px] z-10">
              <i class="fas fa-sun text-[11px] text-accent dark:hidden block"></i>
              <i class="fas fa-moon text-[11px] text-accent hidden dark:block"></i>
            </div>
          </button>
        </div>
'''

blog_link_html = '''
            <a href="blog.html" class="relative group text-xs uppercase tracking-[0.15em] font-medium text-gray-900 dark:text-gray-100 hover:text-accent transition-colors py-2">
              Blog
              <span class="absolute bottom-0 start-0 w-0 h-[2px] bg-accent transition-all duration-300 group-hover:w-full"></span>
            </a>
            '''

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Standardize desktop action buttons
    # We will replace the entire <div class="hidden xl:flex items-center...</div>
    # up to the <div class="xl:hidden flex items-center">
    action_pattern = re.compile(r'<div class="hidden xl:flex items-center[^>]*>.*?</div>\s*<div class="xl:hidden flex items-center">', re.DOTALL)
    
    # ensure it only replaces if it matches
    if action_pattern.search(content):
        content = action_pattern.sub(desktop_actions_html.strip() + '\n\n        <div class="xl:hidden flex items-center">', content)
    
    # 2. Ensure Blog is before Contact
    # Find the contact link block
    contact_pattern = re.compile(r'<a href="contact\.html"[^>]*>\s*Contact\s*<span[^>]*></span>\s*</a>', re.DOTALL)
    match = contact_pattern.search(content)
    if match:
        contact_str = match.group(0)
        # Check if Blog is already right before it, or exists
        if 'href="blog.html"' not in content[:match.start()][-500:]:
            # Insert blog link before contact
            content = content[:match.start()] + blog_link_html + '\n            ' + content[match.start():]

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Header standardized.")
