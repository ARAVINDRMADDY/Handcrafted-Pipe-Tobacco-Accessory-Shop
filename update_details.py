import re
import os

files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Headings font weight to 600 (font-semibold)
    # We will replace font-bold with font-semibold inside h1-h6 tags
    def repl_heading(m):
        return m.group(0).replace('font-bold', 'font-semibold')
    content = re.sub(r'<h[1-6][^>]*>.*?</h[1-6]>', repl_heading, content, flags=re.DOTALL)
    
    # 2. Update Paragraph font weight to 400-550 (font-normal or font-medium)
    # We will replace font-light (300) with font-medium (500) inside p tags
    def repl_p(m):
        return m.group(0).replace('font-light', 'font-medium').replace('text-gray-400', 'text-gray-500 dark:text-gray-400')
    content = re.sub(r'<p[^>]*>.*?</p>', repl_p, content, flags=re.DOTALL)
    
    # 3. Mobile subscribe form rounding fix (360px)
    # Search for the subscribe form container: flex flex-col sm:flex-row bg-white dark:bg-[#1E293B] rounded-full
    content = content.replace(
        'flex flex-col sm:flex-row bg-white dark:bg-[#1E293B] rounded-full p-2',
        'flex flex-col sm:flex-row bg-white dark:bg-[#1E293B] rounded-2xl sm:rounded-full p-2'
    )
    content = content.replace(
        'rounded-l-full',
        'rounded-t-xl sm:rounded-l-full sm:rounded-tr-none'
    )
    # The subscribe button has rounded-full. It should be rounded-b-xl sm:rounded-r-full sm:rounded-l-none
    content = content.replace(
        'rounded-full font-bold uppercase tracking-widest text-xs transition-colors whitespace-nowrap',
        'rounded-b-xl sm:rounded-r-full sm:rounded-l-none font-bold uppercase tracking-widest text-xs transition-colors whitespace-nowrap'
    )
    
    # 4. Footer email link break-all to fix 1024px crop issue
    content = content.replace(
        'href="mailto:contact@eliasthornepipes.com" class="text-base text-brand-muted hover:text-accent transition-colors font-medium"',
        'href="mailto:contact@eliasthornepipes.com" class="text-base text-brand-muted hover:text-accent transition-colors font-medium break-all"'
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated typography, subscribe form, and footer cropping.")
