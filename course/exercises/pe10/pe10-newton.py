##############################################################################
# Programming Excercise 10
#
# Find the square root of X using Newton-Raphson method
#############################################################################

# epsilon represents our error tolerance.  We'll
# accept any answer Y where Y squared is within epsilon
# of X
epsilon = 0.001

# we'll also keep track of how many turns around the loop
# this takes, so we can compare against other techniques.
num_iterations = 0

x = float(input("Please enter a real number:  "))
ans = x/2.0

while abs(ans**2 - x) > epsilon:
    ans = ans - (((ans**2) - x)/(2*ans))
    num_iterations += 1

print ("Completed in", num_iterations, " iterations")
if abs(ans**2 - x ) > epsilon:
    print("Newton-Raphson could not determine the square root of", x)
else:
    print("The square root of", x, "is", ans, "!")