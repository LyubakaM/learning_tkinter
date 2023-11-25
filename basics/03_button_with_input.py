from tkinter import *

root = Tk()

entry_widget = Entry(root, width=20, bg="gray", fg="white")
entry_widget.pack()
entry_widget.insert(0, "Enter your name here...")

def my_click():
    hello = "Hello " + entry_widget.get()
    my_label = Label(root, text=hello)     # you can use var hello or just .get()
    my_label.pack()


my_button = Button(root, text="Enter your name", command=my_click, fg="white", bg="gray")
my_button.pack()

root.mainloop()