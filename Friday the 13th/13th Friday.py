from datetime import date
import pandas as pd

def unluckyDays(startDate, endDate = date.today(), day=13 , weekday=4):

    """
    >>> from datetime import date
    >>> unluckyDays(date(2012, 1, 1), date(2012, 12, 31))
    3
    >>> unluckyDays(date(2012, 1, 1), date(2012, 12, 31), 14, 5)
    3
    >>> unluckyDays(date(2012, 1, 1), date(2012, 12, 31), 17, 4)
    2
    >>> unluckyDays(date(2012, 1, 1), date(2012, 12, 31), 13, 1)
    2
    >>> unluckyDays(startDate=date(2012, 1, 1), day=1, weekday=0, endDate=date(2012, 12, 31))
    1
    """


    daterange = pd.date_range(startDate, endDate)
    count = 0
    countIf = 0

    if day != 13 or weekday != 4:
        for singleDate in daterange:
            if singleDate.weekday() == weekday and singleDate.day == day:
                countIf += 1
        return countIf


    for singleDate in daterange:
        if singleDate.weekday() == 4 and singleDate.day == 13:
            count += 1
    return count




if __name__ == '__main__':
    import doctest
    doctest.testmod()