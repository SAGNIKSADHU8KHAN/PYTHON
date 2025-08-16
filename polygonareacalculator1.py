from abc import ABC, abstractmethod


class Shape(ABC):
    
    def area(self):
        pass

    
    def perimeter(self):
        pass



class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side) 


rect = Rectangle(10, 5)
sq = Square(6)

print("Rectangle Area:", rect.area())
print("Rectangle Perimeter:", rect.perimeter())

print("Square Area:", sq.area())
print("Square Perimeter:", sq.perimeter())