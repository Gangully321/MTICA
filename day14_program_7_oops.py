#Indirect inheritance or multilevel inheritance
class A:
    def first_Method(Self):
        print("print of method of class A.....")
class B(A):
    def second_Method(Self):
        print("print of method of class B.....")
class C(B):
    def third_Method(Self):
        print("print of method of class C.....")

if __name__=='__main__':
    ob=C()
    ob.first_Method()
    ob.second_Method()
    ob.third_Method()
    C().third_Method()
#Circular inheritance is not possible...
