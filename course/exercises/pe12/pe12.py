##############################################################################
# Programming Excercise 12
#
# Write a function `isIn` that accepts two strings as arguments and returns 
# `True` if either string occurs anywhere in the other, and `False` otherwise.
#############################################################################

# Note since we have test cases, its not really necessary to talk to the user

# This is just a testing function, to be reused many times
def test_isIn(str1, str2, expected):
    if isIn(str1, str2) != expected:
        print("Test Failed:  ", str1, " - ", str2, " expected ", expected)
    else :
        print("Test Passed:  ", str1, " - ", str2)

# We are using the in operator, which works with sequences (such as string)
# We'll see more on this later in Chapter 5
# https://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange
def isIn(str1, str2 ):
    if str1 in str2:
        return True
    elif str2 in str1:
        return True
    else:
        return False

test_isIn("abc", "bc", True)
test_isIn("abc", "BC", False)
test_isIn("ABC", "BCD", False)
test_isIn("abc", "zyxabcxyz", True)
test_isIn("BC", "ABCD", True)
test_isIn("ABC", "ABC", True)
