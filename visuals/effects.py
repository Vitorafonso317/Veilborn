"""
Aplicação de efeitos (blur, sombras)
"""
from PIL import Image, ImageFilter

def apply_blur(image, radius=2):
    """Aplica efeito de blur na imagem"""
    return image.filter(ImageFilter.GaussianBlur(radius=radius))

def apply_shadow(image, offset=(5, 5), blur_radius=3):
    """Aplica efeito de sombra na imagem"""
    shadow = Image.new('RGBA', 
                      (image.width + offset[0], image.height + offset[1]), 
                      (0, 0, 0, 0))
    
    # Criar sombra
    shadow_img = Image.new('RGBA', image.size, (0, 0, 0, 128))
    shadow_img = shadow_img.filter(ImageFilter.GaussianBlur(radius=blur_radius))
    
    # Combinar imagens
    shadow.paste(shadow_img, offset)
    shadow.paste(image, (0, 0), image)
    
    return shadow