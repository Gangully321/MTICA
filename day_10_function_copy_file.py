#file handling (copy)

f01=open(r"C:\Users\User\Desktop\DEG1.txt","r")
f02=open(r"C:\Users\User\Desktop\hey","w")

temp=f01.read()
f02.write(temp)
f01.close()
f02.close()
print('file copied')
