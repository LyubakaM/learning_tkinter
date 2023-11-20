from tkinter import *

root = Tk()

# creating a label widget
myLabel = Label(root, text="My first window :D")
myLabel2 = Label(root, text="Hello")

# shoving it onto the screen
myLabel.pack()
myLabel2.pack()
# myLabel.grid(row=0, column=0)     with .grid
# myLabel2.grid(row=1, column=0)

root.mainloop()