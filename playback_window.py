import tkinter as tk
import pygame as pg
from gender_instrument import GenderInstrument
from time import sleep
import threading
from tkinter.filedialog import askopenfile, askopenfiles, asksaveasfile
class PlayBackWindow(tk.Frame):
    def __init__(self, root):
        # self.note_ranges = [7,8,9,-1,-1,8,7,-1,-1,-1,8,8,7,8,9,-1,-1,-1]
        # self.note_ranges = [7,8,9,7,8,9,7,8,9,7,8,9,0,9,8,-1,9,-1,8,-1,-1,9,-1,0,0,6,7,8,7,8,-1,-1,-1]
        self.recorded_notes = []
        
        pg.init()
        pg.mixer.set_num_channels(256)
        # // tempo about 176 bpm
        # add button to choose the file

        super().__init__(root)

        self.grid(column=0,row=0,sticky=tk.NSEW)
        row_number = 0
        title_label = tk.Label(self,text='Play')
        title_label.grid(column=0,row=row_number)

        row_number += 1
        control_frame = tk.Frame(self)
        control_frame.grid(column=0, row=row_number, columnspan=3, )
        upload_button = tk.Button(control_frame, text="Upload File", command=self.open_file, height=5, width=10)
        upload_button.grid(column=0, row=0)
        self.play_button = tk.Button(control_frame, text="Play", command=self.start_threading, height=5, width=10)
        self.play_button.grid(column=1, row=0)
        stop_button = tk.Button(control_frame, text="Stop", command=self.stop_threading, height=5, width=10)
        stop_button.grid(column=2, row=0)
        self.is_playing = False
        self.is_paused = True

        row_number += 1
        picture_frame = tk.Frame(self,width=200, height=100)
        picture_frame.grid(column=0,row=row_number)
        row_number += 1
        self.gender_instrument = GenderInstrument(self)
        self.gender_instrument.grid(column=0,row=row_number)

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
            ##sound = pg.mixer.Sound(f"sounds/note_v_0-9_-0{key}.mp3")
            ##sound.play()
        # return

    def playback(self):
        self.is_playing = True
        index = 0
        while self.is_playing:
            if not self.is_paused:
                self.__play_sound(self.recorded_notes[index])
                index += 1
                if index >= len(self.recorded_notes):
                    self.is_playing = False
                sleep(0.5)
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

root = tk.Tk()
playback_window = PlayBackWindow(root)
# playback_thread = threading.Thread(target=playback_window.playback)
# playback_thread.start()

root.mainloop()
