webinarList=["milan.k@orange.com" ,"amit.m@orange.com","rajat.s@bts.in","gaurav.s@orange.com",
             "jedenak.v@colt.net","audra.s@orange.com","mellisa.t@hp.com"]
orangepeople =lambda x:x.endswith("@orange.com")
outsidepeople=lambda y:not y.endswith("@orange.com")

orangeList=list(filter(orangepeople,webinarList))
outsider= list(filter(outsidepeople,webinarList))

print("people attended from orange")
print(orangeList)
print("people from outside orange")
print(outsider)        