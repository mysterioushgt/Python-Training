# File Operations

import os
path ="C:\\ITMGWL\\itmgwl.txt"
size=os.path.getsize(path)
print("total size of the file = %d" %size)

#Coding for calculating lines in a file
fvl=open("C:\\ITMGWL\\itmgwl.txt","r")
data =fvl.read()
print("File content shown below")
print(data)
lines=data.split("\n")
print("total no of lines =" ,len(lines))