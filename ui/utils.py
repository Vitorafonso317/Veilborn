"""
Funções auxiliares para a UI
"""
import tkinter as tk

def center_window(window, width, height):
    """Centraliza uma janela na tela"""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    window.geometry(f"{width}x{height}+{x}+{y}")

def create_button_style():
    """Cria um estilo padrão para botões"""
    return {
        "font": ("Arial", 12),
        "padx": 20,
        "pady": 10
    }