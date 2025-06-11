import os
from rembg import remove
from PIL import Image

# Extensions d'images supportées
image_extensions = ['.jpg', '.jpeg', '.png', 'jfif', '.bmp', '.tiff', '.webp']
images = [f for f in os.listdir('.') if os.path.isfile(f) and any(f.lower().endswith(ext) for ext in image_extensions)]

print(f"🔍 {len(images)} image(s) trouvée(s)")

for image in images:
    try:
        input_path = image
        output_path = f'{os.path.splitext(image)[0]}_no_bg.png'
        
        input_image = Image.open(input_path)
        output = remove(input_image)
        output.save(output_path)
        
        print(f"✅ {image} → {output_path}")
        
    except Exception as e:
        print(f"❌ Erreur avec {image}: {e}")

print("🎉 Traitement terminé !")