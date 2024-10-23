from tkinter import *
import math
class MyWindow:
    def __init__(self,win):
        self.lbl1=Label(win,text='First number')
        self.lbl2=Label(win,text='Second number')
        self.lbl=Label(win,text='Result')
        self.t1=Entry()
        self.t2=Entry()
        self.t3=Entry()
        
        self.lbl1.place(x=100,y=50)
        self.t1.place(x=200,y=50)
        self.lbl2.place(x=100,y=100)
        self.t2.place(x=200,y=100)
        self.b1=Button(win,text='Add' ,command=self.add) #Another Approach
        self.b2=Button(win,text='Subtract')
        self.b3=Button(win,text='Multiply')
        self.b4=Button(win,text='Sqrt')
       
        
        self.b2.bind('<Button-1>' ,self.sub) #Old Approach
        self.b1.place(x=100,y=150)
        self.b2.place(x=200,y=150)
        self.b3.place(x=300,y=150)
        self.b4.place(x=370,y=150)
        
        self.b3.bind('<Button-1>' ,self.mul) #Old Approach
        self.b1.place(x=100,y=150)
        self.b2.place(x=200,y=150)
        self.b3.place(x=300,y=150)
        self.b4.place(x=370,y=150)
        
        self.b4.bind('<Button-1>' ,self.calc)
        self.lbl.place(x=100,y=200)
        self.t3.place(x=200,y=200)
        
    def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get()) #To read data from a Text BOX
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END , str(result))  #To display a value within a Text Box
        
    def sub(self,event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get()) 
        num2=int(self.t2.get())    
        result=num1-num2
        self.t3.insert(END,str(result))
          
    def mul(self,event):
        self.t3.delete(0,'end')    
        num1=int(self.t1.get()) #To read data from a Text BOX
        num2=int(self.t2.get())
        result=num1*num2
        self.t3.insert(END , str(result))
        
    def calc(self,event):
        self.t3.delete(0,'end')    
        num1=int(self.t1.get())
        result=math.sqrt(num1)
        self.t3.insert(END ,str(result))
        
        
window =Tk()
mywin=MyWindow(window)
window.title('Hello Python')
window.geometry("500x300+10+10")
window.configure(bg="pink")  #Changing the window Background colour
window.mainloop()        
       