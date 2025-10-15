#!/usr/bin/env python3
"""
Arquivo principal que inicia o jogo
"""

if __name__ == "__main__":
    from ui.main_menu import MainMenu
    
    app = MainMenu()
    app.run()