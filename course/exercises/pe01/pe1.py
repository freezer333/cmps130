#############################################
# Programming Excercise 1
#
# Write a program that asks the user
# for 3 integers and prints the 
# largest odd number.  If none of the 
# three numbers were odd, print a message
# indicating so.
#############################################
x = int(input("Enter x:  "))
y = int(input("Enter y:  "))
z = int(input("Enter z:  "))

max_odd = float("-inf")
if x % 2 != 0 and x > max_odd:
	max_odd = x
if y % 2 != 0 and y > max_odd:
	max_odd = y
if z % 2 != 0 and z > max_odd:
	max_odd = z

if max_odd != float("-inf") :
	print("The largest odd number was", max_odd)
else:
	print("There were no odd numbers!")