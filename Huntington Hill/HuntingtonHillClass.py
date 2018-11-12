class Census:

    """
    >>> us2010 = Census(2010, 'us_population.csv')
    >>> us2010.citizens('Alabama')
    4779736
    >>> us2010.citizens('Hawaii')
    1360301
    >>> us2010.citizens('Wyoming')
    563626
    >>> us2010.citizens('Calisota')
    Traceback (most recent call last):
    AssertionError: no data available
    >>> us2010.allocation(435)
    {'Oklahoma': 5, 'Illinois': 18, 'Pennsylvania': 18, 'Iowa': 4, 'Maine': 2, 'South Dakota': 1, 'Nebraska': 3, 'New Jersey': 12, 'Maryland': 8, 'Texas': 36, 'Alabama': 7, 'Idaho': 2, 'South Carolina': 7, 'Michigan': 14, 'Tennessee': 9, 'Kansas': 4, 'Wyoming': 1, 'Wisconsin': 8, 'Louisiana': 6, 'Nevada': 4, 'Vermont': 1, 'Massachusetts': 9, 'Kentucky': 6, 'California': 53, 'Missouri': 8, 'Colorado': 7, 'Arizona': 9, 'Florida': 27, 'Utah': 4, 'Virginia': 11, 'Alaska': 1, 'New Mexico': 3, 'Ohio': 16, 'Oregon': 5, 'Hawaii': 2, 'Indiana': 9, 'North Carolina': 13, 'New York': 27, 'Delaware': 1, 'Minnesota': 8, 'West Virginia': 3, 'New Hampshire': 2, 'Arkansas': 4, 'Montana': 1, 'Georgia': 14, 'Connecticut': 5, 'Rhode Island': 2, 'Mississippi': 4, 'Washington': 10, 'North Dakota': 1}
    >>> us2010.allocation(1024)
    {'Oklahoma': 12, 'Illinois': 43, 'Pennsylvania': 42, 'Iowa': 10, 'Maine': 4, 'South Dakota': 3, 'Nebraska': 6, 'New Jersey': 29, 'Maryland': 19, 'Texas': 84, 'Alabama': 16, 'Idaho': 5, 'South Carolina': 15, 'Michigan': 33, 'Tennessee': 21, 'Kansas': 9, 'Wyoming': 2, 'Wisconsin': 19, 'Louisiana': 15, 'Nevada': 9, 'Vermont': 2, 'Massachusetts': 22, 'Kentucky': 14, 'California': 124, 'Missouri': 20, 'Colorado': 17, 'Arizona': 21, 'Florida': 63, 'Utah': 9, 'Virginia': 27, 'Alaska': 2, 'New Mexico': 7, 'Ohio': 38, 'Oregon': 13, 'Hawaii': 5, 'Indiana': 22, 'North Carolina': 32, 'New York': 64, 'Delaware': 3, 'Minnesota': 18, 'West Virginia': 6, 'New Hampshire': 4, 'Arkansas': 10, 'Montana': 3, 'Georgia': 32, 'Connecticut': 12, 'Rhode Island': 4, 'Mississippi': 10, 'Washington': 22, 'North Dakota': 2}
    >>> us2010.allocation(42)
    Traceback (most recent call last):
    AssertionError: too few representatives

    >>> Census(1900, 'us_population.csv')
    Traceback (most recent call last):
    AssertionError: no data available
    """
    def __init__(self, year, location, city=None, dictionary=None):
        self.year, self.location = year, location
        self.city = city
        self.dictionary = dictionary

        infile = open(self.location, 'r')
        firstLine = infile.readline()

        # All these efforts is to make a dictionary for the years from scratch
        year_list = firstLine.split(',')
        year_list.remove('REGION')
        year_list[10] = '2010'

        yearN = [int(x) for x in year_list]
        y = [list(x) for x in enumerate(yearN)]
        year_dict = {d[0]: d[1:] for d in y}

        for key in year_dict:
            year_dict[key] = ''.join(str(year_dict[key]))
            year_dict[key] = int(year_dict[key].strip("[]"))

        year_dict = {v: k for k, v in year_dict.items()}

        # Now we have a decent dictionary with indices year_dict

        # Assertion Error

        if self.year not in year_dict.keys():
            raise AssertionError('no data available')



    def citizens(self, city):
        self.city = city

        infile = open(self.location, 'r')
        firstLine = infile.readline()

        # All these efforts is to make a dictionary for the years from scratch
        year_list = firstLine.split(',')
        year_list.remove('REGION')
        year_list[10] = '2010'

        yearN = [int(x) for x in year_list]
        y = [list(x) for x in enumerate(yearN)]
        year_dict = {d[0]: d[1:] for d in y}

        for key in year_dict:
            year_dict[key] = ''.join(str(year_dict[key]))
            year_dict[key] = int(year_dict[key].strip("[]"))

        year_dict = {v: k for k, v in year_dict.items()}

        # Now we have a decent dictionary with indices year_dict

        # Assertion Error

        if self.year not in year_dict.keys():
            raise AssertionError('no data available')

        # Reading other files so that we can have another dictionary with cities and their citizens
        otherLines = []
        for line in infile:
            otherLines.append(line)

        line_list = [line.strip().split(',') for line in otherLines]
        line_dict = {d[0]: d[1:] for d in line_list}

        year_value = year_dict[self.year]

        result = dict((k, int(v[year_value])) for k, v in line_dict.items())
        self.dictionary = result

        if self.city not in result.keys():
            raise AssertionError('no data available')
        return result[self.city]


    def allocation(self, representatives):
        self.representatives = representatives

        population = self.dictionary

        # Assertion Error here:
        if self.representatives < len(population):
            raise AssertionError('too few representatives')

        # Method:
        # Creating a new dictionary with the keys of the population dictionary

        result_dict = {x: 1 for x in population.keys()}
        geometric_dict = {x: 0 for x in population.keys()}

        remaining = representatives - len(population)

        # Defining a geometric mean function:

        def geometricMean(n, p):

            mean = p / (n * (n + 1)) ** 0.5

            return mean

        for i in range(1, remaining + 1):
            for key, value in geometric_dict.items():
                geometric_dict[key] = geometricMean(result_dict[key], population[key])
            reversed_geometric = {v: k for k, v in geometric_dict.items()}

            maximum = max(reversed_geometric.keys())
            increase_key = reversed_geometric[maximum]
            result_dict[increase_key] += 1

        return result_dict