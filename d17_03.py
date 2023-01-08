import sys

print("comming through stdout")

save_stdout=sys.stdout
fh=open(r"C:\Users\User\Desktop\DEG.txt","w")
sys.stdout=fh
print("this line goes to test.txt")
print(input())
sys.stdout=save_stdout
fn.close()
