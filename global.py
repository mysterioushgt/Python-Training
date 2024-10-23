y=20 #Global variable
print(f"Initially value of y ={y}")
def modify_global_variable():
    global y
    y=30 # Modify the global variable
    print(f"inside function , y={y}")
    
modify_global_variable()
print(f"outside function , y ={y}")    