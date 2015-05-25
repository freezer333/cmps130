##############################################################################
# Programming Excercise 10
#
# Find the square root of X using bisection
#############################################################################

# epsilon represents our error tolerance.  We'll
# accept any answer Y where Y squared is within epsilon
# of X
epsilon = 0.001

# we'll also keep track of how many turns around the loop
# this takes, so we can compare against other techniques.
num_iterations = 0

x = float(input("Please enter a real number:  "))
ans = 0.0
low = 0
high = max(1, x)
ans = (high + low)/2

while abs(ans**2 - x) > epsilon:
    if ans ** 2 > x :
        high = ans
    else:
        low = ans
    ans = (high + low)/2
    num_iterations += 1

print ("Completed in", num_iterations, " iterations")
if abs(ans**2 - x ) > epsilon:
    print("Exhaustive enumeration could not determine the square root of", x)
else:
    print("The square root of", x, "is", ans, "!")