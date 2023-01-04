spins=[('red','23'),('black','13')('red','23'),('red','23'),('red','5'),('red','18'),('black','13'),
       ('red','9'),('black','15')('black','20')],('black','31'),('red','3'),
def countReds(alist):
    count=0
    for color,number in alist:
        if color =='black':
            yield count
            count=0
        else:
            count +=1
    yield count
gaps=[gap for i in countReds(spins)]
print(gaps)
