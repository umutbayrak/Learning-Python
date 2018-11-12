# Take the input
# I used square root function so imported math
import math

n = int(input())

# Loop for the calculation
# At first I tried looping them all and stuck with the time constraint
# Deleted the loop for c value by defining it with respect to a and b

for a in range(1, n-1):
    for b in range(a+1, n):
        c = (math.sqrt(a**2 + b**2))
        if a + b + c == n:
            print(f'({a}, {b}, {int(c)})')