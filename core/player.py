"""
Classe do jogador
"""
from .inventory import Inventory

class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.level = 1
        self.hp = 100
        self.max_hp = 100
        self.mp = 50
        self.max_mp = 50
        self.experience = 0
        self.min_damage = 10
        self.max_damage = 15
        self.inventory = Inventory()
        
    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)
        
    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)