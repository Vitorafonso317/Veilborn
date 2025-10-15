"""
Tela principal do jogo (batalha, HUD)
"""
import tkinter as tk
from core.player import Player
from core.game import Game
from core.collision import CollisionManager
from visuals.image_loader import ImageLoader
from visuals.gif_loader import GifLoader, AnimatedSprite

class GameUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Jogo - Batalha")
        self.root.geometry("1200x600")
        self.player = Player()
        self.game = Game()
        self.collision_manager = CollisionManager()
        self.collision_manager.load_scenario("forest")  # mude aqui: default, forest, castle, beach, mountain
        self.image_loader = ImageLoader()
        self.gif_loader = GifLoader()
        self.player_sprite = None
        self.player_x = -200  # começa fora da tela
        # Posicionar jogador exatamente no chão
        ground_height = self.collision_manager.get_ground_height()
        self.player_y = ground_height - 400 + 10  # ajuste para sprite dobrado
        
        # Configurações de movimento
        self.walking_speed = 8  # velocidade de corrida
        self.walking_direction = 1  # 1 = direita, -1 = esquerda
        self.is_walking = True  # controla se está andando
        self.setup_ui()
        
    def setup_ui(self):
        # Canvas para o jogo
        self.canvas = tk.Canvas(self.root, width=1200, height=600, bg="lightblue")
        self.canvas.pack()
        
        # Carregar imagem de fundo
        self.bg_image = self.image_loader.load_image("backgorund.png", (1200, 600))
        if self.bg_image:
            self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)
        
        # Carregar GIF do jogador (coloque player.gif na pasta assets/images)
        player_frames = self.gif_loader.load_gif("player.gif", (400, 400))
        if player_frames:
            self.player_sprite = AnimatedSprite(self.canvas, player_frames, self.player_x, self.player_y)
            self.player_sprite.animation_speed = 50  # GIF mais rápido (era 100ms)
            self.player_sprite.start_animation()
            self.start_walking()
        else:
            # Fallback: retângulo se não houver GIF
            self.player_rect = self.canvas.create_rectangle(
                self.player_x, self.player_y, self.player_x + 30, self.player_y + 50, 
                fill="red", outline="black"
            )
            self.start_walking()
        
        # HUD
        self.hp_label = tk.Label(self.root, text=f"HP: {self.player.hp}/{self.player.max_hp}")
        self.hp_label.pack()
        
        # Controles
        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.focus_set()
        
        # Botões
        btn_frame = tk.Frame(self.root)
        btn_frame.pack()
        
        btn_attack = tk.Button(btn_frame, text="Atacar")
        btn_attack.pack(side="left", padx=10)
        
        btn_inventory = tk.Button(btn_frame, text="Inventário")
        btn_inventory.pack(side="left", padx=10)
        
    def on_key_press(self, event):
        """Controla movimento do jogador"""
        new_x, new_y = self.player_x, self.player_y
        
        if event.keysym == "Left":
            new_x -= 10
        elif event.keysym == "Right":
            new_x += 10
        elif event.keysym == "Up":
            new_y -= 10
        elif event.keysym == "Down":
            new_y += 10
            
        # Atualizar posição
        self.player_x, self.player_y = new_x, new_y
        
        if self.player_sprite:
            self.player_sprite.move_to(self.player_x, self.player_y)
        else:
            self.canvas.coords(self.player_rect, 
                             self.player_x, self.player_y, 
                             self.player_x + 30, self.player_y + 50)
    
    def start_walking(self):
        """Inicia o movimento automático do personagem"""
        self.walk_animation()
        
    def walk_animation(self):
        """Animação de caminhada automática"""
        if not self.is_walking:
            return
            
        # Mover personagem
        self.player_x += self.walking_speed * self.walking_direction
        
        # Parar quando sair completamente da tela à direita
        if self.player_x >= 1400:  # completamente fora da tela
            self.is_walking = False
            return
            
        # Atualizar posição visual
        if self.player_sprite:
            self.player_sprite.move_to(self.player_x, self.player_y)
        else:
            self.canvas.coords(self.player_rect, 
                             self.player_x, self.player_y, 
                             self.player_x + 30, self.player_y + 50)
        
        # Continuar animação
        self.root.after(50, self.walk_animation)  # 50ms = movimento suave
    
    def run(self):
        self.root.mainloop()