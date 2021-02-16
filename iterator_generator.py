def factorial(): 
    a = 0
    b = 1
    while True:
        yield a
        a = b
        b = a+b
    


if __name__ == '__main__':
    
    #iterable/iterator
    l = [1,2,3,4,5]
    try:
        print(next(l))
    except:
        print("Not an iterator")
    
    i = iter(l)
    print(next(i))
    print(next(i))

    #generator
    print(type(factorial()))
    
    for i in factorial():
        print(i)
        if i>100:
            break