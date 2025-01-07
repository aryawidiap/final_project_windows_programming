import os
import subprocess
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # For handling the image

def launch_casual_play(current_window):
    """Launch the casual play window and close the current window."""
    launch_app("casual_play_window.py", current_window)

def launch_playback(current_window):
    """Launch the playback window and close the current window."""
    launch_app("playback_window.py", current_window)

def launch_record(current_window):
    """Launch the record window and close the current window."""
    launch_app("record_window.py", current_window)

def launch_main_menu(current_window):
    """Launch the Main Menu window and close the current window."""
    launch_app("main.py", current_window)

def launch_app(file_name, current_window):
    """Launch a Python file in a new process."""
    try:
        # Ensure the file exists before attempting to launch it
        if not os.path.exists(file_name):
            raise FileNotFoundError(f"File '{file_name}' not found.")
        
        # Launch the file
        subprocess.Popen(["python", file_name])
        # Close the current window
        current_window.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to launch {file_name}: {e}")

def create_about_window():
    """Create the About window."""
    about_window = tk.Tk()
    about_window.title("About")
    about_window.geometry("600x500")

    # Add a menubar
    menubar = tk.Menu(about_window)

    # Create the "Main Menu" menu
    main_menu = tk.Menu(menubar, tearoff=0)
    main_menu.add_command(label="Run", command=lambda: launch_main_menu(about_window))
    menubar.add_cascade(label="Main Menu", menu=main_menu)

    # Create the "Free Play" menu
    free_play_menu = tk.Menu(menubar, tearoff=0)
    free_play_menu.add_command(label="Run", command=lambda: launch_casual_play(about_window))
    menubar.add_cascade(label="Free Play", menu=free_play_menu)

    # Create the "Record" menu
    record_menu = tk.Menu(menubar, tearoff=0)
    record_menu.add_command(label="Run", command=lambda: launch_record(about_window))
    menubar.add_cascade(label="Record", menu=record_menu)

    # Create the "Playback" menu
    playback_menu = tk.Menu(menubar, tearoff=0)
    playback_menu.add_command(label="Run", command=lambda: launch_playback(about_window))
    menubar.add_cascade(label="Playback", menu=playback_menu)

    # Configure the menubar
    about_window.config(menu=menubar)

    # Add a title label
    title_label = tk.Label(about_window, text="About Gender Virtual", font=("Arial", 20, "bold"), pady=10)
    title_label.pack()

    # Add a picture
    try:
        # Load the image from the "misc" directory
        image_path = "misc/gender_resized.jpg"
        image = Image.open(image_path)
        image = image.resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        # Display the image
        image_label = tk.Label(about_window, image=photo)
        image_label.image = photo  # Keep a reference to avoid garbage collection
        image_label.pack(pady=10)
    except Exception as e:
        # Handle errors if the image cannot be loaded
        error_label = tk.Label(about_window, text=f"Error loading image: {e}", fg="red", font=("Arial", 12))
        error_label.pack()

    # Add a description
    description = (
        "The gendèr is a metallophone used in Balinese and Javanese gamelan music, with 10–14 tuned metal bars "
        "suspended over bamboo or metal resonators. Played with two mallets, it produces melodies across two octaves, "
        "with five notes per octave. In Javanese gamelan, different gendèr are tuned for specific scales. "
        "A key technique involves dampening the previously struck note with the same hand while playing the next.\n\n"
        "The gendèr resembles instruments like the Balinese gangsa and Javanese slenthem, but stands out with its intricate, "
        "contrapuntal melodies and the challenge of simultaneous playing and dampening."
    )
    description_label = tk.Label(about_window, text=description, wraplength=550, justify="left", font=("Arial", 12))
    description_label.pack(pady=10)

    about_window.mainloop()

if __name__ == "__main__":
    create_about_window()

