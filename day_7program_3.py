#use a nested list comprehesion
#to find all the numbers from 1-100
#are divisible by any single digit excluding 1
#that are divisible by 2 or 3 or  4.....or 9

# method-1
lst=[]
for i in range(1,101):
    if i%2==0 or i%3==0 or i%4==0 or i%5==0 or i%6==0 or i%7==0 or i%8==0 or i%9==0:
        lst.append(i)
print(lst)


#method-2

lst=[]
for i in range(1,101):
    for  j in range(2,10):
        if i%j==0:
            lst.append(i)
            break
print(lst)


#method-3


lst=[i for i in range(1,101) if i%2==0 or i%3==0 or i%4==0 or i%5==0 or
     i%6==0 or i%7==0 or i%8==0 or i%9==0]
print(lst)


method-4

lst={i for i in range(1,101)for  j in range(2,10)if i%j==0}
print(lst)







