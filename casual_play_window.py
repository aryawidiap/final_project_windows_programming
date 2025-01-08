import tkinter as tk
from gender_instrument import GenderInstrument
from menubar import *
# from ctypes import windll
# windll.shcore.SetProcessDpiAwareness(1)
import time
import platform

if platform.system() == 'Windows':
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
    from common_windows import CommonWindows
    common = CommonWindows()
else:
    from common import Common
    common = Common()

class CasualPlayWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        
        self.grid(column=0,row=0,sticky=tk.NSEW)
        title_label = tk.Label(self,text='Casual Play',font=common.TITLE_FONT_STYLE)
        title_label.grid(column=0,row=0)
        picture_frame = tk.Frame(self,width=200, height=100)
        picture_frame.grid(column=0,row=1)

        gender_instrument = GenderInstrument(self)
        gender_instrument.grid(column=0,row=2)


root = tk.Tk()
create_menu(root, "Free Play")

play_window = CasualPlayWindow(root)
root.title("Virtual Gender | Casual Play")
root.resizable(False, False)
root.mainloop()
