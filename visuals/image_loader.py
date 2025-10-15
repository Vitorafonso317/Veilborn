"""
Carregamento de imagens com PIL
"""
from PIL import Image, ImageTk
import os

class ImageLoader:
    def __init__(self, assets_path="assets/images"):
        self.assets_path = assets_path
        self.loaded_images = {}
        
    def load_image(self, filename, size=None):
        """Carrega uma imagem e opcionalmente redimensiona"""
        if filename in self.loaded_images:
            return self.loaded_images[filename]
            
        filepath = os.path.join(self.assets_path, filename)
        if os.path.exists(filepath):
            image = Image.open(filepath)
            if size:
                image = image.resize(size)
            photo = ImageTk.PhotoImage(image)
            self.loaded_images[filename] = photo
            return photo
        return None