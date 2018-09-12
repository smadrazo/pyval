from tkinter import *
from tkinter import ttk


# ---------- MULTIPLE COMPONENTS  ----------
# Some of the different Widgets : Button, Label,
# Canvas, Menu, Text, Scale, OptionMenu, Frame,
# CheckButton, LabelFrame, MenuButton, PanedWindow,
# Entry, ListBox, Message, RadioButton, ScrollBar,
# Bitmap, SpinBox, Image

root = Tk()

# Window configuration (geometry,title,etc)
root.title("App Title")
root.geometry('300x200')

# Frame widgets surround other widgets
frame = Frame(root)

# We'll use a TkInter variable for our label text
# so we can change it with set
labelText = StringVar()

# Create a label and button object
# You can set attributes on creation or by calling
# methods

label = Label(frame, textvariable=labelText)
button = Button(frame, text="Click Me")

# Change the label text
labelText.set("This is a test of TkInter")

# Pack positions the widgets in the window
# It is a simple geometry manager
label.pack()
button.pack()
frame.pack()

root.mainloop()
