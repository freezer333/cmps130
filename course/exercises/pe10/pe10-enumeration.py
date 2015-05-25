##############################################################################
# Programming Excercise 10
#
# Find the square root of X using exhaustive enumeration
#############################################################################

# epsilon represents our error tolerance.  We'll
# accept any answer Y where Y squared is within epsilon
# of X
epsilon = 0.001

# step is based on epsilon for convenience, but doesn't
# have to be.  Its just the increment that we'll check in.
# It should be rather small relative to epsilon
step = epsilon ** 2

# we'll also keep track of how many turns around the loop
# this takes, so we can compare against other techniques.
num_iterations = 0

x = float(input("Please enter a real number:  "))
ans = 0.0

while abs(ans**2 - x) > epsilon:
    ans += step
    num_iterations += 1

print ("Completed in", num_iterations, " iterations")
if abs(ans**2 - x ) > epsilon:
    print("Exhaustive enumeration could not determine the square root of", x)
else:
    print("The square root of", x, "is", ans, "!")