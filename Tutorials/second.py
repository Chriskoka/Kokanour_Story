
invalid_input = True
def start() :
    age = int(input('Please type your age here ----> '))

    if (age > 17) :
        vote=str(input("Please vote who you think is the best out of the following list: Chris, Chris, Chris, and Chris. Answer: "))
        if (vote == "Chris" or vote == "chris") :
            print('Wow, thank you for the vote!')
            invalid_input = False
        else:
            print('Please try again. The answer you typed is not an option on the list.')
    if (age < 18) :
        print('Please go away, you are not of age to vote.')
        invalid_input = False

while invalid_input :
    start()