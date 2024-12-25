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
        self.note_ranges = [7, 8, 9, -1, -1, -1, -1, 8, 7, -1, -1, -1, -1, -1, -1, -1, 8, 8, 7, 8, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 8, 8, 7, 8, 9, -1, -1]
        
        pg.init()
        pg.mixer.set_num_channels(256)
        # // tempo about 176 bpm
        # add button to choose the file

        super().__init__(root)

        self.grid(column=0,row=0,sticky=tk.NSEW)
        row_number = 0
        title_label = tk.Label(self,text='Playback')
        title_label.grid(column=0,row=row_number)
        row_number += 1
        picture_frame = tk.Frame(self,width=200, height=100)
        picture_frame.grid(column=0,row=row_number)
        row_number += 1
        self.gender_instrument = GenderInstrument(self)
        self.gender_instrument.grid(column=0,row=row_number)
        row_number += 1
        upload_button = tk.Button(self, text="Upload File", command=self.open_file)
        upload_button.grid(column=0, row=row_number)
        row_number += 1
        ## playback button
        self.play_button = tk.Button(self, text="Play Back", command=self.start_threading)
        self.play_button.grid(column=0, row=row_number)
        self.is_playing = False

    def start_threading(self):
        if self.is_playing:
            self.play_button.config(text="Play Back")
            self.is_playing = False
        else:
            self.play_button.config(text="Stop")
            self.is_playing = True
            playback_thread = threading.Thread(target=self.playback)
            playback_thread.start()
        
    def __play_sound(self, key):
        print(key)
        if key != -1:
            self.gender_instrument.simulate_button_press(key)
            ##sound = pg.mixer.Sound(f"sounds/note_v_0-9_-0{key}.mp3")
            ##sound.play()
        # return

    def playback(self):
        self.is_playing = True
        for note in self.note_ranges:
            if not self.is_playing:
                break
            self.__play_sound(note)
            sleep(0.5)
        self.is_playing = False
        self.play_button.config(text="Play Back")
    
    def open_file(self):
        file = askopenfile(mode = 'r')
        if file is not None:
            content = file.read()
            print(content)
            self.note_ranges = list(map(int, content.split(',')))
            

            

root = tk.Tk()
playback_window = PlayBackWindow(root)
# playback_thread = threading.Thread(target=playback_window.playback)
# playback_thread.start()

root.mainloop()
