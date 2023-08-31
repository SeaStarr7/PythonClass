# 
# The formula for finding the hypotenuse of a right triangle is the formula.
# The formula is a^2 + b^2 = c^2 where a and b are the two other sides of the triangle
# Write a function called findHypotenuse which takes two integers (assume both are positive)
# return the length of the hypotenuse of the triangle. 
# Use the python math library to help you
# https://docs.python.org/3/library/math.html
# -------------------------------------------------------------------------------------------

import math

def findHypotenuse(a, b):
    c = math.sqrt((a * a) + (b * b))
    return c

findHypotenuse(4, 5)






