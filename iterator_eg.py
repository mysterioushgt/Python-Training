#Initialize the list

import sys  #sys is a modeule
my_list =[2,1,3,6,10]

a=(x**2 for x in my_list) # a is iterator

if(next(a) >=3):
    sys.exit()  #you can forcefully close the program
    
print(list(a))    
print(type(a))    