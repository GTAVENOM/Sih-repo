class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1=Point(10,20)
print(f'x:{point1.x}, y:{point1.y}')