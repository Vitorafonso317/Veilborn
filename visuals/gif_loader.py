"""
Carregamento e animação de GIFs
"""
from PIL import Image, ImageTk
import os

class GifLoader:
    def __init__(self, assets_path="assets/images"):
        self.assets_path = assets_path
        self.loaded_gifs = {}
        
    def load_gif(self, filename, size=None):
        """Carrega um GIF e extrai todos os frames"""
        if filename in self.loaded_gifs:
            return self.loaded_gifs[filename]
            
        filepath = os.path.join(self.assets_path, filename)
        if os.path.exists(filepath):
            gif = Image.open(filepath)
            frames = []
            
            try:
                while True:
                    frame = gif.copy()
                    if size:
                        frame = frame.resize(size)
                    frames.append(ImageTk.PhotoImage(frame))
                    gif.seek(gif.tell() + 1)
            except EOFError:
                pass  # fim do GIF
                
            self.loaded_gifs[filename] = frames
            return frames
        return []

class AnimatedSprite:
    def __init__(self, canvas, gif_frames, x, y):
        self.canvas = canvas
        self.frames = gif_frames
        self.x = x
        self.y = y
        self.current_frame = 0
        self.sprite_id = None
        self.animation_speed = 100  # ms entre frames
        
    def start_animation(self):
        """Inicia a animação do GIF"""
        if self.frames:
            self.animate()
            
    def animate(self):
        """Atualiza o frame da animação"""
        if self.frames:
            if self.sprite_id:
                self.canvas.delete(self.sprite_id)
                
            self.sprite_id = self.canvas.create_image(
                self.x, self.y, anchor="nw", 
                image=self.frames[self.current_frame]
            )
            
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.canvas.after(self.animation_speed, self.animate)
            
    def move_to(self, x, y):
        """Move o sprite para nova posição"""
        self.x = x
        self.y = y