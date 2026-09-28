from abc import ABC,abstractmethod

#abstract class 
class shape(ABC):
    @abstractmethod
    def area(self):
        pass   #JUST DECLEARTION NOT IMPLEMENTATION
class Rectangle(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
rect=Rectangle(3,5)
print("Area of rectangle:",rect.area())
            