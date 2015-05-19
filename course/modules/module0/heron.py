x = int(input("Enter x:  "))
d = 0.00005
g = x / 2

while ( abs(g * g - x) > d ) :
    g = (g + x / g) / 2

print("The square root of", x , "is", g)