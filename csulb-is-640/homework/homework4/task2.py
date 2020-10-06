'''
Create a function that randomly generates and returns a tuple of 
two positive one-digit integers. Then prompt the user for the 
multiplication of the two numbers. For example, if the generated 
number is 3 and 7, the prompt message is 

How much is 3 times 7? 

Then compare the user answer with the correct result. If the answer 
is correct, display a message “done”. Otherwise, if the user input 
20, prompt:

“3 times 7 is not 20, please try again: “

Keep asking the user input until it type the correct answer.

'''
def get_rand_ints(count=1, min=1, max=20, unique=False, testing=False):
    '''
    Based on given arguments, this function returns a list of random integers.\n
        count should be a non-negative integer\n
        min and max should each be any integer\n
        unique and testing should each be boolean values\n
    Passing invalid arguments will result in an empty list being returned.\n
    If unique values are requested and count is greater than the inclusive range
    of min and max then max will be changed to allow for the required count of 
    unique values to be possible.
    '''
    import random
    result = []

    # do some validation to ensure args make sense.
    try:
        # ensure all args are cast to the correct datatypes. 
        count = int(count)
        min = int(min)
        max = int(max)
        unique = bool(unique)
        testing = bool(testing)

        # ensure the count is non-negative
        if count < 0:
            raise ValueError('A count argument of {count} was passed to get_random_ints. Count cannot be a negative number.')
    except:
        # if correct casting is not possible communicate this
        # to the user and return and empty list
        print('Invalid arguments passed to get_rand_ints()')
        print('Returning an empty list')
        return []

    # ensure the min and max are assigned correctly
    if min > max:
        large = min
        small = max
        min = small
        max = large
    
    # if unique = True, ensure the range from min to max is large enough to generate enough unique integers
    if unique:
        range = max - min + 1
        if range < count:
            max = min + count
            range = max - min + 1
            print(f'Your range is too small to provide {count} unique random integers. Will proceed with\n \
                count = {count}\n \
                min = {min}\n \
                max = {min} + {count} = {max}\n \
            now the range of {range} can possibly generate {count} unique random integers')

    # generate random integers between the min to max arguments (inclusive)
    # add the this_rand to the result list 
    # (if unique = True only if it isn't already there)
    # repeat until the length of the result list equals the count argument.
    while len(result) < count:
        this_rand = random.randint(int(min), int(max))
        if unique:
            if this_rand not in result:
                result.append(this_rand)
        else:
            result.append(this_rand)
    
    if testing: print(result)

    return result

def test_multiplication(min=1, max=9):
    '''
    This function presents the user with a multiplication problem
    over and over until they input the correct product.
    '''

    multiples = tuple(get_rand_ints(2, min, max, False, False))
    correct_answer = multiples[0] * multiples[1]
    user_input = ''
    prompt = f'How much is {multiples[0]} times {multiples[1]}? '

    while user_input != correct_answer:
        if user_input != '':
            prompt = f'{multiples[0]} times {multiples[1]} is not {user_input}, please try again: '
        user_input = int(input(prompt))

    print('done')

test_multiplication()