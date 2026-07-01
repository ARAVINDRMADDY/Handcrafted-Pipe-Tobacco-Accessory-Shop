import re

for filename in ['services.html', 'tobacco-accessories.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace the centered background-image hero section with a two-column grid.
    # The hero section typically looks like:
    # <section class="relative min-h-[50vh] flex flex-col items-center justify-center overflow-hidden bg-[...]">
    #   <div class="absolute inset-0 z-0">
    #     <img src="..." alt="..." class="...">
    #     <div class="..."></div>
    #   </div>
    #   <div class="relative z-10 w-full max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center animate-fade-in pt-16">
    #     ... content ...
    #   </div>
    # </section>
    
    # Let's extract the image src, alt, and the content inside the relative z-10 text-center container.
    hero_pattern = re.compile(
        r'<section class="relative min-h-\[50vh\] flex flex-col items-center justify-center overflow-hidden.*?>\s*'
        r'<div class="absolute inset-0 z-0">\s*'
        r'<img src="([^"]+)" alt="([^"]+)" class="[^"]*">\s*'
        r'<div class="[^"]*"></div>\s*'
        r'</div>\s*'
        r'<div class="relative z-10 w-full max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center animate-fade-in pt-16">\s*'
        r'(.*?)\s*'
        r'</div>\s*'
        r'</section>',
        re.DOTALL
    )
    
    match = hero_pattern.search(content)
    if match:
        img_src = match.group(1)
        img_alt = match.group(2)
        inner_content = match.group(3)
        
        # We need to remove the centering from inner content.
        inner_content = inner_content.replace('justify-center', 'justify-start')
        inner_content = inner_content.replace('mx-auto', '')
        
        # Create a new balanced hero section (two columns)
        new_hero = f'''<section class="relative min-h-[50vh] flex items-center bg-brand-light dark:bg-brand-dark border-b border-gray-200 dark:border-white/5 pt-12 overflow-hidden">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
    <div class="grid lg:grid-cols-2 gap-12 items-center">
      <div class="animate-fade-in text-left">
        {inner_content}
      </div>
      <div class="relative hidden lg:block animate-fade-in" style="animation-delay: 0.2s;">
        <div class="absolute -inset-4 bg-accent/20 rounded-full blur-3xl z-0"></div>
        <img src="{img_src}" alt="{img_alt}" class="relative z-10 rounded-sm shadow-2xl w-full h-[500px] object-cover">
      </div>
    </div>
  </div>
</section>'''

        content = content[:match.start()] + new_hero + content[match.end():]
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated hero in {filename}")
