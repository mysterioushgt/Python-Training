from tkinter import *  # All Modules I need to Import
window= Tk()  #Initialize the window

label1 =Label(window ,text="Choose Your Option")
label1.place(x=40,y=20)
label1.pack() # if we will not use pack The component will not be visible

button1 =Button(window,text="OK",bg="Red",fg="yellow")
button2 =Button(window,text="Cancel",bg="Blue",fg="yellow")
button1.place(x=240 ,y=60)
button2.place(x=240 ,y=80)

button1.pack()  #To make it visible
button2.pack()  #To make it visible

window.title("hello python")  #title funct is defined inside the tk
window.geometry("300x200")
window.mainloop()   # the window now can accept the events