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
        subprocess.Popen(["python3", file_name])
        # Close the current window
        current_window.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to launch {file_name}: {e}")

def create_main_window():
    """Create the main menu window."""
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("600x500")
    
    menubar = tk.Menu(root)

    # Create the "Free Play" menu
    free_play_menu = tk.Menu(menubar, tearoff=0)
    free_play_menu.add_command(label="Run", command=lambda: launch_casual_play(root))
    menubar.add_cascade(label="Free Play", menu=free_play_menu)

    # Create the "Record" menu
    record_menu = tk.Menu(menubar, tearoff=0)
    record_menu.add_command(label="Run", command=lambda: launch_record(root))
    menubar.add_cascade(label="Record", menu=record_menu)

    # Create the "Playback" menu
    playback_menu = tk.Menu(menubar, tearoff=0)
    playback_menu.add_command(label="Run", command=lambda: launch_playback(root))
    menubar.add_cascade(label="Playback", menu=playback_menu)

    # Create the "About" menu
    about_menu = tk.Menu(menubar, tearoff=0)
    about_menu.add_command(label="Run", command=lambda: launch_about(root))
    menubar.add_cascade(label="About", menu=about_menu)

    # Configure the menubar
    root.config(menu=menubar)

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

