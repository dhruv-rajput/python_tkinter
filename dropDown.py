from tkinter import *
from PIL import ImageTk ,Image

root = Tk()
root.title("DropDown")
root.geometry("400x400")
def show():
 	mylabel=Label(root, text=clicked.get()).pack()

options= [
"Monday",
"Tuesday",
"Wednesday"
]




clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root, clicked ,*options)
drop.pack()
myButton = Button(root, text="Show Selection", command=show).pack()















root.mainloop()
