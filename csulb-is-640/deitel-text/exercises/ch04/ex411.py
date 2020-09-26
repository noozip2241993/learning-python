'''(Guess the Number) Write a script that plays “guess the number.” Choose the
number to be guessed by selecting a random integer in the range 1 to 1000. Do not reveal
this number to the user. Display the prompt "Guess my number between 1 and 1000 with
the fewest guesses:". The player inputs a first guess. If the guess is incorrect, display
"Too high. Try again." or "Too low. Try again." as appropriate to help the player “zero
in” on the correct answer, then prompt the user for the next guess. When the user enters
the correct answer, display "Congratulations. You guessed the number!", and allow the
user to choose whether to play again.'''

'''(Guess-the-Number Modification) Modify the previous exercise to count the number of guesses the player makes. If the number is 10 or fewer, display "Either you know the
secret or you got lucky!" If the player makes more than 10 guesses, display "You should
be able to do better!" Why should it take no more than 10 guesses? Well, with each “good
guess,” the player should be able to eliminate half of the numbers, then half of the remaining
numbers, and so on. Doing this 10 times narrows down the possibilities to a single number.
This kind of “halving” appears in many computer science applications. For example, in the
“Computer Science Thinking: Recursion, Searching, Sorting and Big O” chapter, we’ll present the high-speed binary search and merge sort algorithms, and you’ll attempt the quicksort
exercise—each of these cleverly uses halving to achieve high performance.'''

def guess_the_number():
    import random
    MIN = 1
    MAX = 1000

    PROMPT_GUESS = f'Guess my number between {MIN} and {MAX} with the fewest guesses: '
    PROMPT_GUESS_AGAIN = f'Guess again. My number is between {MIN} and {MAX}: '
    PROMPT_PLAY_AGAIN = 'Would you like to play again? (Y/N): '

    RESPONSE_TOO_HIGH = 'Too high. Try again.'
    RESPONSE_TOO_LOW = 'Too low. Try again.'
    RESPONSE_CORRECT = 'Congratulations. You guessed the number!'
    RESPONSE_LUCKY = 'Either you know the secret or you got lucky!'
    RESPONSE_TOO_MANY = 'You should be able to do better!'
    RESPONSE_END = 'Thank\'s for playing!'

    incorrect = True
    number = random.randint(MIN, MAX + 1)
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

    feedback = RESPONSE_LUCKY
    if attempts > 10:
        feedback = RESPONSE_TOO_MANY

    print(f'{RESPONSE_CORRECT}\nIt took you {attempts} attempts to guess the correct number... {number}.\n{feedback}')

    if input(PROMPT_PLAY_AGAIN).upper() == 'Y':
        guess_the_number()
    
    print(RESPONSE_END)
guess_the_number()