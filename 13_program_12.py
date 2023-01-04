#solution : Generating odd numbers by pipelining generators
def gen_int(n):
    for i in range(n):
        yield i

def gen_2(gen):
    for n in gen:
        if n % 2:
            yield n

for i in gen_2(gen_int(10)):
    print(i)
