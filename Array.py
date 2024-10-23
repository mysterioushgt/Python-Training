#CREATING TWO DIMENSIONAL ARRAY

import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[0,-4,4],[3,2,9]])
print("Array Detail")
print(arr1)
print("Dimension of Array is =%s" %(arr1.ndim))

print(arr2)
print("Dimension of Array is =%s" %(arr2.ndim))

arr3=arr1+arr2
print("Result Array = ")
print(arr3)

arr4=np.array([[3,0],[4,-1],[0,1]])
arr5=arr1.dot(arr4)
print("Result after Multiplication=")
print(arr5)

arr6=arr1-arr2
print("result after sbtraction := ")
print(arr6)