from tkinter import *
from PIL import ImageTk ,Image

root = Tk()
root.title("CheckBoxes")
root.geometry("400x400")

def show():
	my_lable = Label(root, text=var.get()).pack()


var = StringVar()
c = Checkbutton(root, text="check it" , variable = var,onvalue="On",offvalue="Off")
c.deselect()
c.pack()



my_button = Button(root, text="click me",command=show).pack()




























root.mainloop()
