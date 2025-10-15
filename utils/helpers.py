"""
Outras funções utilitárias (ex: validações)
"""
import re

def validate_player_name(name):
    """Valida o nome do jogador"""
    if not name or len(name.strip()) == 0:
        return False
    if len(name) > 20:
        return False
    if not re.match("^[a-zA-Z0-9_]+$", name):
        return False
    return True

def clamp(value, min_val, max_val):
    """Limita um valor entre min e max"""
    return max(min_val, min(max_val, value))

def calculate_experience_needed(level):
    """Calcula experiência necessária para o próximo nível"""
    return level * 100 + (level - 1) * 50

def format_time(seconds):
    """Formata tempo em segundos para MM:SS"""
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02d}:{seconds:02d}"