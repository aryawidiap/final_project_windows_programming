import pygame as pg
from time import sleep
class GenderInstrument():
    def __init__(self):
        # self.note_ranges = [7,8,9,-1,-1,8,7,-1,-1,-1,8,8,7,8,9,-1,-1,-1]
        self.note_ranges = [7,8,9,7,8,9,7,8,9,7,8,9,0,9,8,-1,9,-1,8,-1,-1,9,-1,0,0,6,7,8,7,8,-1,-1,-1]
        # self.note_ranges = [7, 8, 9, -1, -1, -1, -1, 8, 7, -1, -1, -1, -1, -1, -1, -1, 8, 8, 7, 8, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 8, 8, 7, 8, 9, -1, -1]
        
        pg.init()
        pg.mixer.set_num_channels(256)
        # // tempo about 176 bpm
 
        
    def __play_sound(self, key):
        print(key)
        if key != -1:
            sound = pg.mixer.Sound(f"sounds/note_v_0-9_-0{key}.mp3")
            sound.play()
        # return
    
    def playback(self):
        for note in self.note_ranges:
            self.__play_sound(note)
            sleep(0.5)

gender = GenderInstrument()
gender.playback()
