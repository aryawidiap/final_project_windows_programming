import os
import subprocess
import tkinter as tk
from tkinter import messagebox

def launch_casual_play(current_window):
    """Launch the casual play window."""
    launch_app("casual_play_window.py", current_window)

def launch_playback(current_window):
    """Launch the playback window."""
    launch_app("playback_window.py", current_window)

def launch_record(current_window):
    """Launch the record window."""
    launch_app("record_window.py", current_window)

def launch_about(current_window):
    """Launch the about window."""
    launch_app("about.py", current_window)

def launch_app(file_name, current_window):
    """Launch a Python file in a new process."""
    try:
        # Ensure the file exists before attempting to launch it
        if not os.path.exists(file_name):
            raise FileNotFoundError(f"File '{file_name}' not found.")
        
        # Launch the file using subprocess
        subprocess.Popen(["python", file_name])
        # Close the current window
        current_window.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to launch {file_name}: {e}")

def create_menu(root, current_menu):
    """Create the main menu window."""
    menubar = tk.Menu(root)

    if current_menu != "Free Play":
        # Create the "Free Play" menu
        free_play_menu = tk.Menu(menubar, tearoff=0)
        free_play_menu.add_command(label="Run", command=lambda: launch_casual_play(root))
        menubar.add_cascade(label="Free Play", menu=free_play_menu)

    if current_menu != "Record":
        # Create the "Record" menu
        record_menu = tk.Menu(menubar, tearoff=0)
        record_menu.add_command(label="Run", command=lambda: launch_record(root))
        menubar.add_cascade(label="Record", menu=record_menu)

    if current_menu != "Playback":
        # Create the "Playback" menu
        playback_menu = tk.Menu(menubar, tearoff=0)
        playback_menu.add_command(label="Run", command=lambda: launch_playback(root))
        menubar.add_cascade(label="Playback", menu=playback_menu)

    if current_menu != "About":
        # Create the "About" menu
        about_menu = tk.Menu(menubar, tearoff=0)
        about_menu.add_command(label="Run", command=lambda: launch_about(root))
        menubar.add_cascade(label="About", menu=about_menu)

    # Configure the menubar
    root.config(menu=menubar)