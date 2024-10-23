# Create a decorator function that logs when say hello() is called.

def my_decorator(func):
    def wrapper():
        print("before the function is called.")
        func()
        print("after the function is called.")
    return wrapper

@my_decorator   #Decorator is being used

def say_hello():
    print("Hello")
    
say_hello()        