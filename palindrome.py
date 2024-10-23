str=input("enter any string").strip().upper()

if(str==str[::-1]):
    print("palindrome")
else:
    print("no")