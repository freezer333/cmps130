def median(data) :
    length = len(data)
    if length %2 == 0:
        return (data[length//2-1] + data[length//2])/2
    else:
        return (data[length//2])

class RainfallTable :

    def __init__(self, path):
        table = dict()
        f = open('../../data/njrainfall.txt', 'r')
        for year in f:
            record = self.make_year_list(year)
            table[record[0]] = record[1]
        f.close()
        self.data = table;

    def make_year_list (self, year_line):
        tokens = year_line.split()
        year = int(tokens[0])
        rainfall = [float(x) for x in tokens[1:]]
        return (year, rainfall)

    def get_rainfall(self, year, month):
        """ Returns the rainfall associated with 
            the given year and month.  Both values
            are assumed to be integers (month given
            as 1-12, year as a four digit year).
            Raises an exception if the year/month 
            combination are not found
        """
        assert month >= 1 and month <= 12,  "Month must be integer between 1-12, was " + str(month)
        return self.data[year][month-1];

    def get_average_rainfall_for_month(self, month):
        """ Returns the average rainfall associated with 
            the given month across all years in the table.  
            Month is assumed to be an integer (1-12.
            Raises an exception if the month is not valid.
        """
        total = 0
        years = 0
        for r in self.get_all_by_month(month):
            total += r
            years += 1
        return total/years

    def get_min_year(self):
        """ Returns the minimum year in the table """
        return min(self.data.keys())

    def get_max_year(self):
        """ Returns the maximum year in the table """
        return max(self.data.keys())

    def get_median_rainfall_for_month(self, month):
        """ Returns the median* rainfall associated with 
            the given month across all years in the table.  
            Month is assumed to be an integer (1-12.
            Raises an exception if the month is not valid.
        """
        vals = []
        for r in self.get_all_by_month(month):
            vals.append(r)
        vals.sort()
        return median(vals)

    def get_average_rainfall_for_year(self, year):
        """ Returns the average rainfall in
            the given year across all months.
            Raises exception if year is not
            in table
        """
        total = 0
        for r in self.get_all_by_year(year):
            total += r
        return total/12
    
    def get_median_rainfall_for_year(self, year):
        """ Returns the median rainfall in
            the given year across all months.
            Raises exception if year is not
            in table
        """
        vals = []
        for r in self.get_all_by_year(year):
            vals.append(r)
        vals.sort()
        return median(vals)

    def get_all_by_year(self, year):
        """ Returns the rainfall values for each
            month in the given year.  Raise exception
            if year is not found
        """
        for m in range(1, 13):
            yield self.data[year][m-1]

    def get_all_by_month(self, month):
        """ Returns the rainfall values for each
            year during the given month.  Raise exception
            if month is not valid
        """
        assert month >= 1 and month <= 12,  "Month must be integer between 1-12, was " + str(month)
        for year in self.data.keys():
            yield self.data[year][month-1]

    def get_droughts(self) :
        """ returns a list of strings, representing date (month/year) ranges
            where three or more months in a row had at least 5% less rainfall than
            their historical monthly averages
        """
        return []


table = RainfallTable("../../data/njrainfall.txt")
print(table.get_rainfall(1993, 6))
print(table.get_average_rainfall_for_month(6))

for year in range(table.get_min_year(), table.get_max_year()+1) :
    print("Average monthly rainfall in ", year, "=", table.get_average_rainfall_for_year(year))
    print("Median monthly rainfall in ", year, "=", table.get_median_rainfall_for_year(year))
    print("===========")
    for rain in table.get_all_by_year(year):
        print(rain, end='\t')
    print("\n===========")


for month in range(1, 13) :
    print("Average rainfall in month", month, "=", table.get_average_rainfall_for_month(month))
    print("Median rainfall in month", month, "=", table.get_median_rainfall_for_month(month))
    print("===========")
    for rain in table.get_all_by_month(month):
        print(rain, end='\t')
    print("\n===========")

for d in table.get_droughts() :
    print("Drought:  ", d)


