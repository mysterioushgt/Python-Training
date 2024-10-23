from tkinter import *  # All Modules I need to Import

#Create the root window
root =Tk()  #Initialize the window
root.title("Main Components Example")

frame =Frame(root,bg="Lightgrey" ,bd=2,relief=SUNKEN)
frame.pack(padx=10 ,pady=10)

#Create a label and add it to the frame
label =Label(frame,text="This is a Label")
label.pack(padx=5,pady=5)

#Create a button and add it to the frame
button =Button(frame,text="This is the button")
button.pack(padx=5,pady=5)

root.mainloop()