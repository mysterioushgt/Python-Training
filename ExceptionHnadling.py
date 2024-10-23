#EXCEPTION HANDLING

try:
    firstno= int(input("Enter the first no : "))
    secondno= int(input("Enter the second no : "))
    result =firstno/(secondno-3)
    print("Total =",result)
    
except ValueError:   #ValueError--Exception Error
    print("Input Data should be Number Only...Enter correct Data")    
    
except ZeroDivisionError:  #ZeroDivisionError--Exception Error
    print("Division By 0 is Not Possible...")    

except Exception as K:
    print("Sorry ...Exception Raised..."+K)
    
finally:
    print("thanks... program ended")    