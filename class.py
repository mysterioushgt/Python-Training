#BOOK CLASS

class Book:
    # def __init__(myself):  #Constructor make to do not enter again again publisher name
    #     myself.pubname="Rupa Publishers"
       
    def __init__(myself,pname="Rupa Publishers"):    #Parameterised constructor
         myself.pubname=pname
        
    def EnterDetail(myself):  #Enterdetail ---member function1(function name)
        status ="Book Details" #Local Variable
        myself.bookname=input("Enter Book name : ").upper().strip()  # bookname,author---member variables
        myself.authorname=input("Enter author name : ").upper().strip()
        myself.price=int(input("Enter Price : "))
        # myself.pubname=input("Enter Publisher name : ").upper().strip()
        myself.nppages=int(input("Enter No of pages : "))
        
    def ShowDetail(myself):
        print("Book Name =" ,myself.bookname)
        print("Author Name =" ,myself.authorname) 
        print("Price =" ,myself.price) 
        print("Publisher name =" ,myself.pubname) 
        print("No of pages =" ,myself.nppages)     
        
    def StoreFile(myself):
        try:
            fvl =open("C:\\ITMGWL\\itmgwl.Csv","a")
            data =myself.bookname+","+ myself.authorname+","+str(myself.price)+","+myself.pubname+","+str(myself.nppages)+"\n"
            fvl.write(data)  # write---to save the content in the file
            print("Record Added Successfully !!")
            fvl.close()  # close-- to close the file which was open earlier
        except PermissionError:
            print("Sorry Permission Denied..")
        except FileNotFoundError:
            print("Sorry Please check File path or check if file is open")  
        finally:
            print("File Processed")      
book1 =Book()  # Object We are Creating ,book1 is a object and Book is a class name
book1.EnterDetail()  #Book.EnterDetail(book1)
book1.ShowDetail()  
book1.StoreFile()      
book2=Book("Penguine Publishers")
book2.EnterDetail()
book2.ShowDetail()
book2.StoreFile()

del book1,book2