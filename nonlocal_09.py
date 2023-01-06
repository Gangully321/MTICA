def outer():
    message='Hello World'
    print(message)
    def inner():
        print(message)
    inner()
outer()
