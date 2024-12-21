import tkinter as tk
from gender_blade import GenderBlade
import pygame as pg

class GenderInstrument(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=200)
        
        self.gender_blades: dict[int,GenderBlade] = {}

        note_ranges = [1,2,3,4,5,6,7,8,9,0]
        top_root = self.winfo_toplevel()
        top_root.bind(f'<KeyRelease>', self.__release_button)
        top_root.bind(f'<space>', self.__press_button)
        for index, number in enumerate(note_ranges):
            # has not configured if pressed in screen
            gender_blade = GenderBlade(self, note=number, text=number, height=15+10-index, width=15,)
            top_root.bind(f'{number}', self.__press_button)
            self.gender_blades[number] = gender_blade
        # self.gender_blades[number] = gender_blade
        # temp_gender_blades = self.gender_blades[0]
        # self.gender_blades.pop(0)
        # self.gender_blades[0] = temp_gender_blades

        # index like ordered
        for index, gender_blade in enumerate(self.gender_blades.values()):
            print(index, gender_blade)
            gender_blade.grid(column=index, row=0)
            # add divider every two blades
        
        pg.init()
        pg.mixer.set_num_channels(32)

    def __press_button(self, key_press_event):
        pressed_key: str = key_press_event.char
        # print(pressed_key)
        if pressed_key.isnumeric():
            pressed_key_numeric = int(pressed_key)
            pressed_button = self.gender_blades[pressed_key_numeric]
            if pressed_button.is_pressed:
                return
            pressed_button.config(relief='sunken')
            pressed_button.button_pressed()
            # TODO: remove operations if sounds already exists
            pressed_button.play_sound() 
    def __release_button(self, key_press_event):
        pressed_key: str = key_press_event.char
        if pressed_key.isnumeric():
            pressed_button = self.gender_blades[int(pressed_key)]
            pressed_button.config(relief='raised')
            pressed_button.button_released()
    
# root = tk.Tk()
# instrument = GenderInstrument(root)
# instrument.grid()
# root.mainloop()
