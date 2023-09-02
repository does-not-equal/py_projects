# This is a guess the number game.

import random

secretNumber = random.randint (1, 20)
print ('Guess the number between 1 and 20')

# Ask the play to guess 5 times.
for guessesTaken in range (1, 6):
    print ('Please take a guess.')
    guess = int (input())


    if guess < secretNumber:
        print ('Your guess is too low')
    elif guess > secretNumber:
        print ('Your guess is too high')
    else:
        break # This condition is the correct guess.

if guess == secretNumber:
    print ('Good job. You guessed my number in ' + str (guessesTaken) + ' guesses.')
else:
    print ('That is not correct. The number was ' + str (secretNumber))
