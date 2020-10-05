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
def get_rand_ints(count=2, min=1, max=9, unique=False, testing=False):
    import random
    result = []

    # do some validation to ensure args make sense.
    # ensure all args are cast to the correct datatypes
    count = int(count)
    min = int(min)
    max = int(max)
    unique = bool(unique)
    testing = bool(testing)

    # ensure the min and max are assigned correctly
    if min > max:
        large = min
        small = max
        min = small
        max = large
    
    # if unique = True, ensure the range from min to max is large enough to generate enough unique integers
    if unique:
        range = max - min + 1 # adding one represents the inclusive range 
        if max - min < count:
            max = min + count
            range = max - min + 1
            print(f'Your range is too small to provide {count} unique random integers. Will proceed with\n \
                count = {count}\n \
                min = {min}\n \
                max = {min} + {count} = {max}\n \
            now the range of {range} can possibly generate {count} unique random integers')

    # generate random integers between the min to max arguments (inclusive)
    # add the this_rand to the result list only if it isn't already there
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

def test_multiplication():
    multiples = tuple(get_rand_ints(2, 1, 9, False, False))
    correct_answer = multiples[0] * multiples[1]
    user_input = ''
    prompt = f'How much is {multiples[0]} times {multiples[1]}? '

    while user_input != correct_answer:
        if user_input != '':
            prompt = f'{multiples[0]} times {multiples[1]} is not {user_input}, please try again: '
        user_input = int(input(prompt))

    print('done')

test_multiplication()