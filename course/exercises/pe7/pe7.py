##############################################################################
# Programming Excercise 4
#
# In order to qualify for a particular loan, lets assume you must 
# earn over $60K a year or earn over $35K and have worked at 
# your current job for over 5 years.
# Write program that asks for user's salary and years at current job.
# Output whether or not they qualify.
#############################################################################

salary = float(input("Please enter your current salary:  $"))
years = float(input("Please enter the number of years you've been at this job:  "))

if salary >= 60000 or salary >= 35000 and years >= 5 :
    print("Congratulations, your load has been approved!")
else :
    print("Sorry, we cannot give you the load...")