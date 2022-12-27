import time
inp=int(input("enter a no:"))
start=time.time()
for i in range(inp):
    print("i=",i,"i^2=",i*i)
print("time taken by loop:",(time.time()-start)*100000)
