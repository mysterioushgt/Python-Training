#Validation IP ADDRESS

# this code is not validating either it is valid ip address or not
"""serverip= input("enter the IP Address of the Server :").strip()
octalist =serverip.split(".")
print("Octals Are :")
for x in octalist:
    print(x)
"""

# this code is validating either it is valid ip address or not
import ipaddress
try:
    pp=ipaddress.ip_address(input("Enter Valid IP Address : "))
    
    print("IP Address Obtained : " +str(pp))
    col=str(pp).split(".")
    print("List of octats are")
    for x in col:
        print(x)
except ValueError:
    print("INVALID IP ADDRESS")        