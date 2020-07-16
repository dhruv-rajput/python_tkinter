from tkinter import *
from PIL import ImageTk ,Image


root = Tk()
root.title("NewWindow")

def NewWindow():
	global my_image
	top = Toplevel()
	top.title("SecondWindow")
	my_image= ImageTk.PhotoImage(Image.open("images/capture.png"))
	my_label = Label(top , image = my_image).pack()
	return

btn = Button(root ,text="open",command=NewWindow).pack()































root.mainloop()