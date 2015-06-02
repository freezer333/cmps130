import math

class Shape:
    def __init__(self, color = "black", solid = False):
        self.color = color
        self.solid = solid

    def __str__(self):
        r = "A " + self.color
        if self.solid :
            r += " solid shape"
        else :
            r += " hollow shape"
        return r

class Circle(Shape):
    def __init__(self, color = "red", solid = True, radius = 1):
        Shape.__init__(self, color, solid)
        self.radius = radius

    def getPerimeter(self):
        return 2 * math.pi * self.radius

    def getArea(self):
        return math.pi * (self.radius**2)

    def __str__(self):
        return Shape.__str__(self).replace("shape", "circle") + \
         " with a radius of " + str(self.radius)

class Rectangle(Shape):
    def __init__(self, color = "blue", solid = False, height = 1, width=1):
        Shape.__init__(self, color, solid)
        self.height = height
        self.width = width
    def getPerimeter(self):
        return 2*self.height + 2*self.width
    def getArea(self):
        return self.height * self.width
    def __str__(self):
        return Shape.__str__(self).replace("shape", "rectangle") + \
        " with a dimensions of " + str(self.height) + "x"+ str(self.width)


s = Shape()
print (s)
c = Circle(radius=8, color="green")
print (c)
r = Rectangle(width=5, height=10)
print(r)
