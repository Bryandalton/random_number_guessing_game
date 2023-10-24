from random import randint

answer = randint(1,10)

while True:
    try:
        guess= input('Guess a number between 1 and 10: ')
        if 0 < int(guess) < 11:
            if int(guess) == answer:
                print("Yout're a genius!!!")
                break
            elif int(guess) > answer:
                print('Nope, lower!')
            else:
                print('Nope, higher!')
        else:
            print('1 - 10 only')
        
    except ValueError:
        print('Please enter a number')
