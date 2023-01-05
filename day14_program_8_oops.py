#Inheritance from more than one base class
class A:
    def first_Method(Self):
        print("method of class A.....")
class B:
    def second_Method(Self):
        print("method of class B.....")
class C(A,B):
    def third_Method(Self):
        print("method of class C.....")

if __name__=='__main__':
    ob=C()
    ob.first_Method()
    ob.second_Method()
    ob.third_Method()
   # C().third_Method()
#Circular inheritance is not possible...
