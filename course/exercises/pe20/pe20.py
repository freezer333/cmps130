##############################################################################
# Programming Excercise 20
#
# Build a list of lists representing the monthly rainfall in NJ over 
# the past 120 years.  Use the file in ../../data/rainfall.txt
#
# Ask the user for a year and month and report the rainfall that month, 
# along with the average rainfall for that month over the course of 
# the entire year range of the data
#
# You can get the actual data here:   http://climate.rutgers.edu/stateclim_v1/data/njhistprecip.html
#  
#############################################################################

def make_year_list (year_line):
    tokens = year_line.split()
    year = int(tokens[0])
    # want to build a list of floats, not strings
    rainfall = [float(x) for x in tokens[1:]]
    return (year, rainfall)

def build_table():
    years = []
    f = open('../../data/njrainfall.txt', 'r')
    for year in f:
        years.append(make_year_list(year))
    f.close()
    return years;

def find_average(year_table, month) :
    # each element in year_table is a tuple with two entries
    # entry 0 is the year
    # entry 1 is the list of monthly rainfalls for the year
    # so compile a list of only the specific month from all years
    all_years = [x[1][month] for x in year_table]
    # now get the average
    sum = 0.0
    for r in all_years:
        sum += r
    return sum / len(all_years)


year_table = build_table()
first_year = int(year_table[0][0])
month_strings = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 
                'October', 'November', 'December']
print("Loaded rainfall data for NJ from", year_table[0][0], "through", year_table[-1][0])
done = False
while done == False:
    year = int(input("Please enter the year:  "))
    if year < 0 :
        done = True
    else :
        month = int(input("Please enter the month (1-12):  ")) - 1  # all indexes start at 0!
        avg = find_average(year_table, month)
        this_year = year_table[year-first_year][1][month]
        print("The rainfall in", month_strings[month], "was", this_year, "inches", year, ".")
        print("The average rainfall since", first_year, "was ", avg, "inches.")