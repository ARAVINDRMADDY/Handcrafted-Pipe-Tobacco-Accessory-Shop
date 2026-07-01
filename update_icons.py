import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace fa-leaf with a tobacco leaf SVG
leaf_svg = '<svg xmlns="http://www.w3.org/2000/svg" class="w-12 h-12 text-brand-muted group-hover:text-accent transition-colors" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg>'
content = re.sub(r'<i class="fas fa-leaf text-3xl[^>]*></i>', leaf_svg, content)

# Replace fa-mug-hot with an aromatic steam SVG
steam_svg = '<svg xmlns="http://www.w3.org/2000/svg" class="w-12 h-12 text-brand-muted group-hover:text-accent transition-colors" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="7.5 4.21 12 6.81 16.5 4.21"/><polyline points="7.5 19.79 7.5 14.6 3 12"/><polyline points="21 12 16.5 14.6 16.5 19.79"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>'
content = re.sub(r'<i class="fas fa-mug-hot text-3xl[^>]*></i>', steam_svg, content)

# Replace fa-pepper-hot with spice SVG
spice_svg = '<svg xmlns="http://www.w3.org/2000/svg" class="w-12 h-12 text-brand-muted group-hover:text-accent transition-colors" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 11v8a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1v-7a1 1 0 0 1 1-1h3a4 4 0 0 0 4-4V4a2 2 0 1 1 4 0v5h3a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-3l-1.5-4.5"/><path d="M12 16v5"/></svg>'
content = re.sub(r'<i class="fas fa-pepper-hot text-3xl[^>]*></i>', spice_svg, content)

# Replace fa-seedling with cocoa/bean SVG
bean_svg = '<svg xmlns="http://www.w3.org/2000/svg" class="w-12 h-12 text-brand-muted group-hover:text-accent transition-colors" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M16 8s-3-2-6 2-2 6-2 6"/></svg>'
content = re.sub(r'<i class="fas fa-seedling text-3xl[^>]*></i>', bean_svg, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Icons replaced in index.html")
