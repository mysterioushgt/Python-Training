answer ="Y"
empname=input("enter the employee name :").upper().strip()
if(len(empname)==0):
    print("sorry....Emp Name should not be Blank....Try Once Again")

else:
    print("salary getting processed")
salary = int(input("enter the salary :"))
emailId =input("enter Official Mail ID : ").lower().strip()

print("NAME\t\tSALARY\t\tEMail ID")
print("****\t\t******\t\t********")
print(empname+"\t\t" +"%.2f\t%s" %(salary,emailId))

print("Salary Slips Generated")        