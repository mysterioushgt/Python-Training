"""square =[k*k for k in range(1,11)]
print(square)"""


#LIST COMPREHENSION USING NESTED IF::

"""Numlist=[y for y in range(1,21)if y%2==0 if y%5==0]
print(Numlist)"""


#LIST COMPREHENSION USING NESTED FOR::
i=0
matrix=[[1,2],[3,4],[5,6]]
Trmatrix =[[row[i] for row in matrix]for y in range(0,3)]
print(Trmatrix)           
#the above code will produce transpose matrix of the original one.