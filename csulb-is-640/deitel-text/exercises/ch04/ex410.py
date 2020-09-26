'''(Guess the Number) Write a script that plays “guess the number.” Choose the
number to be guessed by selecting a random integer in the range 1 to 1000. Do not reveal
this number to the user. Display the prompt "Guess my number between 1 and 1000 with
the fewest guesses:". The player inputs a first guess. If the guess is incorrect, display
"Too high. Try again." or "Too low. Try again." as appropriate to help the player “zero
in” on the correct answer, then prompt the user for the next guess. When the user enters
the correct answer, display "Congratulations. You guessed the number!", and allow the
user to choose whether to play again.'''

def guess_the_number():
    import random
    PROMPT_GUESS = 'Guess my number between 1 and 1000 with the fewest guesses: '
    PROMPT_GUESS_AGAIN = 'Guess again. My number is between 1 and 1000: '
    PROMPT_PLAY_AGAIN = 'Would you like to play again? (Y/N) '
    RESPONSE_TOO_HIGH = 'Too high. Try again.'
    RESPONSE_TOO_LOW = 'Too low. Try again.'
    RESPONSE_CORRECT = 'Congratulations. You guessed the number!'

    incorrect = True
    number = random.randint(1,1000)
    guess = int(input(PROMPT_GUESS))
    attempts = 1

    while incorrect:
        if guess > number:
            print(RESPONSE_TOO_HIGH)
            guess = int(input(PROMPT_GUESS_AGAIN))
            attempts += 1
        elif guess < number:
            print(RESPONSE_TOO_LOW)
            guess = int(input(PROMPT_GUESS_AGAIN))
            attempts += 1
        else:
            incorrect = False
    print(f'{RESPONSE_CORRECT}\nIt took you {attempts} attempts to guess the correct number... {number}.\nThank\'s for playing!')

    if input(PROMPT_PLAY_AGAIN).upper() == 'Y':
        guess_the_number()

guess_the_number()