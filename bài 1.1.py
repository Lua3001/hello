import math
class Point:
    def __int__(self, x=0, y=0):
        self.x = x
        self.y = y
    def read(self):
        line = input().strip().split()
        self.x = int(line[0])
        self.y = int(line[1])
    def print(self):
        print(f"({self.x}, {self.y})")
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def GetX(self):
        return self.x
    def GetY(self):
        return self.y
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)
    def distance(self, P):
        dx = self.x - P.getX()
        dy = self.y - P.getY()
        return math.sqrt(dx**2 + dy**2)
