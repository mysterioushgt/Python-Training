#PROGRAM FOR SUBMENU DROPDOWN
from tkinter import *

def red():
    root.configure(bg="red")
def green():
    root.configure(bg="green")
def orange():
    root.configure(bg="orange")
    
root =Tk()
mymenu =Menu(root)
mymenu.add_command(label="Color")
mymenu.add_command(label="Exit")
root.config(menu=mymenu)
mainmenu =Menu(root)     

m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="Red",command=red)
m1.add_command(label="Green",command=green)
m1.add_separator()
m1.add_command(label="Orange" ,command=orange)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Color" ,menu=m1)
mainmenu.add_cascade(label="Exit")
root.config(menu=mainmenu)  #config is used to set the background of window

root.mainloop()