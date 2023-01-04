def sunday():
    print('sunday')
def monday():
    print('Monday')
def tuesday():
    print('Tuesday')
def wedensday():
    print('Wedensday')
def thursday():
    print('Thursday')
def friday():
    print('Friday')
def saturday():
        print('Saturday')
Days={1:sunday,2:monday,3:tuesday,4:wedensday,5:thursday,6:friday,7:saturday}
inp=int(input())
if Days>=1 and Days<=7:
    Days[inp]()
else:
    print('Invalid')
