# FUNCTION TESTING

import geometry
print("Calculating area of circle")
geometry.CircleArea()

print("Calculating area of rectangle")
rlen=float(input("enter length "))
rbre=float(input("enter breadth "))
geometry.RectangleArea(rlen,rbre)


print("calculating area of triangle")
base=float(input("enter base"))
height = float(input("enter height"))
rarea =geometry.TriangleArea(base,height)
print("area of triangle = %.2f" %rarea)