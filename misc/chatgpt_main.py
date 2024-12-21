import tkinter as tk
from tkinter import Menu

# Create the main window
root = tk.Tk()
root.title("Gender Virtual")
root.geometry("400x600")  # Set the window size

# Create a menu bar
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="File")
file_menu.add_command(label="Record")
menu_bar.add_cascade(label="Menu", menu=file_menu)
root.config(menu=menu_bar)

# Create the label for "Casual Play"
casual_label = tk.Label(root, text="Casual Play", bg="black", fg="white", font=("Arial", 16, "bold"))
casual_label.pack(pady=10)

# Create a frame for the placeholder picture
picture_frame = tk.Frame(root, width=300, height=200, bg="lightgray")
picture_frame.pack(pady=20)
picture_frame.pack_propagate(False)  # Prevent resizing to fit content

# Add placeholder text in the picture frame
placeholder_label = tk.Label(picture_frame, text="Picture of a gender from above", bg="lightgray", font=("Arial", 10))
placeholder_label.pack(expand=True)

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Create the numbered buttons
buttons = []
for i in range(10):
    button = tk.Button(button_frame, text=str(i), font=("Arial", 14), width=4, height=2)
    button.grid(row=0, column=i, padx=2)
    buttons.append(button)

# Run the application
root.mainloop()
