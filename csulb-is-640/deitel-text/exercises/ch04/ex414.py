'''(Computer-Assisted Instruction) Computer-assisted instruction (CAI) refers to the
use of computers in education. Write a script to help an elementary school student learn
multiplication. Create a function that randomly generates and returns a tuple of two 
positive one-digit integers. Use that function’s result in your script to prompt the user 
with a question, such as

    How much is 6 times 7?

For a correct answer, display the message "Very good!" and ask another multiplication
question. For an incorrect answer, display the message "No. Please try again." and let
the student try the same question repeatedly until the student finally gets it right.'''

def rando_int_pair():
    import random
    MIN = 1
    MAX = 9
    return (random.randint(MIN, MAX), random.randint(MIN, MAX))

def test_multiplication():
    test_ints = rando_int_pair()
    incorrect = True

    while incorrect:
        response = int(input(f'How much is {test_ints[0]} times {test_ints[1]}? '))
        answer = test_ints[0] * test_ints[1]
        if response == answer:
            incorrect = False
            print('Very good!')
        else:
            print('No. Please try again.')

    new_try = input(f'Would you like to try another? (Y/N) ')
    if new_try.upper() == 'Y':
        test_multiplication()

test_multiplication()