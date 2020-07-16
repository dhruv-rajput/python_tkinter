from tkinter import *
from PIL import ImageTk ,Image
from tkinter import messagebox


root = Tk()
root.title("Messages")

#showinfo , showwarning , showerror , askquestion , askokcancel , askyesno

def popup():
	messagebox.askokcancel("This is my popup","Hello world!")

Button(root ,text="pop up",command=popup).pack()






































root.mainloop()

