"""DISABLE THE RESULT BOX
USING TRY AND EXCEPT PRINT VALUE ERROR IF INVALID INPUT IS GIVEN"""

from tkinter import *
import math
class MyWindow:
    def __init__(self, win):
        self.lb11 = Label(win, text="First Number")
        self.lb12 = Label(win, text="Second Number")
        self.lb13 = Label(win, text="Result")
        self.t1 = Entry()
        self.t2 = Entry()
        self.result_label = Label(win, text="")  # Changed to Label for result
        
        self.lb11.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lb12.place(x=100, y=100)
        self.t2.place(x=200, y=100)

        self.b1 = Button(win, text='Add', command=self.add)
        self.b2 = Button(win, text='Subtract', command=self.sub)
        self.b3 = Button(win, text='Multiply', command=self.multiply)
        self.b4 = Button(win, text='Sqrt', command=self.calc)

        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.b3.place(x=300, y=150)
        self.b4.place(x=370, y=150)

        self.lb13.place(x=100, y=200)
        self.result_label.place(x=200, y=200)  # Use Label for result

    def add(self):
        self.calculate_add()

    def sub(self):
        self.calculate_subtract()

    def multiply(self):
        self.calculate_multiply()

    def calc(self):
        self.calculate_sqrt()

    def calculate_add(self):
        try:
            num1 = int(self.t1.get())
            num2 = int(self.t2.get())
            result = num1 + num2
            self.result_label.config(text=str(result))
        except ValueError:
            self.result_label.config(text="Invalid input!")

    def calculate_subtract(self):
        try:
            num1 = float(self.t1.get())
            num2 = float(self.t2.get())
            result = num1 - num2
            self.result_label.config(text=str(result))
        except ValueError:
            self.result_label.config(text="Invalid input!")

    def calculate_multiply(self):
        try:
            num1 = float(self.t1.get())
            num2 = float(self.t2.get())
            result = num1 * num2
            self.result_label.config(text=str(result))
        except ValueError:
            self.result_label.config(text="Invalid input!")

    def calculate_sqrt(self):
        try:
            num1 = float(self.t1.get())
            result = math.sqrt(num1)
            self.result_label.config(text=str(result))
        except ValueError:
            self.result_label.config(text="Invalid input!")

window = Tk()
mywin = MyWindow(window)
window.title("Calculator")
window.geometry("500x300+10+10")
window.configure(bg='pink')
window.mainloop()