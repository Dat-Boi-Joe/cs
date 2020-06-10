import random


def start():
    print('Welcome to Guessing Game V2!')


def difficulty():
    print('Please select your difficulty')
    print('Easy (1-100 with 15 guesses)')
    print('Medium (1-300 with 10 guesses)')
    print('Hard (1-500 with 5 guesses)`')
    while True:
        x = input(': ').lower()
        if x == 'easy':
            print('You have selected Easy mode.')
            return x
        elif x == 'medium':
            print('You have selected Medium mode')
            return x
        elif x == 'hard':
            print('You have selected Hard mode.')
            return x
        else:
            print('Please select a valid difficulty.')


def number_gen(dif):
    if dif == 'easy':
        number = random.randint(1, 100)
        return number
    elif dif == 'medium':
        number = random.randint(1, 300)
        return number
    elif dif == 'hard':
        number = random.randint(1, 500)
        return number


def tries(difficulty):
    if difficulty == 'easy':
        t = 15
        return t
    elif difficulty == 'medium':
        t = 10
        return t
    elif difficulty == 'hard':
        t = 5
        return t


def errorProof():
    while True:
        y = input(': ')
        try:
            x = int(y)
            if isinstance(x, int):
                break
        except:
            print('Please enter a whole number')
    return x


start()
dif = difficulty()
num = number_gen(dif)
i = int(tries(dif))
while int(i) > 0:
    print('You have ' + str(i) + ' tries left')
    z = errorProof()
    if int(z) == int(num):
        print('Congrats you guessed the number!')
        break
    elif int(z) > int(num):
        print('Not quite, your number is too high')
        i = i - 1
    elif int(z) < int(num):
        print('Not quite, your number is too low')
        i = i - 1
if int(i) == 0:
    print("Sorry you could not guess the number.")
