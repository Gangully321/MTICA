#super refers to the parent class.
class A:
    def first_Method(Self):
        print("method of class A.....")
class B(A):
    def first_Method(Self):
        print("method of class B.....")
        super().first_Method()#calls the first_Method of the superclass "A"

ob=B()
ob.first_Method()
