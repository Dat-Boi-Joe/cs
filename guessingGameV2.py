import random

def invalad():
    print('Please enter a number')

def start():
    print('Welcome to Guessing Game V2!')

def difficulty():
    print('Please select your difficulty')
    print('Easy (1-100 with 15 guesses)')
    print('Medium (1-300 with 10 guesses)')
    print('Hard (1-500 with 5 guesses)`')
    while True:
        x = input(': ').lower
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

def number_gen(difficulty):
    if difficulty == 'easy':
        number = random.randint(1,100)
        return number
    elif difficulty == 'medium':
        number = random.randint(1,300)
        return number
    elif difficulty == 'hard':
        number = random.randint(1,500)
        return number
def tries(difficulty):
    if difficulty == 'easy':
        tries = 15
        return tries
    elif difficulty == 'medium':
        tries = 10
        return tries
    elif difficulty == 'hard':
        tries = 5
        return tries


def errorProof():
    while True:
        try:
            x = int(input('Guess: '))
            break
        except:
            invalad()
    return x




start()
dif = difficulty()
num = number_gen(dif)
i = tries(dif)
while i > 1:
    print('You have ' + str(i) + ' tries left')
    input = errorProof()
    if input == num:
        print('Congrats you guessed the number!')
        break
    elif input > num:
        print('Not quite, your number is too high')
        i - 1
    elif input < num:
        print('Not quite, your number is too low')
        i - 1