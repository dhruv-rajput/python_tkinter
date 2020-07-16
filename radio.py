from tkinter import *

root = Tk()
root.title("Radio Buttons")

#r = IntVar()
#r.set("2")

MODES = [
  ("pizza","pizza"),
  ("burger","burger"),
  ("pasta","pasta"),
  ("tortia","tortia")
]

foods = StringVar()
foods.set("pizza")

for text, mode in MODES:
	Radiobutton(root , text=text,variable=foods,value=mode).pack(anchor=W)

def clicked(value):
	mylabel = Label(root, text=value)
	mylabel.pack()


#Radiobutton(root , text="Option 1",variable=r,value=1,command=lambda:clicked(r.get())).pack()
#Radiobutton(root , text="Option 2",variable=r,value=2,command=lambda:clicked(r.get())).pack()
#mylabel = Label(root, text=foods.get())
#mylabel.pack()

myButton = Button(root ,text="Click me",command=lambda:clicked(foods.get()))
myButton.pack()


































root.mainloop()



















