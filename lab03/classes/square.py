class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2


length = float(input("Enter the side length of the square: "))
square = Square(length)

print(f"The area of the square is: {square.area()}")