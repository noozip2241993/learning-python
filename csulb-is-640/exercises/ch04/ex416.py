'''(Computer-Assisted Instruction: Difficulty Levels) Modify the previous exercise to
allow the user to enter a difficulty level. At a difficulty level of 1, the program should use
only single-digit numbers in the problems and at a difficulty level of 2, numbers as large
as two digits.'''

import random
CORRECT_ANSWER = ['Very good!', 'Nice work!', 'Keep up the good work!']
INCORRECT_ANSWER = ['No. Please try again.', 'Wrong. Try once more.', 'No. Keep trying.']
MAX_DIFFICULTY = 3

def difficulty_level():
    ''' Ask the user to select the difficulty level. Higher difficulty represents larger
    numbers in the random pool.'''
    user_input = ''
    while user_input not in range(1, MAX_DIFFICULTY + 1):
        user_input = int(input(f'Set a difficulty level (1 to {MAX_DIFFICULTY}): '))
    return user_input

def rando_int_pair():
    import random
    MIN = 1
    MAX = 10**difficulty_level() - 1
    return (random.randint(MIN, MAX), random.randint(MIN, MAX))

def test_multiplication():
    incorrect = True
    test_ints = rando_int_pair()

    while incorrect:
        user_response = int(input(f'How much is {test_ints[0]} times {test_ints[1]}? '))
        answer = test_ints[0] * test_ints[1]
        if user_response == answer:
            incorrect = False
            print(CORRECT_ANSWER[random.randint(0,len(CORRECT_ANSWER)-1)])
        else:
            print(INCORRECT_ANSWER[random.randint(0,len(INCORRECT_ANSWER)-1)])

    new_try = input(f'Would you like to try another? (Y/N) ')
    if new_try.upper() == 'Y':
        test_multiplication()

test_multiplication()