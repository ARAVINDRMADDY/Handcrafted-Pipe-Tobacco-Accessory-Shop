import os

files = [f for f in os.listdir('.') if f.endswith('.html')]

# We'll inject this SVG right before the text logo.
# It's a small, elegant smoking pipe icon.
svg_icon = '''<svg class="w-8 h-8 text-accent drop-shadow-sm" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
  <path d="M17.5,7C15.91,7 14.54,8.04 14.12,9.5H7.5C5.57,9.5 4,11.07 4,13C4,14.93 5.57,16.5 7.5,16.5H13V15.5H7.5C6.12,15.5 5,14.38 5,13C5,11.62 6.12,10.5 7.5,10.5H14.12C14.54,11.96 15.91,13 17.5,13C19.43,13 21,11.43 21,9.5C21,7.57 19.43,7 17.5,7ZM17.5,12C16.12,12 15,10.88 15,9.5C15,8.12 16.12,7 17.5,7C18.88,7 20,8.12 20,9.5C20,10.88 18.88,12 17.5,12Z"/>
  <path d="M19,3.5C18.7,3.5 18.5,3.7 18.5,4C18.5,4.7 18.2,5.2 17.7,5.5C17.3,5.8 16.7,6 16,6C15.7,6 15.5,6.2 15.5,6.5C15.5,6.8 15.7,7 16,7C17,7 17.8,6.7 18.4,6.2C19.1,5.7 19.5,4.9 19.5,4C19.5,3.7 19.3,3.5 19,3.5Z"/>
  <path d="M16,2.5C15.7,2.5 15.5,2.7 15.5,3C15.5,3.7 15.2,4.2 14.7,4.5C14.3,4.8 13.7,5 13,5C12.7,5 12.5,5.2 12.5,5.5C12.5,5.8 12.7,6 13,6C14,6 14.8,5.7 15.4,5.2C16.1,4.7 16.5,3.9 16.5,3C16.5,2.7 16.3,2.5 16,2.5Z"/>
</svg>'''

original_text = '<span class="text-2xl font-semibold tracking-tight text-brand-dark dark:text-brand-light uppercase">Pipe<span class="text-accent">Craft</span></span>'
new_logo = f'<div class="flex items-center gap-2">{svg_icon}{original_text}</div>'

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if we already wrapped it, to avoid double wrapping
    if '<div class="flex items-center gap-2"><svg' not in content:
        content = content.replace(original_text, new_logo)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Added side small image (pipe SVG) to the text logo.")
