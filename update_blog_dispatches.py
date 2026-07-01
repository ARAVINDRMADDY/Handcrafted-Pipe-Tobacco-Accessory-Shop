import os

with open('blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the images in the Recent Dispatches section
content = content.replace('img/home2_woods.png', 'img/blog_sandblast.png')
content = content.replace('img/house_blends.png', 'img/blog_cellar.png')
content = content.replace('img/about_anatomy.png', 'img/blog_slowsmoke.png')

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced Recent Dispatches images in blog.html")
