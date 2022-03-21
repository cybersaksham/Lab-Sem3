class Shape:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def perimeter(self):
        return self.a + self.b + self.c + self.d

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width, length, width)
    
    def area(self):
        return self.a * self.b
    
    def perimeter(self):
        return super().perimeter()

class Square(Shape):
    def __init__(self, side):
        super().__init__(side, side, side, side)
    
    def area(self):
        return self.a * self.b
    
    def perimeter(self):
        return super().perimeter()

class Trapezium(Shape):
    def __init__(self, a , b, c, d, h):
        super().__init__(a, b, c, d)
        self.h = h
       
    def area(self):
        return ((self.a + self.c) * self.h) / 2

    def perimeter(self):
        return super().perimeter()
       

   
s1 = Rectangle(10, 5)
print(s1.area(), s1.perimeter())

s2 = Square(10)
print(s2.area(), s2.perimeter())

s3 = Trapezium(10, 20, 5, 10, 15)
print(s3.area(), s3.perimeter())
