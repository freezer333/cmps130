##############################################################################
# Programming Excercise 18
#
# Implement the quadrative formula with a function 
# that accepts three coeficient (A, B, C) of a polynomial
# equation and returns the roots via a tuple
#############################################################################
import math

def findRoots(a, b, c):
    d = b*b - 4*a*c
    if d < 0:
        return ()
    elif d == 0:
        return (-b / (2 * a),)
    else:
        x1 = (-b + math.sqrt(d))/(2 * a)
        x2 = (-b - math.sqrt(d))/(2 * a)
        return (x1, x2) 


print(findRoots(1, 5, 6))
print(findRoots(3, 90, 6))
print(findRoots(2, 4, 2))
print(findRoots(5, 5, 6))