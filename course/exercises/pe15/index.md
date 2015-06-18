# Scientific Programming with 
<img src="../../imgs/python.png"/>
## Programming Exercise 15 - Check for a Palindrome
A palindrome is a string which reads the same forwards and backwards.  Its a condition that can be checked recursively as follows:

- A string of length 1 or 0 is always a palindrome (base case)
- If a string's first and last character are the same, **and** the interior is a palindrome, then the string is a palindrome (recursive step)

Using string slicing, write a program that asks the user for a string and reports back if it is a palindrome or not.

Ignore case, and do not allow any non-alphabetical characters to interfere with the palindrome calculation.  For instance, the following strings are palindromes:

1. `Radar` is a palindrome because of case-sensitivity
1. `No lemon, no melon.` is a palindrome if you do not consider spaces or commas, or capitalization
1. `1234` is a palindrome because it doesn't contain any alphabetical characters, so it falls under the base case immediately!

<div class="highlight">** Reminder -  ** you learn by *doing* not watching.  Do this program yourself first!  Then watch how I did it!</div>

### Solution Video
<iframe width="420" height="315" src="https://www.youtube.com/embed/d03vzGLlh28" frameborder="0" allowfullscreen></iframe>

### Solution Code
[pe15.py](pe15.py)



