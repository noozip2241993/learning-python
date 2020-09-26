'''(Computer-Assisted Instruction: Varying the Types of Problems) Modify the previous exercise to allow the user to 
pick a type of arithmetic problem to study—1 means addition problems only, 2 means subtraction problems only, 3 means 
multiplication problems only, 4 means division problems only (avoid dividing by 0) and 5 means a random mixture of 
all these types.'''

import random
CORRECT_ANSWER = ['Very good!', 'Nice work!', 'Keep up the good work!']
INCORRECT_ANSWER = ['No. Please try again.', 'Wrong. Try once more.', 'No. Keep trying.']
MAX_DIFFICULTY = 3
PROBLEM_BLOCK_LENGTH = 10

def set_problem_type(no_prompt):
    '''Select the arithmatic problem type. A no_prompt argument value of True selects a problem
     type at random. Otherwise the user will be asked. If asked the user has the option to randomize 
     each problem type in a block of problems'''

    PROBLEM_TYPE_PROMPT = '''Pick a type of arithmetic problem to study:
    1 : addition problems only
    2 : subtraction problems only
    3 : multiplication problems only
    4 : division problems only (answers to 2 decimal places)
    5 : a random mixture of all these types.'''
    OPTION_COUNT = 5
    prob_type = ''

    if no_prompt:
        prob_type = random.randint(1, OPTION_COUNT - 1)
    else:
        while prob_type not in range(1, OPTION_COUNT + 1):
            prob_type = int(input(f'{PROBLEM_TYPE_PROMPT}): '))
    return prob_type

def set_difficulty_level(no_prompt):
    '''Select the difficulty level. Higher difficulty represents larger numbers in the random pool.
    A no_prompt argument value of True selects a difficulty level at random. Otherwise the user will be asked.'''
    diff_level = ''

    if no_prompt:
        diff_level = random.randint(1,{MAX_DIFFICULTY + 1})
    else:
        while diff_level not in range(1, MAX_DIFFICULTY + 1):
            diff_level = int(input(f'Set a difficulty level (1 to {MAX_DIFFICULTY}): '))
    return diff_level

def rando_int_pair(max_exponent):
    '''return a tuple containing two random positive ints. The upper limit for these values is determined by
    the max_exponent argument value. As in:
        MAX = 10**max_exponent - 1'''
    import random
    MIN = 1
    MAX = 10**int(max_exponent) - 1
    return (random.randint(MIN, MAX), random.randint(MIN, MAX))

def test_arithmatic():
    ''' Present a user with a series of arithmatic problems to solve. The user cann't proceed to the next problem 
    until they have correctly solved the current problem. Once the series has been completed, the user is asked if
    they would like to try another set.
    
    At the start of each set the user can determine a difficulty level and what kind of arithmatic problems they 
    want to study.'''

    block_difficulty = set_difficulty_level(False) # ask the user to establish a difficulty level for the block
    block_problem_type = set_problem_type(False) # ask the user to establish a problem type for the block

    for i in range(PROBLEM_BLOCK_LENGTH):
        this_prob_ints = rando_int_pair(block_difficulty)
        this_prob_operator = ''
        this_prob_answer = ''

        if block_problem_type == 5:
            this_prob_type = set_problem_type(True)
        else:
            this_prob_type = block_problem_type

        if this_prob_type == 1:
            this_prob_operator = 'plus'
            this_prob_answer = this_prob_ints[0] + this_prob_ints[1]
        elif this_prob_type == 2:
            this_prob_operator = 'minus'
            this_prob_answer = this_prob_ints[0] - this_prob_ints[1]
        elif this_prob_type == 3:
            this_prob_operator = 'times'
            this_prob_answer = this_prob_ints[0] * this_prob_ints[1]
        elif this_prob_type == 4:
            this_prob_operator = 'divided by'
            this_prob_answer = round(this_prob_ints[0] / this_prob_ints[1], 2)
        else:
            print(f'this_prob_type = {this_prob_type}. This should not be possible.')
        
        incorrect = True
        while incorrect:
            user_response = float(input(f'{i + 1:<2} : How much is {this_prob_ints[0]} {this_prob_operator} {this_prob_ints[1]}? '))
            
            if user_response == float(this_prob_answer):
                incorrect = False
                print(CORRECT_ANSWER[random.randint(0,len(CORRECT_ANSWER)-1)])
            else:
                print(INCORRECT_ANSWER[random.randint(0,len(INCORRECT_ANSWER)-1)])

    new_try = input(f'Would you like to try another {PROBLEM_BLOCK_LENGTH} problems? (Y/N) ')
    if new_try.upper() == 'Y':
        test_arithmatic()

test_arithmatic()