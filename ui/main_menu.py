"""
Menu inicial
"""
import tkinter as tk
from tkinter import ttk

class MainMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Seu Jogo")
        self.root.geometry("400x300")
        self.setup_ui()
        
    def setup_ui(self):
        title = tk.Label(self.root, text="SEU JOGO", font=("Arial", 24))
        title.pack(pady=50)
        
        btn_new_game = tk.Button(self.root, text="Novo Jogo", command=self.new_game)
        btn_new_game.pack(pady=10)
        
        btn_quit = tk.Button(self.root, text="Sair", command=self.root.quit)
        btn_quit.pack(pady=10)
        
    def new_game(self):
        from .game_ui import GameUI
        self.root.destroy()
        game_ui = GameUI()
        game_ui.run()
        
    def run(self):
        self.root.mainloop()