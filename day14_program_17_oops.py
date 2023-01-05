class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __del__(self):
        class_name=self.__class__.__name__
        print(class_name,"destroy")


#python shell
##
##pt1=Point()
##pt2=pt1
##pt3=pt1
##print(id(pt1),id(pt2),id(pt3))
##1563712933840 1563712933840 1563712933840
##del pt1
##del pt2
##del pt3
##Point destroy
##pt11=Point(6,7)
##del pt11
##Point destroy
