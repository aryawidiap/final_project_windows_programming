import os
import subprocess
import tkinter as tk
from tkinter import messagebox
from menubar import *

def create_main_window():
    """Create the main menu window."""
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("600x500")
    
    create_menu(root, "Main")

    # Add some content (optional)
    label = tk.Label(root, text="What are we doing today? ^^", font=("Arial", 24))
    label.pack(pady=50)

    button_style = {"font": ("Arial", 16), "width": 20, "height": 2, "bg": "lightgray"}
    tk.Button(root, text="Free Play", command=lambda: launch_casual_play(root), **button_style).pack(pady=10)
    tk.Button(root, text="Record", command=lambda: launch_record(root), **button_style).pack(pady=10)
    tk.Button(root, text="Playback", command=lambda: launch_playback(root), **button_style).pack(pady=10)
    tk.Button(root, text="About", command=lambda: launch_about(root), **button_style).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_main_window()

