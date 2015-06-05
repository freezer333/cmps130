import numpy as np
import math as math
def make_year_list (year_line):
    tokens = year_line.split()
    year = int(tokens[0])
    # want to build a list of floats, not strings
    rainfall = [float(x) for x in tokens[1:]]
    return (year, rainfall)

def build_table():
    table = dict()
    f = open('../../data/njrainfall.txt', 'r')
    for year in f:
        record = make_year_list(year)
        table[record[0]] = record[1]
    f.close()
    return table;

def find_average(year_table, month) :
    # each element in year_table is a tuple with two entries
    # entry 0 is the year
    # entry 1 is the list of monthly rainfalls for the year
    # so compile a list of only the specific month from all years
    all_years = [ year_table[year][month] for year in year_table ]
    # now get the average
    sum = 0.0
    for r in all_years:
        sum += r
    return sum / len(all_years)

def get_averages(year_table):
    months = []
    for i in range(12):
        months.append(find_average(year_table, i))
    return months

def get_stds(year_table):
    months = []
    def sum_of_square(xlist, mean):
        total = 0
        for  x in xlist:
            total+= (x - mean)**2
        return total

    for i in range(12):
        mean = find_average(year_table, i);
        xs = [ year_table[year][i] for year in year_table ]
        ss = sum_of_square(xs, mean);
        under = (1/len(xs)) * ss
        months.append(math.sqrt(under))
    return months

def simulate_years(num_years, means, stds):
    rain = [max(0, np.random.normal(means[i%12], std[i%12])) for i in range(12*num_years)]
    return rain

def has_drought(months, thres, consec, means):
    in_a_row = 0
    for m in range(len(months)):
        if months[m] <= means[m%12]*thres :
            in_a_row += 1
        else :
            in_a_row = 0
        if in_a_row == consec:
            return True
    return False


year_table = build_table()
means = get_averages(year_table)
std = get_stds(year_table)


threshold = float(input("Please enter drought threshold (i.e 0.05 means 5% < is considered drought):  "))
consec = int(input("Enter the number of consecutive months to qualify for drought:  "))
num_have_drought = 0.0
for trial in range(100000):
    future = simulate_years(2, means, std)
    if has_drought(future, 1-threshold, consec, means) :
        num_have_drought += 1

print("Likelhood of severe drought is " + "{0:.3f}%".format(num_have_drought/100000.0*100))


