class Point():
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def show(self):
        print(f"x1 coordinate is {self.x1} \ny1 coordinate is {self.y1}")
        print(f"x2 coordinate is {self.x2} \ny2 coordinate is {self.y2}")
    def move(self):
        self.x1 = int(input('new x1 coordinate: '))
        self.y1 = int(input('new y1 coordinate: '))
        self.x2 = int(input('new x2 coordinate: '))
        self.y2 = int(input('new y2 coordinate: '))
    def distance(self):
        self.distance = ( ( (self.x1-self.x2) ** 2 ) + ( (self.y1-self.y2) ** 2) ) ** 0.5
        print(f'distance is {self.distance}')
obj = Point()
obj.show()
obj.move()
obj.distance()