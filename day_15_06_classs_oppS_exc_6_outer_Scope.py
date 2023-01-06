message ='outer scope'
def outer():
    message='demo'
    print(message)
    def inner():
        nonlocal message
        message='inner scope'
        print(message)
    inner()
    print(message)

outer()
