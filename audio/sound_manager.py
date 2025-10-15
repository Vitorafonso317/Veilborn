"""
Toca efeitos sonoros com playsound
"""
from playsound import playsound
import os
import threading

class SoundManager:
    def __init__(self, sounds_path="assets/sounds"):
        self.sounds_path = sounds_path
        self.volume = 1.0
        
    def play_sound(self, filename, async_play=True):
        """Toca um efeito sonoro"""
        filepath = os.path.join(self.sounds_path, filename)
        if os.path.exists(filepath):
            if async_play:
                threading.Thread(target=playsound, args=(filepath,)).start()
            else:
                playsound(filepath)
                
    def set_volume(self, volume):
        """Define o volume (0.0 a 1.0)"""
        self.volume = max(0.0, min(1.0, volume))