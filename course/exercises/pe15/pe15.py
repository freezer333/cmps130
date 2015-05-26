##############################################################################
# Programming Excercise 15
#
# A palindrome is a string which reads the same forwards and backwards.  
# Its a condition that can be checked recursively as follows:
#
# - A string of length 1 or 0 is always a palindrome (base case)
# - If a string's first and last character are the same, **and** 
#   the interior is a palindrome, then the string is a palindrome (recursive step)
#############################################################################



def isPalindrome(s):

    # internal function, its only relevant (and callable) from within
    # the isPalindrome function.  Many would call theis a "helper" function
    def toChars(s):
        """ Returns s, with all lower case letters and all numbers, spaces, 
            and punctuation removed"""
        s = s.lower()
        letters = ""
        for c in s:
            if c in "abcdefhijklmnopqrstuvwxyz":
                letters = letters + c
        return letters


    # this does the real recursive work...
    def isPal(s):
        if len(s) <= 1:
            return True
        else :
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

test = input("Please enter a phrase:  ")
if isPalindrome(test) :
    print("That is a palindrome!")
else:
    print("That is not a palindrome")