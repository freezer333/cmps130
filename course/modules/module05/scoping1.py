def f(x):  #name x used as formal parameter
    y = 1
    x = x + y
    print( 'x = ', x)
    return x

x = 3
y = 2
z = f(x) #value of x used as actual parameter

print ('z = ', z)
print ('y = ', y)
print ('x = ', x)