def factorial(n):
    #base case:if n is 0,return 1
    if n==0:
        return 1
    #recursive case: n*factorial of(n-1)
    else:
        return n*factorial(n-1)
    
print(factorial(5))    