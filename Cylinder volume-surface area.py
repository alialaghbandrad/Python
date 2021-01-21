# Calculating volume and surface area of cylinder
# Step 1: define Cylinder class
class Cylinder():

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * 3.14 * (self.radius) ** 2

    def surface_area(self):
        top = 3.14 * (self.radius) ** 2
        return (2 * top) + (2 * 3.14 * self.radius * self.height)
# Step 2: Define instance object by inserting the radius and height
h = int(input("Enter height: \n"))
r = int(input("Enter radius: \n"))

c = Cylinder(h, r)

print(f"The volume of cylinder is {c.volume()} and the surface area is {c.surface_area()}\n")