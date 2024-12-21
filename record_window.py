import tkinter as tk
from gender_instrument import GenderInstrument
from tkinter.filedialog import asksaveasfile
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
import time

class RecordWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.recorded_notes = []
        self.notes_display_var = tk.StringVar()
        self.notes_display_var.set('test')
        
        self.grid(column=0,row=0,sticky=tk.NSEW)
        row_number = 0
        title_label = tk.Label(self,text='Record')
        title_label.grid(column=0,row=row_number)
        row_number += 1
        notes_display = tk.Label(self,textvariable=self.notes_display_var)
        notes_display.grid(column=0, row=row_number)
        row_number += 1
        picture_frame = tk.Frame(self,width=200, height=100)
        picture_frame.grid(column=0,row=row_number)
        row_number += 1
        gender_instrument = GenderInstrument(self)
        gender_instrument.grid(column=0,row=row_number)
        row_number += 1
        top_root = self.winfo_toplevel()
        # top_root.bind(f'<KeyRelease>', self.__release_button)
        top_root.bind(f'<space>', self.__press_button, add=True)
        top_root.bind(f'<BackSpace>', self.__press_button, add=True)
        note_ranges = [1,2,3,4,5,6,7,8,9,0]
        for number in note_ranges:
            # has not configured if pressed in screen
            top_root.bind(f'{number}', self.__press_button, add=True)
        save_button = tk.Button(self, text='Save recording', command=self.__save_notes)
        save_button.grid(column=0,row=row_number)
    def __press_button(self, key_press_event):
        pressed_key: str = key_press_event.char
        # print(pressed_key)
        # print(key_press_event)
        if pressed_key == '\x08':
            print("Deleting last note...")
            if len(self.recorded_notes) > 0:
                self.recorded_notes.pop()
        if pressed_key == ' ':
            print("Adding one stop...")
            self.recorded_notes.append(-1)
        if pressed_key.isnumeric():
            self.recorded_notes.append(int(pressed_key))
        print(self.recorded_notes)
        # instead of below, maybe make a new frame
        # grid a square, where note => row
        # the index in list => column
        # use the len of the list
        self.notes_display_var.set(" | ".join(map(str, self.recorded_notes)))

    def __save_notes(self):
        files = [('All files', '*.*'), ('Plain text', '*.txt')]
        saved_file = asksaveasfile(filetypes=files, defaultextension=files,)
        notes_text = ','.join(str(note) for note in self.recorded_notes)
        if saved_file != None: saved_file.write(notes_text)
        return

root = tk.Tk()

play_window = RecordWindow(root)

root.mainloop()
