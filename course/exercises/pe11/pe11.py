##############################################################################
# Programming Excercise 11
#
# Using a function to print each line, write a program
# that accepts a positive number N from the user and
# prints a full diamond of stars, where the top half
# has N rows and the bottom half has N-1 rows
#############################################################################

terms = int(input("Please enter a number:  "));

def print_chars(c, times):
    p = c*times
    print(p, end="")

def print_line(spaces, stars):
    print_chars(" ", spaces)
    print_chars("*", stars)
    print("")

# initialize for first half
spaces = terms-1
stars = 1
for i in range(terms):
    print_line(spaces, stars)
    spaces -= 1
    stars += 2

# re-initialize for second half
spaces = 1
stars -= 4
for i in range(terms-1):
    print_line(spaces, stars)
    spaces += 1
    stars -= 2