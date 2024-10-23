from tkinter import *
#This program is to Implement Sub menus

def mycolor(myself):
    window.configure(bg='red')
    
window =Tk()
window.title("New Window")

menubar =Menu(window)   #Menu is used for creating menubar
menubar.add_command(label="Red")
menubar.add_command(label="Blue")
menubar.add_command(label="Yellow")  
menubar.add_command(label="Orange")
window.config(menu=menubar)

window.configure(bg='pink')  

window.mainloop()