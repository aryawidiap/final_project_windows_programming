import tkinter as tk
import time
import pygame as pg

class GenderBlade(tk.Button):
    __slot__ = ['is_pressed']
    def __init__(self, root, note, **kwargs):
        super().__init__(root, command=self.__press_button, **kwargs)
        self.is_pressed: bool = False
        self.note: int = note
    def button_pressed(self):
        self.is_pressed = True
    def button_released(self):
        self.is_pressed = False
    def __press_button(self):
        print(self.note)
        # pressed_button = self.gender_blades[pressed_key_numeric]
        # if pressed_button.is_pressed:
        #     return
        # pressed_button.config(relief='sunken')
        # pressed_button.button_pressed()
        # TODO: remove operations if sounds already exists
        self.play_sound(self.note)
    def play_sound(self):
        sound = pg.mixer.Sound(f"sounds/note_v_0-9_-0{self.note}.mp3")
        sound.play()
        return