lst_even=[]
lst_odd=[]
while(True):
    inp=int(input("enter a value(0 to end)"))
    if inp==-1:
        break
    if inp%2==0:
        lst_even.append(inp)
    else:
        lst_odd.append(inp)
lst_even.sort()
lst_odd.sort()
print("EVEN:",*lst_even)
print("min",lst_even[0])
print("max",lst_even[-1])
print("avg",round(sum(lst_even)/len(lst_even),1))
print("ODD:",*lst_odd)
print("min",lst_odd[0])
print("max",lst_odd[-1])
print("avg",round(sum(lst_odd)/len(lst_odd),1))
