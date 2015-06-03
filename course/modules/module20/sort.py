import time
import random

def selection_sort(original):
    data = original[:]
    start = 0
    while start != len(data):
        for i in range(start, len(data)):
            if data[i] < data[start]:
                data[start], data[i] = data[i], data[start]
        start += 1
    return data

def time_sort(original):
    return sorted(original)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1

    while i < len(left):
        result.append(left[i])
        i+= 1
    while j < len(right):
        result.append(right[j])
        j+= 1
    return result

def merge_sort(original):
    if len(original) < 2 :
        return original[:]
    else:
        middle = len(original)//2
        left = merge_sort(original[:middle])
        right = merge_sort(original[middle:])
        return merge(left, right)

class Test:
    def __init__(self, name, algorithm):
        self.elapsed_time = 0
        self.name = name
        self.algorithm = algorithm
    
    def __str__(self):
         return self.name + "\tSorted successfully in " + str(self.elapsed_time)  + " seconds"
    
    
    
    def check_test(self, sorted_list, original):
        assert len(sorted_list) == len(original), " sorted list was not the same length as original"
        for i in original:
            assert i in sorted_list, i + " was not in the sorted list"

        k = -1
        for i in sorted_list:
            if k >= 0:
                assert i >= k, "The sorted list is not sorted!"
            k = i

    def run_test(self, data):
        start = time.time()
        sorted_list = self.algorithm(data)
        end = time.time()
        self.elapsed_time += (end-start)
        self.check_test(sorted_list, data)

def make_random_list(max):
    data = []
    for i in range(0, max):
        data.append(random.randint(0,max))
    return data


random.seed(time.time())

tests = (
        Test("Selection Sort", selection_sort), 
        Test("Merge Sort", merge_sort),
        Test("Time Sort", time_sort)
    )

data = make_random_list(10000)

for test in tests:
    test.run_test(data)
    print(test)


