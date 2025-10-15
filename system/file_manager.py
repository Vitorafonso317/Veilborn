"""
Leitura/escrita de arquivos com os, json, pickle
"""
import os
import json
import pickle

class FileManager:
    @staticmethod
    def save_json(data, filepath):
        """Salva dados em formato JSON"""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
    @staticmethod
    def load_json(filepath):
        """Carrega dados de arquivo JSON"""
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None
        
    @staticmethod
    def save_pickle(data, filepath):
        """Salva dados em formato pickle"""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'wb') as f:
            pickle.dump(data, f)
            
    @staticmethod
    def load_pickle(filepath):
        """Carrega dados de arquivo pickle"""
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                return pickle.load(f)
        return None