# Python program to bind all 
# the number keys in Tkinter 

# Import the library Tkinter 
from tkinter import *

# Create a GUI app 
app = Tk() 

# Set the title and geometry of the app 
app.title('Bind Number Keys') 
app.geometry("800x400") 

# Make a function to display a message 
# whenever user presses 0-9 key 
def key_press(a): 
	Label(app, text="You pressed: " + a.char, 
		font='Helvetica 18 bold').pack() 

# Create a label widget to display the text 
label = Label(app, text="Press any key in between range 0-9") 
label.pack(pady=25) 
label.config(font='Arial 20 bold') 

# Bind all the number keys with the callback function 
for i in range(10): 
	app.bind(str(i), key_press) 

# Make infinite loop for displaying app on the screen 
app.mainloop() 
