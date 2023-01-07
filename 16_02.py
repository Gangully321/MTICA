def removeSpecialchar(s):
    ans=''
    for i in s:
        if ord(i) in range(65,91) or ord(i) in range(97,123)or ord(i) in range(48,57):
            ans+=i
    return ans


inp=input()
print(removeSpecialchar(inp))
