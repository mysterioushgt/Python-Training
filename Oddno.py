#ITERATOR EXAMPLE:::

class Counter:
    def __init__(self,low,high):
        self.current =low  # current is member variable and self is a object
        self.high =high  
        
    def __iter__(self):
        return self  # self is return (object)
    
    def __next__(self):
        if self.current>self.high:
            raise StopIteration
        else:
            self.current +=1
            return self.current -1
        
counter = Counter(1,5)
for number in counter:
    if(number%2!=0):
         print(number)         