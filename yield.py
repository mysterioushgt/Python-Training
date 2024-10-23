def mygenerator():
    print("First item")
    yield 10
    
    print('Second item')
    yield 20
    
    print('last item')
    yield 30
    
try:
    output1=mygenerator()
    print(next(output1))
    print(next(output1))
    print(next(output1))
    print(next(output1))
    
except StopIteration:
    print("ALL RESULTS DISPLAYED")        