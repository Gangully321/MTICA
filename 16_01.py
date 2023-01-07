for x in it:
    print(x,end=" ")
##or using next() function
import sys
while True:
    try:
        print(next(it))
    except StopIteration as ob:
        print(ob)
        break
    #sys.exit()
    #you have to import sys module for this
