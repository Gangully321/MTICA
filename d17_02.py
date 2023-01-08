import sys
print(sys.argv)
for i in range(len(sys.argv)):
    if i ==0:
        print("function name:{0}".format (sys.argv[0]))
    else:
        print("{0}.argument:{1}".format(i,sys.argv[i]))
