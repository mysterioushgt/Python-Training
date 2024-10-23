#Using Numpy For Statistical Operations

import numpy
from scipy import stats

pricelist =[56,89,23,35,35,35,60,62,60,60,72,60,210,124]
pricelist.sort()
print("Original Price values are")
print(pricelist)
meanprice=numpy.mean(pricelist)
print("Mean Price =%.2f" %(meanprice))

medianprice =numpy.median(pricelist)
print("Median Price =%.2f" %(medianprice))
stdprice1=numpy.std(pricelist)
print("Standard Deviation of Price =%.2f" %(stdprice1))

x=stats.mode(pricelist)
print("Mode =" ,x)