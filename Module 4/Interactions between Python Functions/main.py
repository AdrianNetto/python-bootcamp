from random import shuffle

def shuffle_list(lst):
    shuffle(lst)
    return lst

def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Pick a number: 0, 1 or 2 \n')
    return int(guess)

def check_guess(lst, guess):
    if lst[guess] == 'O':
        print('You won!')
    else:
        print('Wrong guess :(')
        print(lst)


mylist = [' ', 'O', ' ']
mixed_list = shuffle_list(mylist)
guess = player_guess()
check_guess(mixed_list, guess)