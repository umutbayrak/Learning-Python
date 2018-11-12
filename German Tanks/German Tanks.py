# Taking the first input

x = int(input("Please enter an integer: "))
maximum = 0
n = 0
while x >= 0: # Taking inputs till it's negative

    n += 1 # It will give the number of observations, n

    if x > maximum:   # Obtains the maximum value
        maximum = x

    x = int(input("Another integer: "))

t = ((n+1)*maximum/n) - 1  # Estimation formula for tank number

print(f'The number of produced tanks is estimated to be {round(t)}.')
