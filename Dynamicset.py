# 3 FOR EXAMPLE SOMETIMES WE HAVE TO MAKE A DYNAMIC set

countrylist =set()  # this is going to create a blank set
while True:
    cname=input("Enter the country name : ").upper()
    countrylist.add(cname)
    answer =input("Want to add another country name ?").upper().strip()
    if(answer=="Y"):
        continue
    else:
        break
    
print("List of Countries : ")
for x in countrylist:
    print(x)    