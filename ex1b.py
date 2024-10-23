# USING ANOTHER FORM
answer ="Y"

while True:
   empname=input("enter the employee name :").upper().strip()
   if(len(empname)==0):
       print("sorry....Emp Name should not be Blank....Try Once Again")
       continue

   else:
       print("salary getting processed")
       break
while True:   
  salary = int(input("enter the salary :"))
  if(salary>=25000):
      break
  else:
      print("improper salary....")
      continue
while True: 
  emailId =input("enter Official Mail ID : ").lower().strip()
  if(len(emailId)!=0 and emailId.endswith("@itmgoi.in")):
      break
  else:
      print("not a valid email id")

print("NAME\t\tSALARY\t\tEMail ID")
print("****\t\t******\t\t********")
print(empname+"\t\t" +"%.2f\t%s" %(salary,emailId))

print("Salary Slips Generated")        