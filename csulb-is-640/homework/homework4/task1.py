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

def is_prime(number):
    number = int(number)
    factors = []

    for n in range(1, number + 1):
        if number % n == 0:
            factors.append(n)
    
    if len(factors) == 2:
        #print(factors) # for testing porposes show the factors
        return True
    else:
        #print(factors) # for testing porposes show the factors
        return False

def test_is_prime():
    RANDS_COUNT = 6 # tested with a value of 6
    RANDS_MIN = 1 # tested with a value of 1
    RANDS_MAX = 100 # tested with a value of 100

    article = ' ? '
    check = ''
    rands = get_unique_rand_ints(RANDS_COUNT, RANDS_MIN, RANDS_MAX) # live randoms

    # these lists is used while testing
    '''
    TEST1_VALUES = [87, 23, 34, 96, 6, 11]
    PRIMES_UNDER_1000 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
        53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 
        137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 
        223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 
        307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 
        397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 
        487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 
        593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 
        677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 
        787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 
        883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 
        997]
    NON_PRIMES_UNDER_1000 = []
    for i in range(1, 1000):
        if i not in PRIMES_UNDER_1000:
            NON_PRIMES_UNDER_1000.append(i)
    
    rands = TEST1_VALUES #test1 values
    rands = PRIMES_UNDER_1000 #test2 values
    rands = NON_PRIMES_UNDER_1000 #test3 values
    '''

    for number in rands:
        if is_prime(number):
            article = ' '
            #if number not in PRIMES_UNDER_1000:
            #    check = ' WRONG!'
        else:
            article = ' not '
            #if number in PRIMES_UNDER_1000:
            #    check = ' WRONG!'
        
        print(f'The random number {number} is{article}a prime number.{check}')

def get_unique_rand_ints(count, min, max):
    import random
    result = []

    # do some validation to ensure args make sense.
    # ensure all args are integers
    count = int(count)
    min = int(min)
    max = int(max)

    # ensure the min and max are assigned correctly
    if min > max:
        large = min
        small = max
        min = small
        max = large
    
    # ensure the range from min to max is large enough to generate enough unique integers
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
        if this_rand not in result:
            result.append(this_rand)
    
    return result

test_is_prime()