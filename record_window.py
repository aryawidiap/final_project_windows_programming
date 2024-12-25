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
        self.note_displays = []
        
        self.grid(column=0,row=0,sticky=tk.NSEW)
        row_number = 0

        title_label = tk.Label(self,text='Record',font=('Calibri', 16))
        title_label.grid(column=0,row=row_number)
        # notes_display = tk.Label(self,textvariable=self.notes_display_var)
        # notes_display.grid(column=0, row=row_number)
        
        # Partiture and button group
        row_number += 1
        notes_display_and_button_group = tk.Frame(self, )
        notes_display_and_button_group.grid(column=0, row=row_number)

        # Partiture
        row_number += 1
        notes_display_and_scroller = tk.Frame(notes_display_and_button_group, height=160,  width=300,)
        notes_display_and_scroller.grid(column=0, row=0)

        h_scrollbar = tk.Scrollbar(notes_display_and_scroller, orient=tk.HORIZONTAL)
        h_scrollbar.grid(sticky=tk.EW, column=0,row=1)
        
        self.notes_display_canvas = tk.Canvas(notes_display_and_scroller, bg='white', height=156,  width=300, yscrollcommand=h_scrollbar.set)
        self.notes_display_canvas.grid(column=0, row=0)
        h_scrollbar.config(command=self.notes_display_canvas)
        

        # Buttons row
        button_group = tk.Frame(notes_display_and_button_group)
        button_group.grid(column=1, row=0)
        ## Save button
        pause_button = tk.Button(button_group, text='Add pause\n(Spacebar)', command=self.__save_notes)
        pause_button.grid(column=0,row=0, padx=(20,0))
        delete_button = tk.Button(button_group, text='Delete last note\n(Backspace)', command=self.__save_notes)
        delete_button.grid(column=1,row=0, padx=(20,0))
        save_button = tk.Button(button_group, text='Save recording\n(Enter)', command=self.__save_notes)
        save_button.grid(column=2,row=0, padx=(20,0))

        # row_number += 1
        # picture_frame = tk.Frame(self,width=200, height=100)
        # picture_frame.grid(column=0,row=row_number)
        
        # The instrument
        row_number += 1
        gender_instrument = GenderInstrument(self)
        gender_instrument.grid(column=0,row=row_number)
        
        # Binding the keys of keyboard
        top_root = self.winfo_toplevel()
        # top_root.bind(f'<KeyRelease>', self.__release_button)
        top_root.bind(f'<space>', self.__press_button, add=True)
        top_root.bind(f'<BackSpace>', self.__press_button, add=True)
        note_ranges = [1,2,3,4,5,6,7,8,9,0]
        for number in note_ranges:
            # has not configured if pressed in screen
            top_root.bind(f'{number}', self.__press_button, add=True)
        
    def __press_button(self, key_press_event):
        pressed_key: str = key_press_event.char
        # print(pressed_key)
        # print(key_press_event)
        if pressed_key == '\x08':
            print("Deleting last note...")
            if len(self.recorded_notes) > 0:
                self.recorded_notes.pop()
                self.notes_display_canvas.delete(self.note_displays[-1])
                self.note_displays.pop()
            return
        note_display_width = 20
        note_display_height = 15
        note_index = len(self.recorded_notes)
        x1 = note_index * note_display_width + 3
        x2 = x1 + note_display_width
        print(x1,x2)
        if pressed_key == ' ':
            print("Adding one stop...")
            self.recorded_notes.append(-1)
            y1 = 0 + 3
            y2 = y1 + note_display_height * 10
            color = 'white'
        note = None
        if pressed_key.isnumeric():
            self.recorded_notes.append(int(pressed_key))
            note = int(pressed_key) if int(pressed_key) != 0 else 10
            y1 = (10 - note) * note_display_height + 3
            color = 'brown'
            y2 = y1 + note_display_height
        print(y1,y2)
            
        print(self.recorded_notes)
        # instead of below, maybe make a new frame
        # grid a square, where note => row
        # the index in list => column
        # use the len of the list
        self.notes_display_var.set(" | ".join(map(str, self.recorded_notes)))
        
        self.note_displays.append(self.notes_display_canvas.create_rectangle(x1, y1, x2, y2,fill = color,))
        

    def __save_notes(self):
        files = [('All files', '*.*'), ('Plain text', '*.txt')]
        saved_file = asksaveasfile(filetypes=files, defaultextension=files,)
        notes_text = ','.join(str(note) for note in self.recorded_notes)
        if saved_file != None: saved_file.write(notes_text)
        return

root = tk.Tk()

play_window = RecordWindow(root)

root.mainloop()
