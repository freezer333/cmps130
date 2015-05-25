##############################################################################
# Programming Excercise 8
#
# Ask the user for a positive integer N, between 2 and 20.  
# Print a vertical half diamond, where the top half has 
# N rows, and the bottom half has N-1 rows.
#
# So, for N = 4

# * 
# * * 
# * * * 
# * * * * 
# * * * 
# * * 
# *
#############################################################################

done = False
while not done :
  x = int(input("Please enter an integer between 2 and 20:  "));
  done = x >= 2 and x <= 20

# top half
for i in range(1, x+1):
    for j in range(i):
        # the print function takes an optional command to specify
        # the end character.  Default is the new line character, 
        # but I don't want that after each *, so I'm giving it the
        # empty string
        print("*", end="")
    # This is the end of the outer loop, we need to move to the 
    # next line now
    print("")

# bottom half
for i in range(x-1, 0, -1):
    for j in range(i):
        # the print function takes an optional command to specify
        # the end character.  Default is the new line character, 
        # but I don't want that after each *, so I'm giving it the
        # empty string
        print("*", end="")
    # This is the end of the outer loop, we need to move to the 
    # next line now
    print("")

