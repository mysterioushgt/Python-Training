def local_scope_example():
    x=10 #Local Variable
    print(f"inside function , x= {x}")
    
local_scope_example()
print(x)   # this will raise a nameerror because x is not defined outside the function
    