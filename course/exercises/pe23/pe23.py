##############################################################################
# Programming Excercise 23
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
    try:
        year = int(input("Please enter the year:  "))

        if year < 0 :
            done = True
        else :
            user_input = input("Please enter the month (1-12) or full month name:  ")
            month = resolve_month(user_input)
            avg = find_average(year_table, month)
            this_year = year_table[year][month]
            print("The rainfall in", month_strings[month], "was", this_year, "inches", year, ".")
            print("The average rainfall since", first_year, "was ", avg, "inches.")
    except ValueError as e:
        print("Please make sure you enter a valid year and month")
        print(e)
    except KeyError:
        print("The requested year was not available")
        

