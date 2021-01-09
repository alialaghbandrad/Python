from random import shuffle

# 1 INITIAL LIST
mycard = ['', '0', '']


# 2 SHUFFLE LIST
def shuffle_cards(mycard):
    shuffle(mycard)
    return mycard


mixedup_cards = shuffle_cards(mycard)


# 3 PLAYER GUESS
def player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input("Pick a card number: 0, 1, or 2\n")

    return int(guess)


guess = player_guess()


# 4 CHECK GUESS
def check_guess(mycard, guess):
    if mycard[guess] == '0':
        print('Correct!')
        print(mycard)
    else:
        print("Wrong guess!")
        print(mycard)


check_guess(mixedup_cards, guess)




