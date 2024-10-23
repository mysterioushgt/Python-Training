from tkinter import *

def mouseClick(event):
    message ="mouse clicked at x=" +str(event.x) + ", y=" +str(event.y)
    panellabel.config(text=message)
    
window =Tk()
label1=Label(window ,text= "Click me")
label1.pack()
panellabel=Label(window,text="Result Panel")
label1.bind("<Button>" ,mouseClick)
b1=Button(window ,text="OK" ,fg ="Red" ,bg="Orange")
b2=Button(window ,text="CANCEL" ,fg ="Green" ,bg="Orange")
b1.pack()  #Otherwise component will not be visible
b2.pack()
b1.bind("<Button>" ,mouseClick)  #<Button> Represents Mouse Left Click
b2.bind("<Button>" ,mouseClick)
panellabel.pack()
window.mainloop()