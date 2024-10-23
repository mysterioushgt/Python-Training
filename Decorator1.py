#Decoratord work on Functions speciality is that using it you can return a function

"""Associating decorator with a function

Defining my_decorator for a function"""

def mydecorator(func): #func = sayhello
    def wrapper():
        
        func()
        print("Good morning")
        print("Have a nice Day")
        
    return wrapper

@mydecorator
def sayhello():
    print("hello Friends")
sayhello() # here the function sayhello() is being called        
    