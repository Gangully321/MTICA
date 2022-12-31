#file handling (append data)
fo=open(r"C:\Users\User\Desktop\DEG1.txt","w")
for i in range(5):
    inpstr=input("enter string:")
    fo.write(inpstr+'\n')
fo.close()
print('written to file')
