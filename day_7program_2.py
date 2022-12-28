#use a dictionary comprehrsion
#to count the length of each word in a sentence and reverse the words


string=''' hai guys freshes function eppudu plan chedam.'''

wordslst=string.split(' ')
print(wordslst)
wordslst=[i.strip("\n")for i in wordslst]

ans={i:i[::-1] for i in wordslst}
print(ans)


