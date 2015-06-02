##############################################################################
# Programming Excercise 24
#
# Build a Python class representing a Polynomial
# that has three attributes, A, B, and C.  
# - It should support an `evaluate` function given a value X, returns an actual float representing the result of the polynomial when X is plugged in.
# - It should support a `findRoots` function that returns a tuple representingn the roots of the polynomial (x values which yeild 0).  Return an empty tuple when there are no rational roots (see [pe18](../pe18))
# - It should support the `__str__` method such that when the polynomial is printed a proper string representation is displayed.
#  
#############################################################################
import math

class Polynomial :
    def __init__(self, A, B, C):
        self.a = A
        self.b = B
        self.c = C

    def evaluate(self, x):
        return self.a**2 * x + self.b * x + self.c

    def findRoots(self):
        d = self.b*self.b - 4*self.a*self.c
        if d < 0:
            return ()
        elif d == 0:
            return (-self.b / (2 * self.a),)
        else:
            x1 = (-self.b + math.sqrt(d))/(2 * self.a)
            x2 = (-self.b - math.sqrt(d))/(2 * self.a)
            return (x1, x2) 

    def __str__(self):
        return str(self.a) + "x^2 + " + str(self.b) + "x + " + str(self.c)

p1 = Polynomial(1, 5, 6)
p2 = Polynomial(2, 4, 2)
p3 = Polynomial(5, 5, 6)

assert len(p1.findRoots()) == 2
assert len(p2.findRoots()) == 1
assert len(p3.findRoots()) == 0
assert str(p3) == "5x^2 + 5x + 6"
assert p3.evaluate(5) == 156

