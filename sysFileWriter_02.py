import sys
print('coming from stout')
save_stdout=sys.stdout
fh=open(r'D:\Arun1.txt','w')
sys.stdout=fh
print('this line goes to Arun1.txt')
print(input())
sys.stdout=save_stdout
fh.close()
