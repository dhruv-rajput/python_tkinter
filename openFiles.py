from tkinter import *
from PIL import ImageTk ,Image
from tkinter import filedialog

root = Tk()
root.title("Open Files")
def OpenFile():
	global my_image
	root.filename = filedialog.askopenfilename(initialdir="C:/Users/DELL/Desktop/Dhruv/python101/tkinter/images",title="images",filetypes=(("Png Files","*.png"),("All Files","*.*")))
	my_image= ImageTk.PhotoImage(Image.open(root.filename))
	my_label = Label(root , image = my_image).pack()

my_btn =Button(root, text="open it u bitch!", command= OpenFile).pack()

























root.mainloop()
