"""
Música de fundo com threading
"""
import threading
import time
from playsound import playsound
import os

class MusicThread:
    def __init__(self, music_path="assets/sounds"):
        self.music_path = music_path
        self.current_music = None
        self.playing = False
        self.thread = None
        self.loop = False
        
    def play_music(self, filename, loop=True):
        """Toca música de fundo"""
        self.stop_music()
        self.current_music = os.path.join(self.music_path, filename)
        self.loop = loop
        
        if os.path.exists(self.current_music):
            self.playing = True
            self.thread = threading.Thread(target=self._play_loop)
            self.thread.start()
            
    def _play_loop(self):
        """Loop interno para tocar música"""
        while self.playing:
            try:
                playsound(self.current_music)
                if not self.loop:
                    break
            except:
                break
                
    def stop_music(self):
        """Para a música"""
        self.playing = False
        if self.thread:
            self.thread.join()