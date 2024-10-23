#DOING GUI2 PROGRAM WITH EVENT HANDLING using Events

#This program is to Implement Sub menus
from tkinter import *

def Red():
    window.configure(bg='red')
def Blue():
    window.configure(bg='blue')
def Yellow():
    window.configure(bg='yellow')
def Orange():
    window.configure(bg='orange')        
        
window =Tk()
window.title("New Window")

menubar =Menu(window)   #Menu is used for creating menubar
menubar.add_command(label="Red" ,command=Red)
menubar.add_command(label="Blue",command=Blue)
menubar.add_command(label="Yellow" ,command=Yellow)  
menubar.add_command(label="Orange" ,command= Orange)
window.config(menu=menubar)

window.configure(bg='pink')  

window.mainloop()