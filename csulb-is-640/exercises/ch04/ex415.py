'''(Computer-Assisted Instruction: Reducing Student Fatigue) Varying the computer’s 
responses can help hold the student’s attention. Modify the previous exercise so that
various comments are displayed for each answer. Possible responses to a correct answer
should include 'Very good!', 'Nice work!' and 'Keep up the good work!' Possible 
responses to an incorrect answer should include 'No. Please try again.', 'Wrong. Try
once more.' and 'No. Keep trying.' Choose a number from 1 to 3, then use that value
to select one of the three appropriate responses to each correct or incorrect answer.'''

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