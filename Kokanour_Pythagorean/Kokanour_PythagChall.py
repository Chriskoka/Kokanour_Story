"""
To see directions, go to the pythagorean assignment directions
"""
name = input("Hello user! What is your name? Input: ")
print("Nice to meet you, " + name + "!")
a = float(input("Now " + name + ", can you please give me one leg of a right triangle? a = "))
b = float(input("Thank you " + name + ", can you please give me the second leg of a right triangle? b = "))
c = float(input("Finally, can you please give me the hypotenuse of a right triangle? c = "))
x = 2
if (a**2 + b**2 == c **2):
    print('This is a right triangle!')
    
else:
    print('This is not a right triangle!')
