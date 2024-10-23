import pandas
mydata = pandas.read_csv("C:\\ITMGWL\\College.Csv")
print(mydata)
coursename= set(mydata["Course"])
print(coursename)