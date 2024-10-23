#  YOU HAVE TO CREATE A CLASS SAY FURNITURE WHICH CONTAINS THE FOLLOWING INFORMATIONS--
# FurnitureName , Color , Material ,Price
# Implement 2 member function - say GetDetail() and DisplayDetail() to enter and show the above informations

# Implement Constructor and Initialize Material as Wooden
import os
get_file_size=lambda file_path:os.path.getsize(file_path) if os.path.exists(file_path) else 0

class Furniture:
    
    def __init__(myself):
        myself.material= "Wooden"
        
    def GetDetail(myself):
        myself.Furniturename =input("Enter the furniture name : ").upper().strip()
        myself.color=input("Enter the colour : ").upper().strip()
        # myself.material =input("Enter the material : ").upper().strip()
        myself.price =int(input("enter price :"))
        
        
    def DisplayDetail(myself):
        print("Furniture name : " ,myself.Furniturename) 
        print("color name : " ,myself.color)
        print("material name : " ,myself.material) 
        print("Price: " ,myself.price)        
        
    def StoreDetail(myself):
        fvl=open("C:\\ITMGWL\\Furniture.Csv","a")
        data =myself.Furniturename+","+ myself.color+","+str(myself.price)+","+myself.material+"\n"
        fvl.write(data)  # write---to save the content in the file
        print("Record Added Successfully !!")
        
        # For counting the lines in the file
        fvl=open("C:\\ITMGWL\\Furniture.Csv","r") 
        data =fvl.read()   
        lines=data.split("\n")
        print("total no of lines =" ,len(lines)-1) 
    
        fvl.close()  # close-- to close the file which was open earlier
        
        size =get_file_size("C:\\ITMGWL\\Furniture.Csv") 
        print("the size of the file : ",size)
        # path ="C:\\ITMGWL\\Furniture.Csv"
        # size=os.path.getsize(path)
        # print("total size of the file = %d" %size)
        
    # def CountLine(myself):
    #     fvl=open("C:\\ITMGWL\\Furniture.Csv","r") 
    #     data =fvl.read()   
    #     lines=data.split("\n")
    #     print("total no of lines =" ,len(lines)-1)  
    #     fvl.close() 
     
        
Furniture1=Furniture()
Furniture1.GetDetail()
Furniture1.DisplayDetail()
Furniture1.StoreDetail()  
