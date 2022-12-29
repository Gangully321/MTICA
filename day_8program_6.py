num1=int(input("enter a number :"))
num2=int(input("enter a number :"))

try:
    res=num1/num2 #executed with num2=non zero and zero
except ZeroDivisionError:
    print("division by zero not allowed")
else:
    print(num1,'/',num2,'/',res)
print('thanks')
