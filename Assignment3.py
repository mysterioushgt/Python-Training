"""USING THE CONCEPT OF GENERATOR EVALUATE:--
1+4+9+16+25=?"""

def Squarerrot(n):
   for i in range(1,n+1):
       yield i*i
       
Squar_root=sum(Squarerrot(5))
print(Squar_root)       
       