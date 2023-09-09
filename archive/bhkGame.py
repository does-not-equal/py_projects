import random, sys


print('Boulder, Haiku, or Katana')


# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        print('Enter your move: (b)oulder, (h)aiku, (k)atana, or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quits the program.
        if playerMove == 'b' or playerMove == 'h' or playerMove == 'k':
            break # Breaks the player input loop
        print('Type either b, h, k, or q.')

    # Display what the player chose:
    if playerMove == 'b':
        print('Boulder versus...')
    elif playerMove == 'h':
        print('Haiku versus...')
    elif playerMove == 'k':
        print('Katana versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'b'
        print('Boulder')
    elif randomNumber == 2:
        computerMove = 'h'
        print('Haiku')
    elif randomNumber == 3:
        computerMove = 'k'
        print('Katana')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('You tied with the computer.')
        ties = ties + 1
    elif playerMove == 'b' and computerMove == 'k':
        print('You have bested the computer.')
        wins = wins + 1
    elif playerMove == 'h' and computerMove == 'b':
        print('You have bested the computer.')
        wins = wins + 1
    elif playerMove == 'k' and computerMove == 'h':
        print('You have bested the computer.')
        wins = wins + 1
    elif playerMove == 'b' and computerMove == 'h':
        print('You have been bested by the computer.')
        losses = losses + 1
    elif playerMove == 'h' and computerMove == 'k':
        print('You have been bested by the computer.')
        losses = losses + 1
    elif playerMove == 'k' and computerMove == 'b':
        print('You have been bested by the computer.')
        losses = losses + 1
