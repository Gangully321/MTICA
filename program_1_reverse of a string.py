def string(s):
    ans=[i[::-1]for i in s]
    return ans
inp=input().split()

print(*string(inp))

##
##inp=input().split()
##print(*(inp))

