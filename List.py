# str=["saloni","garg","gopal pura","8085565703"]
# print(type(str))

techcourse=["Power BI","AWS","MS SQL Server","Python","Github","Ansible","Tableau"]
ecourse=["Soft skills","Project Management","Crisis Management","Customer Handling"]

allcourse =techcourse+ecourse

print("list of all courses:")

allcourse.append("cybersecrity")  # append insert at the end of the memory
allcourse.insert(2,"snowflakes") # it insert at index 2
allcourse.remove("Github")   #to remove any object from memory
allcourse.sort()  #to sort the elements of a list

for x in allcourse:    # x is iterator and in is a membership operator
    print(x)
print("total Courses :" , len(allcourse))


#script to search a particular course
course=[]  # a blank list will be formed
for x in allcourse:
    course.append(x.upper())
cname=input("enter course to search ?").upper().strip()
if cname in course:
    print("%s is available in list" %cname)
else:
    print("%s is not available in the list" %cname)    
    
#to remove any object from memory    
del techcourse,allcourse   