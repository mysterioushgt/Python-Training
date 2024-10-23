myno =int(input("enter your number"))
result1=myno %5
result2 = myno %8

if(result1==0 and result2 ==0):
    print("%d is divisible by both 5 and 8" %myno)
elif(result1!=0 and result2==0):
    print("%d is divisible by 8 but not by 5 " %myno)    
elif(result1==0 and result2!=0):
    print("%d is divisible by 5 but not by 8 " %myno)    
elif(result1!=0 and result2!=0):
    print("%d is not divisible by 5 and 8 " %myno)   

print("program ended") 