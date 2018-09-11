age = input('Please type your age here ----> ')

if (age > 17) :
    vote=input("Please vote who you think is the best out of the following list: Chris, Chris, Chris, and Chris. Answer: ")
    if (vote=="Chris") :
        print('Wow, thank you for the vote!')
    else:
        print('Please try again, you typed the wrong answer')
if (age < 18) :
    print('Please go away, you are not of age to vote.')