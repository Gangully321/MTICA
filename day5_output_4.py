def anagram(g1,g2):
    if sorted(g1)==sorted(g2):
        return 'yes'
    return 'no'
inp=input('enter your string:').split()
print(anagram(inp[0],inp[1]))
