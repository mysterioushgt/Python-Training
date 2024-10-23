import pandas as pd  # pd is a nickname given for pandas
from collections import Counter # counter is a module in the package collections
vegetables=["Potato","Brinjal","Cauli Flower","Onion","Beans","Cabbage","Brinjal","Red Beans","Beans",
            "Ginger","Lemon","Onion"]

# notduplicate=set(vegetables)
# list=list(notduplicate)
# list.sort()
# print(list)


#DataFrame:-to organise in a tabular form either in row or column form
mydata=pd.DataFrame.from_dict(Counter(vegetables).items())
print(mydata)