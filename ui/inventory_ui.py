"""
Tela de inventário
"""
import tkinter as tk
from tkinter import ttk

class InventoryUI:
    def __init__(self, parent, inventory):
        self.parent = parent
        self.inventory = inventory
        self.window = tk.Toplevel(parent)
        self.window.title("Inventário")
        self.window.geometry("400x300")
        self.setup_ui()
        
    def setup_ui(self):
        # Lista de itens
        self.item_listbox = tk.Listbox(self.window)
        self.item_listbox.pack(expand=True, fill="both", padx=10, pady=10)
        
        self.update_inventory()
        
    def update_inventory(self):
        self.item_listbox.delete(0, tk.END)
        for item, quantity in self.inventory.items.items():
            self.item_listbox.insert(tk.END, f"{item} x{quantity}")