import tkinter as tk
from gender_blade import GenderBlade
import pygame as pg
from time import sleep
import platform

from common import Common
common = Common()

# if platform.system() == 'Windows':
#     from ctypes import windll
#     windll.shcore.SetProcessDpiAwareness(1)
#     from common_windows import CommonWindows
#     common = CommonWindows()
# else:
#     from common import Common
#     common = Common()

DIVIDER_COLOR = '#bb452d'
HOLDER_COLOR = '#624944'
GENDER_BLADE_LABEL_FONT_STYLE = ('Calibri', 14)

class GenderInstrument(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=200)
        
        self.gender_blades: dict[int,GenderBlade] = {}

        note_ranges = [1,2,3,4,5,6,7,8,9,0]
        top_root = self.winfo_toplevel()
        top_root.bind(f'<KeyRelease>', self.__release_button)
        top_root.bind(f'<space>', self.press_button)
        for index, number in enumerate(note_ranges):
            # has not configured if pressed in screen
            gender_blade = GenderBlade(self, note=number, text=number, height=common.GENDER_BLADE_HEIGHT_BASE-index, width=common.GENDER_BLADE_WIDTH, font=GENDER_BLADE_LABEL_FONT_STYLE)
            top_root.bind(f'{number}', self.press_button)
            self.gender_blades[number] = gender_blade
        # self.gender_blades[number] = gender_blade
        # temp_gender_blades = self.gender_blades[0]
        # self.gender_blades.pop(0)
        # self.gender_blades[0] = temp_gender_blades
        # TODO: Clean up comments

        # index like ordered
        left_holder = tk.Frame(self, height=common.HOLDER_HEIGHT, width=common.HOLDER_WIDTH, bg=HOLDER_COLOR)
        left_holder.grid(column=0, row=0, padx=(0,5))

        divider_adder = 0
        for index, gender_blade in enumerate(self.gender_blades.values()):
            gender_blade.grid(column=index+divider_adder+1, row=0)
            if (index + 1) % 2 == 0 and (index + 1) != 10:
                divider_adder += 1
                divider_frame = tk.Frame(self)
                divider_top = tk.Frame(divider_frame, height=common.DIVIDER_HEIGHT, width=common.DIVIDER_WIDTH, bg=DIVIDER_COLOR)
                divider_gap = tk.Frame(divider_frame, height=common.DIVIDER_GAP_HEIGHT, width=common.DIVIDER_WIDTH,)
                divider_bottom = tk.Frame(divider_frame, height=common.DIVIDER_HEIGHT, width=common.DIVIDER_WIDTH, bg=DIVIDER_COLOR)
                divider_frame.grid(column=index+divider_adder+1, row=0)
                divider_top.grid(column=0, row=0)
                divider_gap.grid(column=0, row=1)
                divider_bottom.grid(column=0, row=2)
            # add divider every two blades
        
        right_holder = tk.Frame(self, height=common.HOLDER_HEIGHT, width=common.HOLDER_WIDTH, bg=HOLDER_COLOR)
        right_holder.grid(column=10+divider_adder+1, row=0, padx=(5,0))
        
        pg.init()
        pg.mixer.set_num_channels(32)

    def press_button(self, key_press_event):
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
    
    def simulate_button_press(self, note):
        key = tk.Event()
        key.char = str(note)
        self.press_button(key)
        sleep(0.3)
        self.__release_button(key)
