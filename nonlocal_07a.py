def myfunc1():
    x='John'
    def myfunc2():
        nonlocal x
        x='hello'
    myfunc2()
    return x
print(myfunc1())
