##############################################################################
# Programming Excercise 5
#
# Ask the user to enter a series of positive integers.  
# When they enter a -1, you can stop.
#
# Print out the largest odd number they entered.  
# If they didn't enter any odd numbers then just simply say so.

#############################################################################

# note 0 isn't odd, so we'll know this 
# was never set by checking against 0!
largest_odd = 0 

entered = 0 # this will be -1 to stop the loop
while entered != -1 :
    entered = int(input("Please enter a positive odd number (-1 to stop):  "))
    if entered % 2 != 0 and largest_odd < entered:
        largest_odd = entered

if largest_odd == 0:
    print ("You never entered any odd numbers... oh well!")
else :
    print ("The largest odd number you typed was", largest_odd)