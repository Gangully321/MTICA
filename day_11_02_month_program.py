months={'1:january','2:February','3:march',
'4:April','5:May','6:June','7:July','8:August',
'9:September','10:October','11:November','12:December',}



n=int(input())
for count in range(n):
    mn=int(input())
    if mn>=1 and mn<=12:
        print(months[mn])
    else:
        print("Invalid")

