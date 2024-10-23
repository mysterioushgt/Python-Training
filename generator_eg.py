#A Sinple generator function

def my_gen():
    n=4
    mylist=[10,3,45,8,7,24,6,15,82,19,37]
    print("first 4 numbers ")
    #Generator function contains yield statements
    newlist=mylist[:n]
    yield newlist
    
    newlist =mylist[n:n+4]
    yield newlist
    
    n+=1
    print('this is printed at last')
    yield n
    
next(my_gen()) 