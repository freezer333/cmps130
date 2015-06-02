##############################################################################
# Programming Excercise 25
#
# In this example we'll use the [ezgraphics](http://www.ezgraphics.org/) to actually draw some circles and rectangles.  

# - Add a tuple property to the base shape class that represents an x,y position (center) of the shape
# - Add a draw() method to the circle and rectangle class that uses the ezgraphics library to draw to the screen.  

#############################################################################
import math



class Shape:

    

    def __init__(self, color = "black", solid = False, position = (10, 10)):
        self.color = color
        self.solid = solid
        self.position = position

    def __str__(self):
        r = "A " + self.color
        if self.solid :
            r += " solid shape"
        else :
            r += " hollow shape"
        return r

    def prepare_canvas(self, canvas):
        canvas.setOutline(self.color)
        if self.solid:
            canvas.setFill(self.color)
        else:
            canvas.setFill()


class Circle(Shape):
    def __init__(self, color = "red", solid = True, radius = 1, position=(10, 10)):
        Shape.__init__(self, color, solid, position)
        self.radius = radius

    def getPerimeter(self):
        return 2 * math.pi * self.radius
        
    def getArea(self):
        return math.pi * (self.radius**2)

    def __str__(self):
        return Shape.__str__(self).replace("shape", "circle") + \
         " with a radius of " + str(self.radius)
    def draw(self, canvas):
        self.prepare_canvas(canvas)
        canvas.drawOval(self.position[0], self.position[1], self.radius/2, self.radius/2)

class Rectangle(Shape):
    def __init__(self, color = "blue", solid = True, height = 1, width=1, position=(10, 10)):
        Shape.__init__(self, color, solid, position)
        self.height = height
        self.width = width
    def getPerimeter(self):
        return 2*self.height + 2*self.width
    def getArea(self):
        return self.height * self.width
    def __str__(self):
        return Shape.__str__(self).replace("shape", "rectangle") + \
        " with a dimensions of " + str(self.height) + "x"+ str(self.width)
    def draw(self, canvas):
        self.prepare_canvas(canvas)
        canvas.drawRectangle(self.position[0], self.position[1], self.width, self.height)

import ezgraphics

things = []
things.append(Circle(radius=80, color="green", position=(50, 100)))
things.append(Rectangle(width=50, height=100, solid=False,position=(200, 15)))
things.append(Rectangle(width=200, color="red", height=50, position=(100, 260)))

win = ezgraphics.GraphicsWindow()
win.setTitle("CMPS 130 - pe25")
canvas = win.canvas()
for thing in things:
    thing.draw(canvas)
win.wait()
