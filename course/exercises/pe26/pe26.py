import numpy as np
import matplotlib.pyplot as pylab

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

def get_all_years(year_table, month):
    # each element in year_table is a tuple with two entries
    # entry 0 is the year
    # entry 1 is the list of monthly rainfalls for the year
    # so compile a list of only the specific month from all years
    return [ year_table[year][month] for year in year_table ]

def find_average(year_table, month) :
    all_years = get_all_years(year_table, month)
    total = sum(all_years)
    return total / len(all_years)

def find_min(year_table, month) :
    return min(get_all_years(year_table, month))

def find_max(year_table, month) :
    return max(get_all_years(year_table, month))

def get_minimums(year_table):
    months = []
    for i in range(12):
        months.append(find_min(year_table, i))
    return months

def get_maximums(year_table):
    months = []
    for i in range(12):
        months.append(find_max(year_table, i))
    return months

def get_averages(year_table):
    months = []
    for i in range(12):
        months.append(find_average(year_table, i))
    return months

def get_months(year_table, year):
    months = []
    for i in range(12):
        months.append(year_table[year][i])
    return months

def get_total(year_table, year):
    total = 0
    for i in range(12):
        total += (year_table[year][i])
    return total

def get_totals(year_table) :
    totals = []
    for y in year_table:
        totals.append(get_total(year_table, y))
    return totals


def resolve_month(user_input):
    try :
        m = int(user_input)
    except ValueError:
        # must be a string...
        if user_input in month_strings:
            return month_strings.index(user_input)
        else :
            raise ValueError(user_input + " is not a valid month string")

    # note, m is an int if we are here, because the except
    # block returns or raises an exception
    if m < 1 or m > 12 :
        raise ValueError(user_input + " is not a valid month number (1-12)")
    else:
        return m-1

year_table = build_table()
first_year = min(year_table.keys())
month_strings = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 
                'October', 'November', 'December']
print("Loaded rainfall data for NJ from", first_year, "through", max(year_table.keys()))
done = False
while done == False:
    print("Plotting options:")
    print("1) Plot of rainfall over a given year (x-axis is months, y-axis is rainfall)")
    print("2) Plot of yearly rainfall totals (x axis is years, y-axis is rainfall total for that year)")
    print("3) Plot of monthly averages, min, max (x-axis is months, y-axis is average/min/max as separate data points)")
    print("q) Quit")
    choice = input("Please select a plot:  ")

    if choice == 'q' or choice == 'Q':
        done = True
    elif choice == '1':
        year = int(input("What year would you like to plot?  "))
        pylab.figure("Monthly Rainfall for " + str(year))
        pylab.plot(range(len(month_strings)), get_months(year_table, year))
        pylab.xticks(range(len(month_strings)), month_strings, size='small')
        pylab.ylabel('Rainfall (inches)')
        pylab.show()
    elif choice == '2':
        pylab.figure("Yearly Rainfall - " + str(min(year_table.keys())) + "-" + str(max(year_table.keys())))
        pylab.plot(range(min(year_table.keys()),max(year_table.keys())+1), get_totals(year_table))
        pylab.ylabel('Rainfall (inches)')
        pylab.show()
    elif choice == '3':
        pylab.figure("Monthly Rainfall Averages")
        pylab.plot(range(len(month_strings)), get_averages(year_table))
        pylab.plot(range(len(month_strings)), get_minimums(year_table))
        pylab.plot(range(len(month_strings)), get_maximums(year_table))
        pylab.xticks(range(len(month_strings)), month_strings, size='small')
        pylab.ylabel('Rainfall (inches)')
        pylab.show()