# We need to import math because we are going to need natural log later on.
import math

# 1. read the country name
Country = input()

# 2. LE, MYS, EYS, GNIpc values as floating inputs
LE = float(input("Please enter life expectancy at birth (LE): "))
MYS = float(input("Please enter mean years of schooling for a 25-year-old (MYS): "))
EYS = float(input("Please enter expected years of schooling for a 5-year-old (EYS): "))
GNIpc = float(input("Please enter gross national income per capita (GNIpc): "))

# 3. Calculation of LEI, EI, MYSI, EYSI, II
LEI = (LE - 20) / (82.3-20)
MYSI = MYS/13.2
EYSI = EYS/20.6
EI = ((MYSI*EYSI)**(1/2)) / 0.951
II = (math.log(GNIpc) - math.log(100)) / (math.log(107721) - math.log(100))

# 4. Calculation of HDI
HDI = (LEI * EI * II)**(1/3)

HDI = format(HDI, '.3f')

# 5. Printing the HDI score with 3 decimals

print("The HDI of %s is %s." %(Country, HDI))