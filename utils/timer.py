"""
Funções com time (delays, cooldowns)
"""
import time

class Timer:
    def __init__(self):
        self.start_time = time.time()
        
    def reset(self):
        """Reinicia o timer"""
        self.start_time = time.time()
        
    def elapsed(self):
        """Retorna o tempo decorrido em segundos"""
        return time.time() - self.start_time
        
    def has_passed(self, seconds):
        """Verifica se o tempo especificado já passou"""
        return self.elapsed() >= seconds

class Cooldown:
    def __init__(self, duration):
        self.duration = duration
        self.last_used = 0
        
    def can_use(self):
        """Verifica se o cooldown já passou"""
        return time.time() - self.last_used >= self.duration
        
    def use(self):
        """Marca o cooldown como usado"""
        if self.can_use():
            self.last_used = time.time()
            return True
        return False