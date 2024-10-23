"""Q-YOU are supposed to enter the detail of some items like--
ItemName,Qty,Price
Note: Qty & Price can not be 0 or -ve in case you enter any such values then immediately
WrongValueError(An user Defined Exception should be generated)"""

answer="Y"
class QTYException(Exception):
    pass
class PriceException(Exception):
    pass
while(answer=="y" or answer=="Y"):
    try:
        while(True):
          ItemName=input("enter the item name : ").upper().strip()
          if(len(ItemName)==0):
             print("sorry....item Name should not be Blank....Try Once Again")
             continue
          else:
             break
    
        while(True):
          qty =int(input("enter quantity : "))
          if(qty<=0):
            raise QTYException()
          else:
            break
        
        
        while(True):
          Price=int(input("Enter Price : "))
          if(Price<=0):
            raise PriceException()
          else:
            break
        
     
        print("INAME\t\tQTY\t\tPRICE")
        print("****\t\t******\t\t********")
        print("%s\t\t%d\t%d" %(ItemName,qty,Price))   
        
    except ValueError:
       print("Salary is not proper...please renter")
       continue   
    
    except QTYException:
        print("Sorry Quantity can not be less than 0") 
        
    except PriceException:
        print("Sorry Price can not be less than 0")     
        
    finally:
        print("Thanks")       
        
        