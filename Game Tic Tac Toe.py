# STEP 1: Print out board
def display_board(board):
    print('\n' * 100)

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# STEP 2: Player input: X or O
def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):

        marker = input('Player one: Do you want to be X or O? \n').upper()

        if marker not in ['X', 'O']:
            print("Sorry, wrong input! please choose X or O ")

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# STEP 3: The function that requests the marker (X or O) and the desired position of the board and inserts into the board
def place_marker(board, marker, position):
    board[position] = marker


# STEP 4: Win check
def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[7] == board[4] == board[1] == mark) or
            (board[8] == board[5] == board[2] == mark) or
            (board[9] == board[6] == board[3] == mark) or
            (board[7] == board[5] == board[3] == mark) or
            (board[9] == board[5] == board[1] == mark))


# STEP 5: Function that randomly decides which player goes first
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# STEP 6: Board space checking
def space_check(board, position):
    return board[position] == ' '


# STEP 7: Check if the board spaces are full or not
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):  # means if board has empty space
            return False  # means not full

    # BOARD is full if we return true
    return True


# STEP 8: Player chooses the position
def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position (1-9) \n'))

    return position


# STEP 9: Ask to play again?
def replay():
    choice = ''

    while not (choice == 'yes' or choice == 'no'):

        choice = input("Do you want to play again? Enter Yes or No\n").lower()

        if choice not in ['yes', 'no']:
            print("Sorry, wrong input! please choose Yes or No \n")

    if choice == 'yes':
        return True
    else:
        return False

# Step 10: Ready to start game?
def start_game():
    play_game = input('Are you ready to play? Enter Yes or No.\n').lower()

    if play_game not in ['yes', 'no']:
        print("Sorry, wrong input! please choose Yes or No \n")

    if play_game.lower() == 'yes':
        game_on = True
        return game_on
    else:
        game_on = False
        return game_on

# Combining all functions to run the game
print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = start_game()

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! Player 1 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations! Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break