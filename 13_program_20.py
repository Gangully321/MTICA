a=-1
b=9
try:
    #condition for checking negative values
    if a < 0 or b<0:
        #raising exception using raise keyword
        raise ZeroDivisionError
    print(a/b)
except ZeroDivisionError:
    print("please enter valid integer values")
