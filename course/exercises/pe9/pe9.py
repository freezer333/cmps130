##############################################################################
# Programming Excercise 9
#
# PI can be estimated by computing an infinite series…
#
# PI = 4 * ( 1 - 1/3 + 1/5 - 1/7 + 1/9 -1/11 +…)
#
# Write a program to estimate PI…
# How long does it take to get to 3.14159?
#############################################################################

terms = int(input("Please enter number of terms:  "));

den = 1
sign = 1
accum = 0
for i in range(terms) :
    term = sign / den
    accum += term
    den += 2
    sign *= -1

print ("PI is about", 4 * accum)