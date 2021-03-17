class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def __lt__(self):
        if rect1<rect2:
            print("second rectangle is greater than first!")
        else:
            print("first rectangle is greater than second")
obj1=rectangle(2,4)
obj2=rectangle(3,4)
print("Area of rectangle1:",obj1.area())
print("Area of rectangle1:",obj2.area())
rect1=obj1.area()
rect2=obj2.area()
rect=rectangle(rect1,rect2)
rect.__lt__()