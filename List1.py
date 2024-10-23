webinarList=["milan.k@orange.com" ,"amit.m@orange.com","rajat.s@bts.in","gaurav.s@orange.com",
             "jedenak.v@colt.net","audra.s@orange.com","mellisa.t@hp.com"]
orangeList=[]
outsider=[]
for x in webinarList:
    if(x.endswith("@orange.com")):
        orangeList.append(x)
    else:
        outsider.append(x)    
print("people attended from orange")
print(orangeList)
print("people from outside orange")
print(outsider)        