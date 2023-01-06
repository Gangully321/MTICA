def outer():
    message='Hello World'
    print(message)
    def inner():
        nonlocal message
        message='Im Arun'
        print('inner : ',message)
    inner()
    print('outer : ',message)
                                        
outer()
