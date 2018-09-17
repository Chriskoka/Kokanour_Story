"""
Math Functions
"""
#Variables

a = 3
b = -6
c = 9

#Addition & Subtraction

print(a+b)
print(a-b)

#Multiplication & Division

print(a * b)
print(a / b)

#exponents

print(a ** b) # Notice ** means to the power of
print(b ** a)

#Square Root & Cube Root

print(c ** (1/3))
print(c ** (1/2))

#Modulus (% symbol is used) -- Only returns the remainder after division

print(c % a) #Said as c mod a
print(c%4)

"""In order to do advanced math like sine, cosine, etc, you have to inport math and add .math to the function"""

import math

print(math.sin(a))