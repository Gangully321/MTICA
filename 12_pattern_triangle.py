##output:
##Enter number of row: 5
##    *
##   ***
##  *****
## *******
##*********
##

def ganesh(g):
   for i in range(g):
      print(" " * (g-i-1) + '*' * (2*i+1))
g=int(input())
ganesh(g)
