def demo_yield():
    print("code segment1 execited")
    x=7
    yield x*x
    print("code segment2 execited")
    yield 2
    print("code segment1 execited")
    yield 3
    print("code segment4 execited")
    
