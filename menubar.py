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

def launch_main_menu(current_window):
    """Launch the Main Menu window and close the current window."""
    launch_app("main.py", current_window)

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

    if current_menu != "Main":
        # Create the "Main Menu" menu
        menubar.add_command(label="Main Menu", command=lambda: launch_main_menu(root))

    if current_menu != "Free Play":
        # Create the "Free Play" menu
        menubar.add_command(label="Free Play", command=lambda: launch_casual_play(root))

    if current_menu != "Record":
        # Create the "Record" menu
        menubar.add_command(label="Record", command=lambda: launch_record(root))

    if current_menu != "Playback":
        # Create the "Playback" menu
        menubar.add_command(label="Playback", command=lambda: launch_playback(root))

    if current_menu != "About":
        # Create the "About" menu
        menubar.add_command(label="About", command=lambda: launch_about(root))

    # Configure the menubar
    root.config(menu=menubar)