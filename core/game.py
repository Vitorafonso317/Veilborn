"""
Lógica principal do jogo
"""

class Game:
    def __init__(self):
        self.running = False
        
    def start(self):
        self.running = True
        
    def stop(self):
        self.running = False
        
    def update(self):
        pass