def checkpalindrome(a):
    if a==a[::-1]:
        return 'yes'
    return 'no'
inp=input()
print(checkpalindrome(inp))
