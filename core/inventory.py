"""
Sistema de inventário
"""

class Inventory:
    def __init__(self, max_slots=20):
        self.items = {}
        self.max_slots = max_slots
        
    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
            
    def remove_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] -= quantity
            if self.items[item] <= 0:
                del self.items[item]