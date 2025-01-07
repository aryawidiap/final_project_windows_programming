from functools import partial
import tkinter as tk
import pygame as pg

class GenderBlade(tk.Button):
    __slot__ = ['is_pressed']
    def __init__(self, root, note, **kwargs):
        super().__init__(root, command=self.__press_button, background='#f2e6be', **kwargs)
        self.is_pressed: bool = False
        self.note: int = note
        pg.init()
        self.sound = pg.mixer.Sound(f"sounds/note_v_0-9_-0{self.note}.mp3")
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
        self.play_sound()
    def bind_command(self, func, **kwargs):
        self.configure(command=partial(self.__bind_command, func, **kwargs))
    def __bind_command(self, func, **kwargs):
        func(**kwargs)
        self.__press_button()
    def play_sound(self):
        self.sound.play()
        # print(f"Channel number {self.sound.get_num_channels()}")
        return