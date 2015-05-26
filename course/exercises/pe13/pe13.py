##############################################################################
# Programming Excercise 13
#
# Computer the greatest common denominator from two user inputs
# using Euclid's recursive definition/method
#############################################################################

def gcd (p, q):
    print(p, " . ", q)
    if q < 1 :
        return p
    return gcd(q, p%q)


x = int(input("Please enter x:  "))
y = int(input("Please enter y:  "))

# the algorithm relies on x being >= y
if x < y:
    t = x
    x = y
    y = t

print("GCD = ", gcd(x, y))

