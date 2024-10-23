import pandas
import math
mydata = pandas.read_excel("C:\\Users\\ProBook\\Downloads\\loan.xls")
print(mydata)

max_loan = mydata['Loan Amount'].max()
min_loan = mydata['Loan Amount'].min()
avg_loan = mydata['Loan Amount'].mean()


print(f"Maximum Loan Amount: {max_loan}")
print(f"Minimum Loan Amount: {min_loan}")
print(f"Average Loan Amount: {avg_loan}")