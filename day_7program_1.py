#use a dictionary comprehrsion
#to count the length of each word in a sentence


string=''' hai guys freshes function eppudu plan chedam.'''

wordslst=string.split(' ')
print(wordslst)
wordslst=[i.strip("\n")for i in wordslst]
print(wordslst)
ans={i:len(i) for i in wordslst}
print(ans)


