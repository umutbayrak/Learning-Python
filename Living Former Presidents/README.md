# Learning-Python---Living-Former-Presidents
An exercise from Python class

Donald John Trump (born June 14, 1946) has taken office as the 45th President of the United States on January 20, 2017. Since that day, five former American presidents are alive at the same time.

In the history of the United States there have been only four periods when this was the case:

March 4, 1861 - January 18, 1862: Martin Van Buren, John Tyler, Millard Fillmore, Franklin Pierce, James Buchanan

January 20, 1993 - April 22, 1994: Richard Nixon, Gerald Ford, Jimmy Carter, Ronald Reagan, George H. W. Bush

January 20, 2001 - June 5, 2004: Gerald Ford, Jimmy Carter, Ronald Reagan, George H. W. Bush, Bill Clinton

January 20, 2017 - today: Jimmy Carter, George H. W. Bush, Bill Clinton, George W. Bush, Barack Obama

Herbert Hoover lived another 11,553 days (31 years and 230 days) after leaving office. James Polk died only three months (103 days) after leaving his presidency. Of the individuals elected as US President, eight never obtained the status of "former president" because they died in office: William H. Harrison (pneumonia), Zachary Taylor (bilious diarrhea), Abraham Lincoln (assassinated), James A. Garfield (assassinated), William McKinley (assassinated), Warren G. Harding (heart attack), Franklin D. Roosevelt (cerebral hemorrhage) and John F. Kennedy (assassinated).

Assignment
In this assignment we will process text files that contain information about the lifespan and term of the heads of a particular state. Each line contains five tab-separated information fields: i) name of head of state, ii) birth date, iii) (first) term start date, iv) (last) term end date and v) death date. The four date fields are given in the format dd/mm/yyyy with each fragment being a natural number without leading zeroes: dd indicates the day, mm the month and yyyy the year. The following example shows the contents of such a file that contains information about the last ten Presidents of the United States.

Lyndon B. Johnson	27/8/1908	22/11/1963	20/1/1969	22/1/1973
Richard Nixon	9/1/1913	20/1/1969	9/8/1974	22/4/1994
Gerald Ford	14/7/1913	9/8/1974	20/1/1977	26/12/2006
Jimmy Carter	1/10/1924	20/1/1977	20/1/1981	
Ronald Reagan	6/2/1911	20/1/1981	20/1/1989	5/6/2004
George H. W. Bush	12/6/1924	20/1/1989	20/1/1993	
Bill Clinton	19/8/1946	20/1/1993	20/1/2001	
George W. Bush	6/7/1946	20/1/2001	20/1/2009	
Barack Obama	4/8/1961	20/1/2009	20/1/2017	
Donald Trump	14/6/1946	20/1/2017		
In case a head of state has served multiple non-consecutive terms, we make the assumption that he has served only one consecutive term that runs from the start date of the first term until the end date of the last term. In case the head of state is still serving today, the end date of his term is represented by an empty string. In case the head of state is still alive today, the death date is represented by an empty string. Your task:

Write a function headOfState that takes the location of a text file that contains information about the lifespan and term of the heads of a particular state. The function must return a dictionary that maps the names of all heads of state in the file onto a tuple with the dates (datetime.date objects) of the four events mentioned in the file, in the same order of appearance as in the file. Dates of events that have not yet occurred must be represented by the value None.

Write a function retirement that takes two arguments: the name of a head of state and a dictionary that is constructed as the dictionaries returned by the function headsOfState. The function must return a positive integer that indicates how long the given head of state has enjoyed his retirement. This is computed as the number of days from the end of his (last) term until his death (if the head of state has already died) or until today (if the head of state is still alive). Heads of state that still serve today have not yet enjoyed a single day of their retirement by definition. In case the given name does not occur as a key in the given dictionary, an AssertionError must be raised with the message unknown head of state.

Write a function alive that takes a dictionary that is constructed as the dictionaries returned by the function headsOfState. In addition, the function has an optional parameter reference that may take a reference date (datetime.date object). In case not value is explicitly passed to the parameter reference, the function must use today's date as the reference date. The function also has an optional parameter former that takes a Boolean value (default value: False). The function must return a set containing the names of all heads of state in the dictionary that are/were still alive on the given reference date. If the value True is passed to the parameter former, this set has to be restricted to all former heads of state at the given reference date.
