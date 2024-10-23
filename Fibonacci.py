#Example :Fibonacci Sequence
def fibonacci(n):
    a,b=0 ,1
    while a<n:
        yield a  #Yield is a generator it basically returns the current value
        a,b=b,a+b
        
fib =fibonacci(10)
for num in fib:
    print(num)  #Output : 0 1 1 2 3 5 8        