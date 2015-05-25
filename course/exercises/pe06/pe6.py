##############################################################################
# Programming Excercise 6
#
# Ask the user to enter 5 numbers that are divisible by 3 and 5.
# Don’t let them stop until they’ve entered 5 of them!
#############################################################################

count = 0
while count < 5 :
    val = int(input("Enter a value divisible by 3 and 5:  "))
    if val % 3 == 0 and val % 5 == 0 :
        count += 1