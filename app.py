options = ['rock', 'paper', 'scissors']
scorePlayer1 = 0
scorePlayer2 = 0
turnsPlayed = 0

# create a function that returns a random element from the list 'options'
def get_random_option(options):
    # import the 'random' module
    import random
    # return a random element from the list 'options'
    return random.choice(options)

# create a function that returns the winner of the game
def get_winner(selection1, selection2):
    player1Msg = 'Player 1 wins.'
    player2Msg = 'AI wins.'
    global turnsPlayed
    global scorePlayer2
    turnsPlayed += 1
    def player_1_win_msg():
        global scorePlayer1
        scorePlayer1 += 100
        return player1Msg
    
    # if 'selection1' is equal to 'selection2' return 'draw'
    if selection1 == selection2:
        return selection1 + ' vs ' + selection2 + ' = draw'
    # if 'selection1' is equal to 'rock' and 'selection2' is equal to 'scissors' return 'selection1'
    elif selection1 == 'rock' and selection2 == 'scissors':
        return player_1_win_msg()
    # if 'selection1' is equal to 'paper' and 'selection2' is equal to 'rock' return 'selection1'
    elif selection1 == 'paper' and selection2 == 'rock':
        return player_1_win_msg()
    # if 'selection1' is equal to 'scissors' and 'selection2' is equal to 'paper' return 'selection1'
    elif selection1 == 'scissors' and selection2 == 'paper':
        return player_1_win_msg()
    # in any other case return 'selection2'
    else:
        scorePlayer2 += 100
        return player2Msg
    

def get_final_winner():
    print('Thanks for playing! You played ' + str(turnsPlayed) + ' turns. ')
    if scorePlayer1 > scorePlayer2:
        print('The winner is Player 1 with a score of: ' + str(scorePlayer1))
    elif scorePlayer1 < scorePlayer2:
        print('The winner is AI with a score of: ' + str(scorePlayer2))
    else:
        print('There is a draw with a score of: ' + str(scorePlayer1))
    
    
def new_game():
    # ask for text input in the terminal
    selection1 = input('Enter your selection: ')
    # transform 'selection1' to lowercase
    selection1 = selection1.lower()

    # validate if 'selection1' is truthy and one of the following strings 'rock', 'paper', 'scissors'
    if selection1 and selection1 in options:
        selection2 = get_random_option(options)
        print('AI selected: ' + selection2)
        print(get_winner(selection1, selection2))
        
    else:
        print('invalid input')
        new_game()

def app():
    new_game()
    print('Would you like to play again?')
    askNewGame = input('y/n: ')
    askNewGame = askNewGame.lower()
    if askNewGame and askNewGame in ['y', 'yes']:
        app()
    else:
        get_final_winner()


app()