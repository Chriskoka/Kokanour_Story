"""
To see directions, go to the pythagorean assignment directions
"""
name = input("Hello user! What is your name? Input: ")
print("Nice to meet you, " + name + "!")
a = float(input("Now " + name + ", can you please give me one leg of a right triangle? a = "))
b = float(input("Thank you " + name + ", can you please give me the second leg of a right triangle? b = "))
x = 2
d = ((a ** x) + (b ** 2))
c = (d ** (1/2))
print("With the given legs of " + str(a) + " and " + str(b) + " I can tell you that the hypotenuse is " + str(c))
