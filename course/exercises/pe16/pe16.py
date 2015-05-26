##############################################################################
# Programming Excercise 16
#
# The file data.txt has a series of temperature values in it (Fahrenheit)
# Open the file and read each value and report back the min, max, and average
# temperature
#############################################################################

input_file = open('data.txt', 'r')
min = float('inf')
max = float('-inf')
total = 0
count = 0

for temp in input_file:
    temp = float(temp)
    if temp < min :
        min = temp
    if temp > max :
        max = temp
    total += temp
    count += 1

input_file.close()
print ("Maximum temperature:  ", max);
print ("Minimum temperature:  ", min);
print ("Average temperature:  ", total/count);