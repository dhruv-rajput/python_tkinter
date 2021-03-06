from tkinter import *
from PIL import ImageTk ,Image

root = Tk()
root.title("Frames")


frame1=LabelFrame(root,padx=5,pady=5)
frame1.grid(row=0,column=0,padx=10,pady=10)


frame2=LabelFrame(root,padx=5,pady=35)
frame2.grid(row=0,column=1,padx=10,pady=10)

#CALCULATOR FRAME 1
e = Entry(frame1 , width=40 , borderwidth=5)
e.grid(row=0 , column=0,columnspan=4, padx=10,pady=10)

def button_click(number):
	current = e.get()
	e.delete(0 , END)
	e.insert(0 , str(current) + str(number))

def button_clear():
	e.delete(0,END)

def button_add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0,END)

def button_equal():
	second_number = e.get()
	e.delete(0,END)
	if math == 'addition':
		e.insert(0 , f_num + int(second_number))
	if math == 'subtraction':
		e.insert(0 , f_num - int(second_number))
	if math == 'multiplication':
		e.insert(0 , f_num * int(second_number))	
	if math == 'division':
		e.insert(0 , f_num / int(second_number))	

def button_subtract():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0,END)

def button_multiply():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0,END)

def button_divide():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	e.delete(0,END)

button_1 = Button(frame1 , text="1" , padx=40 , pady=20 ,borderwidth=3,command=lambda: button_click(1))
button_2 = Button(frame1 , text="2" , padx=40 , pady=20 ,borderwidth=3,command=lambda: button_click(2)) 
button_3 = Button(frame1 , text="3" , padx=40 , pady=20 ,borderwidth=3,command=lambda: button_click(3)) 
button_4 = Button(frame1 , text="4" , padx=40 , pady=20 ,borderwidth=3,command=lambda: button_click(4))
button_5 = Button(frame1 , text="5" , padx=40 , pady=20 ,borderwidth=3,command=lambda: button_click(5)) 
button_6 = Button(frame1 , text="6" , padx=40 , pady=20 ,borderwidth=3,command=lambda: button_click(6)) 
button_7 = Button(frame1 , text="7" , padx=40 , pady=20 ,borderwidth=3,command=lambda: button_click(7)) 
button_8 = Button(frame1 , text="8" , padx=40 , pady=20 ,borderwidth=3,command=lambda: button_click(8)) 
button_9 = Button(frame1 , text="9" , padx=40 , pady=20 ,borderwidth=3,command=lambda: button_click(9))   
button_0 = Button(frame1 , text="0" , padx=40 , pady=20 ,borderwidth=3,command=lambda: button_click(0)) 
button_add = Button(frame1 , text=" + " , padx=36.4 , pady=20 ,borderwidth=3,command=button_add)
button_equal = Button(frame1 , text="=" , padx=86.5 , pady=20 ,borderwidth=3,command=button_equal) 
button_clear = Button(frame1 , text="Clear" ,padx=29.5, pady=14 ,borderwidth=3,command=button_clear) 
button_subtract = Button(frame1 , text="-" , padx=40.5 , pady=20 ,borderwidth=3,command=button_subtract)  
button_multiply = Button(frame1 , text="*" , padx=40.5 , pady=20 ,borderwidth=3,command=button_multiply)  
button_divide = Button(frame1 , text="/" , padx=40.5 , pady=20 ,borderwidth=3,command=button_divide)  
    
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)
button_clear.grid(row=0,column=4, columnspan =1)
button_add.grid(row=1,column=4)
button_equal.grid(row=4,column=1 , columnspan =2)
button_subtract.grid(row=2,column=4)
button_multiply.grid(row=3,column=4)
button_divide.grid(row=4,column=4)




#IMAGES FRAME 2

my_img1 = ImageTk.PhotoImage(Image.open('images/capture.png'))
my_img2 = ImageTk.PhotoImage(Image.open('images/capture1.png'))
my_img3 = ImageTk.PhotoImage(Image.open('images/capture2.png'))
my_img4 = ImageTk.PhotoImage(Image.open('images/capture3.png'))
my_img5 = ImageTk.PhotoImage(Image.open('images/capture4.png'))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1,relief = SUNKEN,anchor=E)
my_label = Label(frame2,image=my_img1)
my_label.grid(row= 0 , column = 0, columnspan=3)



def forward(image_number):
	global my_label
	global button_forward
	global button_back
	
	my_label= Label(frame2,image=image_list[image_number])
	my_label.grid_forget()
	button_forward= Button(frame2,text=">>",command=lambda:forward(image_number+1))
	button_back = Button(frame2,text="<<",command=lambda:back(image_number-1))
	if image_number ==4:
		button_forward = Button(frame2,text=">>", state=DISABLED)
	my_label.grid(row= 0 , column = 0, columnspan=3)
	button_back.grid(row=1,column=0)
	button_forward.grid(row=1,column=2)
	status = Label(root, text="Image " + str(image_number+1) + " of " + str(len(image_list)), bd=1,relief = SUNKEN,anchor=E)
	status.grid(row=2, column=0 ,columnspan=3,sticky=W+E)

def back(image_number):
	global my_label
	global button_forward
	global button_back
	my_label= Label(frame2,image=image_list[image_number])
	my_label.grid_forget()
	button_forward= Button(frame2,text=">>",command=lambda:forward(image_number+1))
	button_back = Button(frame2,text="<<",command=lambda:back(image_number-1))
	if image_number ==0:
		button_back = Button(frame2,text="<<", state=DISABLED)
	my_label.grid(row= 0 , column = 0, columnspan=3)
	button_back.grid(row=1,column=0)
	button_forward.grid(row=1,column=2)
	status = Label(root, text="Image " + str(image_number+1) + " of " + str(len(image_list)), bd=1,relief = SUNKEN,anchor=E)
	status.grid(row=2, column=0 ,columnspan=3,sticky=W+E)
	
button_back = Button(frame2,text="<<",command=back,state=DISABLED)
button_quit = Button(frame2 , text= "Exit Program", command=root.quit)
button_forward = Button(frame2,text=">>",command=lambda:forward(1))
button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)
status.grid(row=2, column=0 ,columnspan=3,sticky=W+E)
root.mainloop()





























root.mainloop()
