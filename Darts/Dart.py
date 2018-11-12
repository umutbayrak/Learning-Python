# Being able to use arctan in the polar coordinates
import math

# Take the x, y coordinates of the result
x_float = float(input("Enter the x-axis in mm: "))
y_float = float(input("Enter the y-axis in mm: "))

# Conversion to the Polar Coordinates

r_float = (x_float**2 + y_float**2)**0.5
teta_float = math.atan2(y_float, x_float)

beta_float = (math.pi/2) + (math.pi/20) - teta_float

positionAngle = (beta_float // (math.pi/10)) % 20 + 1

if r_float < 6.35:   # bull's eye
    score = 50
elif r_float < 31.8/2:   # single bull
    score = 25
elif r_float < 97.4:
    score = positionAngle
elif r_float < 107:  # triple ring
    score = positionAngle*3
elif r_float < 160.4:
    score = positionAngle
elif r_float < 170:    # double ring
    score = positionAngle*2
else:
    score = 0

print(int(score))
