#Consider the following list--
# SampleNos =[24,67,36,20,56,81,49,39,25]

# Implement a function so that the whole list can be passed as a parameter and we can calculate 
# the square root of all the no.s

import math

"""def squareroot(sample_nos):
    return [math.sqrt(num) for num in sample_nos]
    
    
SampleNos =[24,67,36,20,56,81,49,39,25]

squareroots = squareroot(SampleNos)
print(squareroots)
"""

# using lambda and map
SampleNos =[24,67,36,20,56,81,49,39,25]
mylambda =lambda x: math.sqrt(x)
result =map(mylambda,SampleNos)
print(list(result))

