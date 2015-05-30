class RainfallTable :
    def __init__(self, path):
        print("created")

    def get_rainfall(self, year, month):
        """ Returns the rainfall associated with 
            the given year and month.  Both values
            are assumed to be integers (month given
            as 1-12, year as a four digit year).
            Raises an exception if the year/month 
            combination are not found
        """
        return 0.0;

    def get_average_rainfall_for_month(self, month):
        """ Returns the average rainfall associated with 
            the given month across all years in the table.  
            Month is assumed to be an integer (1-12.
            Raises an exception if the month is not valid.
        """
        return 0.0

    def get_min_year(self):
        """ Returns the minimum year in the table """
        return 1990

    def get_max_year(self):
        """ Returns the maximum year in the table """
        return 2010

    def get_median_rainfall_for_month(self, month):
        """ Returns the median* rainfall associated with 
            the given month across all years in the table.  
            Month is assumed to be an integer (1-12.
            Raises an exception if the month is not valid.
        """
        return 0

    def get_average_rainfall_for_year(self, year):
        """ Returns the average rainfall in
            the given year across all months.
            Raises exception if year is not
            in table
        """
        return 0
    def get_median_rainfall_for_year(self, year):
        """ Returns the median rainfall in
            the given year across all months.
            Raises exception if year is not
            in table
        """
        return 0

    def get_all_by_year(self, year):
        """ Returns the rainfall values for each
            month in the given year.  Raise exception
            if year is not found
        """
        for s in range(0, 1):
            yield s

    def get_all_by_month(self, month):
        """ Returns the rainfall values for each
            year during the given month.  Raise exception
            if month is not valid
        """
        for s in range(0, 1):
            yield s

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
    print("Average rainfall in ", year, "=", table.get_average_rainfall_for_year(year))
    print("Median rainfall in ", year, "=", table.get_median_rainfall_for_year(year))
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


