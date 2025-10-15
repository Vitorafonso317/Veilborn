"""
Sistema de batalha (random, cooldowns)
"""
import random
import time

class Combat:
    def __init__(self):
        self.last_attack = 0
        self.cooldown = 1.0
        
    def can_attack(self):
        return time.time() - self.last_attack >= self.cooldown
        
    def attack(self, attacker, target):
        if not self.can_attack():
            return False
            
        damage = random.randint(attacker.min_damage, attacker.max_damage)
        target.take_damage(damage)
        self.last_attack = time.time()
        return True