'''
A prime number is a number that is only evenly divisble by itself and 1.
For example, the number 5 is prime because it can only be evenlly divided by 1
and 5. The number 6, however, is not prime because it can be divided evenly
by 2 and 3.

Write a Boolean function named is_prime which takes an integer as an argument
and returns true if the argument is a prime number, or false otherwise. 

Then write a program that generates six random number between 1 and 100 (inclusive) 
and print out the result like the following (each run will have six different 
random numbers):

The random number 87 is a not a prime number.
The random number 23 is a prime number.
The random number 34 is a not a prime number.
The random number 96 is a not prime number.
The random number 6 is a not a prime number.
The random number 11 is a prime number.
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

def is_prime(number=1,verbose=False):
    '''
    Given an integer, this function returns a boolean value indicating whether 
    that integer is a prime number.\n
    If True, the verbose arg will show the factors for the number before returning. 
    '''
    number = int(number)
    factors = []

    for n in range(1, number + 1):
        if number % n == 0:
            factors.append(n)
    
    if verbose: print(factors) # show the factors

    if len(factors) == 2:
        return True
    else:
        return False

def test_is_prime():
    '''
    This function tests whether a series of 6 random unique integers between 1 and 100 (inclusive)
    are prime numbers using the is_prime function.
    '''

    RANDS_COUNT = 6
    RANDS_MIN = 1 #inclusive
    RANDS_MAX = 100 #inclusive
    RANDS_UNIQUE = True

    rands = get_rand_ints(RANDS_COUNT, RANDS_MIN, RANDS_MAX, RANDS_UNIQUE, False)
    
    article = ' !ERROR! '
    for number in rands:
        if is_prime(number,False):
            article = ' '
        else:
            article = ' not '
        
        print(f'The random number {number} is{article}a prime number.')

test_is_prime()