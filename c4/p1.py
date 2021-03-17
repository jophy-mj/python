class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def peri(self):
        return  2*(self.length+self.breadth)
    def area(self):
        a=self.length + self.breadth
        return a
rect1=rectangle(2,2)
rect1.peri()
rect1.area()
print("Perimeter=",rect1.peri())
print("Area=",rect1.area())
rect2=rectangle(3,4)
rect2.peri()
rect2.area()
print("Perimeter=",rect2.peri())
print("Area=",rect2.area())
if  rect1.area() == rect2.area():
    print("The 2 rectangle have same area")
else:
    print("not equal")