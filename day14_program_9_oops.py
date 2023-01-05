#Indirect Inheritance or multilevel inheritance
class A:
    def first_Method(Self):
        print("method of class A.....")
class B:
    def first_Method(Self):
        print("method of class B.....")
class C(B,A):#B,A
    def third_Method(Self):
        print("method of class C.....")
        #super().first_method()

if __name__=='__main__':
    ob=C()
    ob.first_Method()
    ob.third_Method()
   # C().third_Method()
#Circular inheritance is not possible...
