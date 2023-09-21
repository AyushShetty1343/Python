#7a
import math
class shape:
    def area(self):
        pass
class triangle(shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5*self.base*self.height

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
    
class rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
tri=triangle(5,10)
cir=circle(3)
rect=rectangle(4,6)
print("area of triangle= ",tri.area())
print("area of circle= ",cir.area())
print("area of rectangle= ",rect.area())