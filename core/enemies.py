"""
Dados e lógica dos inimigos
"""

class Enemy:
    def __init__(self, name, hp, min_damage, max_damage):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.min_damage = min_damage
        self.max_damage = max_damage
        
    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)
        
    def is_alive(self):
        return self.hp > 0

# Inimigos predefinidos
ENEMIES = {
    "goblin": Enemy("Goblin", 30, 5, 10),
    "orc": Enemy("Orc", 60, 8, 15),
    "dragon": Enemy("Dragon", 200, 20, 35)
}