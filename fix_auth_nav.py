import os

for filename in ['login.html', 'register.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # The issue is that the flex container lost its first child (the logo)
    # so justify-between causes the single remaining child (toggles) to float left.
    # Changing justify-between to justify-end forces the toggles to the right.
    content = content.replace(
        '<div class="flex justify-between items-center h-[90px]">',
        '<div class="flex justify-end items-center h-[90px]">'
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed flex alignment in login and register pages.")
