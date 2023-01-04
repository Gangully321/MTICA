def calculateCubic():
    i=1;
    while True:
        yield i*i*i
        i +=1
for num in calculateCubic():
    if num > 1000:
        break
    print(num)
