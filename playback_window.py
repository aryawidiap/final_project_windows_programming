import tkinter as tk
import pygame as pg
from gender_instrument import GenderInstrument
from time import sleep
<<<<<<< HEAD
class GenderInstrument():
    def __init__(self):
        # self.note_ranges = [7,8,9,-1,-1,8,7,-1,-1,-1,8,8,7,8,9,-1,-1,-1]
        self.note_ranges = [7,8,9,7,8,9,7,8,9,7,8,9,0,9,8,-1,9,-1,8,-1,-1,9,-1,0,0,6,7,8,7,8,-1,-1,-1]
        # self.note_ranges = [7, 8, 9, -1, -1, -1, -1, 8, 7, -1, -1, -1, -1, -1, -1, -1, 8, 8, 7, 8, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 8, 8, 7, 8, 9, -1, -1]
        
=======
import threading
from tkinter.filedialog import askopenfile, askopenfiles, asksaveasfile
import platform

if platform.system() == 'Windows':
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
    from common_windows import CommonWindows
    common = CommonWindows()
else:
    from common import Common
    common = Common()

class PlayBackWindow(tk.Frame):
    def __init__(self, root):
        self.recorded_notes = []
        self.bpm = 120
        self.interval = float(60 / float(self.bpm))

>>>>>>> b2105ab0d81a14bafcebbc07fa50c193040e783c
        pg.init()
        pg.mixer.set_num_channels(256)
        # // tempo about 176 bpm
        super().__init__(root)

        self.grid(column=0,row=0,sticky=tk.NSEW)
        row_number = 0
        title_label = tk.Label(self,text='Playback',font=common.TITLE_FONT_STYLE)
        title_label.grid(column=0,row=row_number, pady=(0,15))

        row_number += 1
        control_frame = tk.Frame(self)
        control_frame.grid(column=0, row=row_number, columnspan=3, pady=(0,15))
        upload_button = tk.Button(control_frame, text="Open File", command=self.open_file, font=common.UTILITY_BUTTON_STYLE)
        upload_button.grid(column=0, row=0, padx=(common.UTILITY_BUTTON_GAP,0))
        self.play_button = tk.Button(control_frame, text="Play", command=self.start_threading, font=common.UTILITY_BUTTON_STYLE)
        self.play_button.grid(column=1, row=0, padx=(common.UTILITY_BUTTON_GAP,0))
        stop_button = tk.Button(control_frame, text="Stop", command=self.stop_threading, font=common.UTILITY_BUTTON_STYLE)
        stop_button.grid(column=2, row=0, padx=(common.UTILITY_BUTTON_GAP,0))
        self.bpm_slider = tk.Scale(control_frame, from_=60, to=240, orient=tk.HORIZONTAL, label="BPM", length=200, command=(self.set_bpm))
        self.bpm_slider.set(self.bpm)
        self.bpm_slider.grid(column=3, row=0)
        self.is_playing = False
        self.is_paused = True

        row_number += 1
        self.gender_instrument = GenderInstrument(self)
        self.gender_instrument.grid(column=0,row=row_number)

    def set_bpm(self, new_bpm):
        self.bpm = new_bpm
        self.interval = float(60 / float(self.bpm))
        print(self.bpm)

    def start_threading(self):
        if self.is_paused:
            self.play_button.config(text="Pause")
            self.is_paused = False
            if not self.is_playing:
                playback_thread = threading.Thread(target=self.playback)
                playback_thread.start()
        else:
            self.play_button.config(text="Resume")
            self.is_paused = True
    
    def stop_threading(self):
        self.is_playing = False
        self.is_paused = True
        self.play_button.config(text="Play")

    def __play_sound(self, key):
        print(key)
        if key != 'rest':
            self.gender_instrument.simulate_button_press(int(key))

    def playback(self):
        self.is_playing = True
        index = 0
        while self.is_playing:
            if not self.is_paused:
                self.__play_sound(self.recorded_notes[index])
                index += 1
                if index >= len(self.recorded_notes):
                    self.is_playing = False
                sleep(float(self.interval))
        self.is_paused = True
        self.is_playing = False
        self.play_button.config(text="Play")
    
    def open_file(self):
        self.stop_threading()
        file = askopenfile(mode = 'r', filetypes=[('Text Files', '*.txt')])

        if file is not None:
            content = file.read()
            print(content)
            self.recorded_notes = list(content.split(','))

# root = tk.Tk()
# playback_window = PlayBackWindow(root)
# # playback_thread = threading.Thread(target=playback_window.playback)
# # playback_thread.start()

# root.mainloop()
