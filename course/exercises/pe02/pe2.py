##############################################################################
# Programming Excercise 2
#
# Write a program that asks the user for a numeric grade.  
# Use a series of branching statements to print out the letter grade - 
# where A is between 90 and 100, B is between 80 and 89, C is between 
# 70 and 79, D is between 60-69, and anything lower is an F.  
# If the user types in a negative number or a number greater than 
# 100, print out an error message and exit using the `exit()` command
#############################################################################

# read the number as a float just in case they enter something like 89.8!
num = float(input("Please enter a grade between 0 and 100:  "))
if num < 0 or num > 100 :
	print("That is not a valid grade!")
	exit()


if num >= 90:
	print("You got an A!")
elif num >= 80:
	print("You got a B!")
elif num >= 70:
	print("You got a C!")
elif num >= 60:
	print("You got a D...")
else :
	print("You failed...sorry :(");
