class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter()")



class Rectangle(Shape):
    def __init__(self, length, width):
        
        self.__length = length
        self.__width = width

   
    def get_length(self):
        return self.__length
    
    def set_length(self, length):
        if length > 0:
            self.__length = length
        else:
            print("Length must be positive!")

    def get_width(self):
        return self.__width
    
    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            print("Width must be positive!")

    
    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)



class Square(Rectangle):
    def __init__(self, side):
       
        super().__init__(side, side)

    
    def area(self):
        return self.get_length() ** 2

    
    def perimeter(self):
        return 4 * self.get_length()


shapes = [Rectangle(10, 5),Square(6)]

for shape in shapes:
    print(f"{shape.__class__.__name__} → Area: {shape.area()}, Perimeter: {shape.perimeter()}")