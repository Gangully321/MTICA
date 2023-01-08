import sys
print(sys.argv)
for i in range(len(sys.argv)):
    if i==0:
        print('Function name: {0}'.format(sys.argv[0]))
    else:
        print('{0}. argumunt : {1}'.format(i,sys.argv[i]))
