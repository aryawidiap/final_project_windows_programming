import tkinter as tk
import time

class GenderBlade(tk.Button):
    __slot__ = ['is_pressed']
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.is_pressed: bool = False
    def button_pressed(self):
        self.is_pressed = True
    def button_released(self):
        self.is_pressed = False