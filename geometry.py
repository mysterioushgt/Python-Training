#CREATING OUR OWN MODULE
# def is the first keyword to define function stands for "define"
def CircleArea():
    radius =float(input("enter the Radius : "))
    area=3.14*radius*radius
    print("area of circle = %.2f" %area)
    
def RectangleArea(length,breadth):
    area=length*breadth
    print("area of rectangle = %d "%area)   
    
def TriangleArea(base,height):
    area=0.5*base*height
    # print("area of triangle =%.2f" %area)   
    return area
    
def RhombusArea():
    pass    
