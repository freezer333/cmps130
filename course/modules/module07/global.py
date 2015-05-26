##############################################################################
# Programming Excercise 14
#
# Write a recursive function to find the Nth Fibonicci number
#
# As a point of reference, the iterative approach is also calculated.
# Check out how big of a difference these approaches make for n = 40!
# ... careful, the recursive solution may take several minutes for n = 40!
#############################################################################
import time

def fib_iteratively(n):
    n0 = 1
    n1 = 1
    total = 1
    for i in range(2, n):
        t = n1
        n1 = t + n0
        n0 = t
    return n1 + n0


def fib(n):
    global fib_calls
    fib_calls += 1
    if n <= 1:
        return 1
    else: 
        return fib(n-1) + fib(n-2)



n = int(input("Please enter n:  "))
global fib_calls
fib_calls  = 0
start = time.time()
v = fib(n)
end = time.time()

print("Fibonacci #", n, "is", v, "in", end-start, "seconds recursively")
print("This included", fib_calls, "calls to the fib function!")
start = time.time()
v = fib_iteratively(n)
end = time.time()
print("Fibonacci #", n, "is", v, "in", end-start, "seconds iteratively")

