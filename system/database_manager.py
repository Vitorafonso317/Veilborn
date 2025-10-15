"""
Acesso ao banco SQLite
"""
import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_path="data/database.db"):
        self.db_path = db_path
        self.init_database()
        
    def init_database(self):
        """Inicializa o banco de dados"""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Tabela de ranking
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS ranking (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    player_name TEXT NOT NULL,
                    score INTEGER NOT NULL,
                    level INTEGER NOT NULL,
                    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            conn.commit()
            
    def add_score(self, player_name, score, level):
        """Adiciona pontuação ao ranking"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO ranking (player_name, score, level) VALUES (?, ?, ?)",
                (player_name, score, level)
            )
            conn.commit()
            
    def get_top_scores(self, limit=10):
        """Obtém as melhores pontuações"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT player_name, score, level FROM ranking ORDER BY score DESC LIMIT ?",
                (limit,)
            )
            return cursor.fetchall()