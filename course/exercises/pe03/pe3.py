##############################################################################
# Programming Excercise 3
#
#############################################################################

weight = float(input("Please enter a weight (in kg):  "))
distance = float(input("Please enter a distance (in miles):  "))

if weight <= 2:
	rate = 1.1
elif weight <= 6:
	rate = 2.2
elif weight <= 10:
	rate = 3.7
elif weight <= 20:
	rate = 4.8
else:
	print("Sorry, we can't ship packages over 20kg!")
	exit()

price = rate * distance / 500

# We haven't dealt with output formatting yet... but here is a nice usage of it.
print("It will cost $", "{0:.2f}".format(price) , "to ship this package");
