##############################################################################
# Programming Excercise 7
#
# Ask the user for a number (x) and find the cube 
# root.  If there is no perfect integer cube root, 
# print out a message indicating so.
#############################################################################

x = int(input("Please enter an integer:  "))
ans = 0

# Algorithm:
#   Find the smallest value (ans) which when
#   cubed, is equal to or greater than x
while ans**3 < abs(x):
    ans += 1

# Algorithm:
#    (ans) cubed is either exactly abs(x), meaning it
#    it is the cube root of x, or it is greater
#    than x, meaning there was no cube root (since
#    the cube root function is a monotonic function)
if ans**3 != abs(x):
    print("Sorry,", x, "is not a perfect cube")
else:
    print("The cube root of", x, "is", ans)