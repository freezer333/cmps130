import time
import random

def binary_search(data, key):
    def bsearch(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bsearch(L, e, low, mid-1)
        else:
            return bsearch(L, e, mid+1, high)

    if len(data) == 0:
        return False
    else:
        return bsearch(data, key, 0, len(data)-1)

def linear_find_unordered(data, key):
    for i in data:
        if i == key:
            return True;
    return False

def linear_find_ordered(data, key):
    for i in data:
        # The following isn't great, because now we have
        # two comparisons for each value instead of one - 
        # any performance gain we have from ending early 
        # is killed...
        #if i == key:
        #    return True;
        #if i > key:
            #return False

        # Instead, we write it a bit more cryptically, but we'll
        # see a performance increase roughly proportional to the number
        # of misses
        if i >= key:
            return i == key
    return False


class Test
    def __init__(self, name, algorithm):
        self.hits = 0
        self.elapsed_time = 0
        self.name = name
        self.algorithm = algorithm
    def __str__(self):
        print(name + "\tFound", self.hits, " successfully in", self.elapsed, "seconds")
    
    def run_test(data, keys):
        for key in keys:
            start = time.time()
            if algorithm(data, key):
                result.hits += 1
            end = time.time()
            result.elapsed_time += (end-start)
        return result


gen_max = 10000
random.seed(time.time())
data = []
for i in range(0, gen_max):
    data.append(random.randint(0,gen_max))

data.sort()

keys = []
for i in range (0, gen_max):
    keys.append(random.randint(0, gen_max))

lu = TestResult("Linear, unordered", linear_find_unordered)
lo = TestResult("Linear, ordered", linear_find_ordered)
bi = TestResult("Binary Search", binary_search)

lu.run_test(data, keys);
li.run_test(data, keys);
bs.run_test(data, keys);

print(lu)
print(lo)
print(bi)
