import os

# The files that use the "WeaveNest" template colors
weavenest_files = ['artisans.html', 'collections.html', 'journal.html']

for filename in weavenest_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # We will only replace within the desktop actions block that we overwrote
        # to restore their specific color tokens.
        # But doing a global replace in these files for the tokens is also safe
        # because those tokens shouldn't exist in the file otherwise, 
        # except where we injected them.
        
        content = content.replace('bg-accent', 'bg-soft-gold')
        content = content.replace('text-accent', 'text-soft-gold')
        content = content.replace('border-accent', 'border-soft-gold')
        content = content.replace('hover:text-accent', 'hover:text-soft-gold')
        content = content.replace('hover:bg-accent', 'hover:bg-soft-gold')
        content = content.replace('hover:border-accent', 'hover:border-soft-gold')
        
        content = content.replace('bg-brand-dark', 'bg-charcoal')
        content = content.replace('text-brand-dark', 'text-charcoal')
        content = content.replace('dark:bg-brand-dark', 'dark:bg-charcoal')
        content = content.replace('dark:text-brand-dark', 'dark:text-charcoal')
        
        content = content.replace('bg-brand-light', 'bg-off-white')
        content = content.replace('text-brand-light', 'text-off-white')
        content = content.replace('dark:bg-brand-light', 'dark:bg-off-white')
        content = content.replace('dark:text-brand-light', 'dark:text-off-white')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Restored WeaveNest template colors.")
