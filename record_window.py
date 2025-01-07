from functools import partial
import threading
from time import sleep
import tkinter as tk
from gender_instrument import GenderInstrument
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
from menubar import *
import platform

if platform.system() == 'Windows':
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
    from common_windows import CommonWindows
    common = CommonWindows()
else:
    from common import Common
    common = Common()

class RecordWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.recorded_notes = []
        self.note_displays = []
        
        self.grid(column=0,row=0,sticky=tk.NSEW)
        row_number = 0

        title_label = tk.Label(self,text='Record',font=common.TITLE_FONT_STYLE)
        title_label.grid(column=0,row=row_number)
        
        # Partiture and button group
        row_number += 1
        notes_display_and_button_group = tk.Frame(self, )
        notes_display_and_button_group.grid(column=0, row=row_number, sticky=tk.EW)

        # Partiture
        row_number += 1
        notes_display_and_scroller = tk.Frame(notes_display_and_button_group, height=common.NOTES_DISPLAY_AND_SCROLLER_HEIGHT)
        notes_display_and_scroller.grid(column=0, row=0,sticky=tk.EW)
        notes_display_and_scroller.columnconfigure(0,weight=1)

        self.notes_display_canvas = tk.Canvas(notes_display_and_scroller, bg='white', height=common.NOTES_DISPLAY_CANVAS_HEIGHT, width=common.NOTES_DISPLAY_CANVAS_WIDTH,)
        h_scrollbar = tk.Scrollbar(notes_display_and_scroller, orient=tk.HORIZONTAL)
        h_scrollbar.grid(sticky=tk.EW, column=0, row=1)
        h_scrollbar.config(command=self.notes_display_canvas.xview)
        
        self.notes_display_canvas.config(xscrollcommand=h_scrollbar.set)
        self.notes_display_canvas.grid(column=0, row=0, sticky=tk.EW)
        self.notes_display_canvas.config(scrollregion=(0,0,10000,156))

        # Buttons row
        button_group = tk.Frame(notes_display_and_button_group)
        button_group.grid(column=1, row=0)
        ## Save button
        pause_button = tk.Button(button_group, text='Add pause\n(Spacebar)', 
                                 command=partial(self.__press_button, ' '), 
                                 font=common.UTILITY_BUTTON_STYLE)
        pause_button.grid(column=0,row=0, padx=(common.UTILITY_BUTTON_GAP,0))
        delete_button = tk.Button(button_group, text='Delete last note\n(Backspace)', command=partial(self.__press_button, '\x08'), font=common.UTILITY_BUTTON_STYLE)
        delete_button.grid(column=1,row=0, padx=(common.UTILITY_BUTTON_GAP,0))
        save_button = tk.Button(button_group, text='Save recording\n(Enter)', command=self.__save_notes, font=common.UTILITY_BUTTON_STYLE)
        save_button.grid(column=2,row=0, padx=(common.UTILITY_BUTTON_GAP,0))
        # Add play and stop button
        self.play_button = tk.Button(button_group, text="Play", command=self.start_threading, font=common.UTILITY_BUTTON_STYLE)
        self.play_button.grid(column=3, row=0, padx=(common.UTILITY_BUTTON_GAP,0))
        stop_button = tk.Button(button_group, text="Stop", command=self.stop_threading, font=common.UTILITY_BUTTON_STYLE)
        stop_button.grid(column=4, row=0, padx=(common.UTILITY_BUTTON_GAP,0))
        self.is_playing = False
        self.is_paused = True
        
        # The instrument
        row_number += 1
        self.gender_instrument = GenderInstrument(self)
        self.gender_instrument.grid(column=0,row=row_number)
        for gender_blade in self.gender_instrument.gender_blades.values():
            gender_blade.bind_command(self.__press_button, command=gender_blade.note)
        
        # Binding the keys of keyboard
        top_root = self.winfo_toplevel()
        top_root.bind(f'<space>', self.__press_key,)
        top_root.bind(f'<BackSpace>', self.__press_key,)
        
        for number in common.note_ranges:
            top_root.bind(f'{number}', self.__press_key,)
        
    def __press_key(self, key_press_event):
        pressed_key: str = key_press_event.char
        if pressed_key.isnumeric():
            pressed_key = int(pressed_key)
            if self.gender_instrument.gender_blades[pressed_key].is_pressed:
                return
        self.__press_button(pressed_key)
        self.gender_instrument.press_button(key_press_event)
    def __press_button(self, command):
        if command == '\x08':
            print("Deleting last note...")
            if len(self.recorded_notes) > 0:
                self.recorded_notes.pop()
                self.notes_display_canvas.delete(self.note_displays[-1])
                self.note_displays.pop()
            return
        note_display_width = common.NOTE_DISPLAY_WIDTH
        note_display_height = common.NOTE_DISPLAY_HEIGHT
        note = None
        if command == ' ':
            print("Adding one stop...")
            self.recorded_notes.append('rest')
            y1 = 0 + 3
            y2 = y1 + note_display_height * 10
            color = 'white'
        elif type(command) is int:
            if int(command) in common.note_ranges:
                note = int(command)
                self.recorded_notes.append(note)
                note = note if note != 0 else 10
                y1 = (10 - note) * note_display_height + 3
                color = 'brown'
                y2 = y1 + note_display_height
            else:
                return
        note_index = len(self.recorded_notes)
        x1 = note_index * note_display_width + 3
        x2 = x1 + note_display_width
        print(x1,x2)
        print(y1,y2)
        print(self.recorded_notes)

        self.note_displays.append(self.notes_display_canvas.create_rectangle(x1, y1, x2, y2,fill = color,))
    def __save_notes(self):
        files = [('Plain text', '*.txt'), ('All files', '*.*'),]
        saved_file = asksaveasfile(filetypes=files, defaultextension=files,)
        notes_text = ','.join(str(note) for note in self.recorded_notes)
        if saved_file != None: saved_file.write(notes_text)
        return
    def start_threading(self):
        if len(self.recorded_notes) == 0:
            messagebox.showwarning('No recorded note yet', 'Please record the notes before playing.')
            return
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
    def __play_sound(self, key):
        print(key)
        if key != 'rest':
            self.gender_instrument.simulate_button_press(int(key))

root = tk.Tk()
create_menu(root, "Record")

record_window = RecordWindow(root)
root.mainloop()
