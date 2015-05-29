##############################################################################
# Programming Excercise 22
#
# Write a function that accepts a list of integers and returns 
# the first even number in the list.
#
# Raise an exception if the list does not have an even number.
#############################################################################

def find_evens(numbers):
    for n in numbers :
        if n % 2 == 0:
            return n
    raise ValueError("The list provided does not contain even numbers")

t = find_evens([1, 3, 4, 5, 9, 10])
assert t == 4, "Expected 4, got "+t

t = find_evens([2, 3, 4, 5, 9, 10])
assert t == 2, "Expected 2, got "+t

try :
    t = find_evens([1, 3, 7, 5, 9, 111])
    assert False, "Whoa... shouldn't get here, find_evens should have thrown an exception!"
except ValueError:
    print("It works!")
