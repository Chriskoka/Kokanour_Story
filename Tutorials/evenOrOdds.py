"""
Write a program that will take a number (Integers Only) and return a statement that will let the user know if it is even or odd
"""

num=float(input("Hello! Welcome to the even or odd program. This is where you pick an integer and I will tell you if it's Even or Odd! Now please, give me an integer. Input: "))
    
if (num%2 == 1) :
    print("Hey! " + str(num) +  " is an odd number!")
        
        
elif (num%2 == 0) :
    print("Hey! " + str(num) +  " is an even number!")
    
else :
    print("What you typed is not an integer! Please try again!")
