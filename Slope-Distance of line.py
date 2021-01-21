# Calculating the ditance and slope of the line connecting point 1 (coor1) to point 2 (coor 2)
# Step 1: Define Line class
class Line(object):

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1)/(x2 - x1)

# Step 2: Define instance object by inserting the points coordinates
print("Enter two points: (x1, y1) and (x2, y2) \n")
x1 = int(input("Enter x1: \n"))
y1 = int(input("Enter y1: \n"))
x2 = int(input("Enter x2: \n"))
y2 = int(input("Enter y2: \n"))


connectingline = Line((x1, y1), (x2, y2))

print(f"The distance between points is {connectingline.distance()}\n")
print(f"The slope of the line connecting the points is {connectingline.slope()}\n")
