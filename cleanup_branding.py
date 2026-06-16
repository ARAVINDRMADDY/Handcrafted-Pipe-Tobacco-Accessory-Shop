import os
import glob

replacements = {
    'ProDetail Mobile Auto Detailing': 'Handcrafted Pipe & Tobacco Accessory Shop',
    'ProDetail Mobile Auto Care': 'Handcrafted Pipe & Tobacco Shop',
    'ProDetail - Redefine Your Ride': 'Elias Thorne - Master Pipe Crafter',
    'ProDetail - Mobile Auto Detailing & Ceramic Coating Service': 'Elias Thorne - Handcrafted Pipes & Tobacco',
    'info@prodetail.com': 'contact@eliasthornepipes.com',
    'ProDetail': 'Elias Thorne Pipes',
    'Mobile Detailing Map Placeholder': 'Workshop Location Map',
    'We are a fully mobile detailing service, meaning our equipped vans bring the showroom shine directly to your driveway or workplace.': 'Our master craftsmen operate from our dedicated atelier. While our primary focus is handcrafting bespoke pipes, our workshop is open by appointment for custom consultations.',
    'Get in touch with ProDetail to book your premium mobile detailing service or ask any questions about our packages.': 'Get in touch to commission a custom handcrafted pipe or inquire about our premium tobacco blends.',
    'Read the latest auto detailing tips, ceramic coating guides, and car care advice from the experts': 'Read the latest pipe smoking tips, tobacco blending guides, and briar care advice from our master craftsmen',
    'empowering vehicles through bespoke detailing and ceramic coating': 'crafting world-class smoking pipes from premium Mediterranean briar',
    # Replace the image source of the map placeholder in contact.html specifically
    'src="https://images.unsplash.com/photo-1582210850021-3965b05c5fc5?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" \n                alt="Mobile Detailing Map Placeholder"': 'src="img/home2_workshop.png" \n                alt="Workshop Location Map"'
}

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Specific map image fix for contact.html
    if 'contact.html' in filepath:
        content = content.replace('src="https://images.unsplash.com/photo-1582210850021-3965b05c5fc5?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"\n                alt="Mobile Detailing Map Placeholder"', 'src="img/home2_workshop.png" alt="Workshop Location Map"')
        content = content.replace('src="https://images.unsplash.com/photo-1582210850021-3965b05c5fc5?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" \n                alt="Workshop Location Map"', 'src="img/home2_workshop.png" \n                alt="Workshop Location Map"')
        # simpler replace
        content = content.replace('https://images.unsplash.com/photo-1582210850021-3965b05c5fc5?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" \n                alt="Workshop Location Map"', 'img/home2_workshop.png" \n                alt="Workshop Location Map"')

    for old, new in replacements.items():
        content = content.replace(old, new)
        
    # Also clean up the map placeholder if it wasn't caught
    content = content.replace('alt="Mobile Detailing Map Placeholder"', 'alt="Workshop Location Map"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
