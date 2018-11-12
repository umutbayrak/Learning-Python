# Learning-Python---Friday-the-13th
An exercise from Python class

Friday the thirteenth is generally seen as an unlucky day in our culture. However, it is not immediately sure where this superstition comes from, and although there are numerous reports in various religions and customs, it seems that this superstition is at most 100 years old.

The combination of the weekday Friday and the number thirteen is also not as universal as you might think. In Belgium, the Netherlands and England, for example, Friday the thirteenth is indeed seen as an unlucky day. However, in Greece, Spain and Latin America, Tuesday the thirteenth is an unlucky day. In Italy everyone is extra careful on Friday the seventeenth.

Assignment

Write a function unluckyDays that takes a starting date as its argument. In addition, the function has three optional arguments that respectively indicate an end date, a day number and a weekday number. The function must return the number of days between the start date and the end date (including these boundaries) that fall on the specified weekday. If only the mandatory argument is given, the number of Fridays the thirteenth between the start date and today must be calculated. If the starting date comes later than the end date, there are no days between the starting date and the end date, and logically the function must return the value 0 in this case.

Preparation

In this assignment you will have to make use of the data types date and timedelta that are defined in the datetime module of the Python Standard Library. Before starting to work on the actual assignment, you should first have a look at how Python responds when you execute the following sequence of instructions in an interactive Python session:
