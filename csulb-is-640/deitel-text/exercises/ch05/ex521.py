'''
5.21 (Computer-Assisted Instruction: Reducing Student Fatigue) Re-implement
Exercise 4.15 to store the computer’s responses in lists. Use random-number generation
to select responses using random list indices.
'''
import random
CORRECT_ANSWER = ['Very good!', 'Nice work!', 'Keep up the good work!']
INCORRECT_ANSWER = ['No. Please try again.', 'Wrong. Try once more.', 'No. Keep trying.']

def rando_int_pair():
    import random
    MIN = 1
    MAX = 9
    return (random.randint(MIN, MAX), random.randint(MIN, MAX))

def test_multiplication():
    test_ints = rando_int_pair()
    incorrect = True

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