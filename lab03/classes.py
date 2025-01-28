# class MyClass:
#     def __init__(self):
#         self.text = ""

#     def getString(self):
#         self.text = input("Enter a string: ")

#     def printString(self):
#         print(self.text.upper())

# obj = MyClass()
# obj.getString()
# obj.printString()



# class Shape:
#     def area(self):
#         return 0

# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

#     def area(self):
#         return self.length * self.length

# square = Square(6)
# print(square.area())  



# class Shape:
#     def area(self):
#         return 0  

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         super().__init__()  
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width


# rect = Rectangle(27, 6)
# print(rect.area())  



# import math

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def show(self):
#         print(f"Point coordinates: ({self.x}, {self.y})")

#     def move(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y

#     def dist(self, other_point):
#         return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


# p1 = Point(1, 2)
# p2 = Point(4, 6)

# p1.show()  
# p1.move(3, 5)
# p1.show()  
# print(p1.dist(p2))  



