import tkinter as tk
from gender_instrument import GenderInstrument
# from ctypes import windll
# windll.shcore.SetProcessDpiAwareness(1)
import time

class PlayWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        
        self.grid(column=0,row=0,sticky=tk.NSEW)
        title_label = tk.Label(self,text='Casual Play')
        title_label.grid(column=0,row=0)
        picture_frame = tk.Frame(self,width=200, height=100)
        picture_frame.grid(column=0,row=1)

        gender_instrument = GenderInstrument(self)
        gender_instrument.grid(column=0,row=2)


# root = tk.Tk()

# play_window = PlayWindow(root)

# root.mainloop()
