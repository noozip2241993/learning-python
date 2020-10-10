print("5.8 (Sieve of Eratosthenes)\n\
A prime number is an integer greater than 1 that’s evenly divisible only by itself and 1.\n\
The Sieve of Eratosthenes is an elegant, straightforward method of finding prime numbers.\n\
The process for finding all primes less than 1000 is:\n\
a) Create a 1000-element list primes with all elements initialized to True. List elements\n\
    with prime indices (like 2, 3, 5, 7, 11, …) will remain True. All other list elements\n\
    will eventually be set to False.\n\
b) Starting with index 2, if a given element is True iterate through the rest of the\n\
    list and set to False every element in primes whose index is a multiple of the\n\
    index for the element we’re currently processing. For list index 2, all elements\n\
    beyond element 2 in the list that have indices which are multiples of 2 (i.e., 4,\n\
    6, 8, 10, …, 998) will be set to False.\n\
c) Repeat Step (b) for the next True element. For list index 3 (which was initialized to True),\n\
    all elements beyond element 3 in the list that have indices which are multiples of 3\n\
    (i.e., 6, 9, 12, 15, …, 999) will be set to False; and so on. A subtle observation \n\
    (think about why this is true): The square root of 999 is 31.6, you’ll need to test\n\
    and set to False only all multiples of 2, 3, 5, 7, 9, 11, 13, 17, 19, 23, 29 and 31.\n\
    This will significantly improve the performance of your algorithm, especially if you\n\
    decide to look for large prime numbers.\n\
When this process completes, the list elements that are still True indicate that the index is\n\
a prime number. These indices can be displayed. Use a list of 1000 elements to determine\n\
and display the prime numbers less than 1000. Ignore list elements 0 and 1. [As you work\n\
through the book, you’ll discover other Python capabilities that will enable you to cleverly\n\
reimplement this exercise.]")

import time

def get_primes_a(greater_than = 0, less_than=1000):
    #a) Create a 1000-element list primes with all elements initialized to True. List elements
    #    with prime indices (like 2, 3, 5, 7, 11, …) will remain True. All other list elements
    #    will eventually be set to False.")
    import math
    
    efficient_less_than = int(math.sqrt(less_than - 1) // 1)
    primes = []
    result = []
    for i in range(greater_than, less_than):
        primes.append(True)

    #b) Starting with index 2, if a given element is True iterate through the rest of the
    #    list and set to False every element in primes whose index is a multiple of the
    #    index for the element we’re currently processing. For list index 2, all elements
    #    beyond element 2 in the list that have indices which are multiples of 2 (i.e., 4,
    #    6, 8, 10, …, 998) will be set to False.

    for i, is_prime in enumerate(primes):
        if i >= 2 and is_prime == True:
            result.append(i)
            if i == efficient_less_than:
                print('',end='')
            if i <= efficient_less_than:
                for j, is_prime in enumerate(primes):
                    if j > i and j % i == 0:
                        primes[j] = False

    #c) Repeat Step (b) for the next True element. For list index 3 (which was initialized to True),
    #    all elements beyond element 3 in the list that have indices which are multiples of 3
    #    (i.e., 6, 9, 12, 15, …, 999) will be set to False; and so on. A subtle observation
    #    (think about why this is true): The square root of 999 is 31.6, you’ll need to test
    #    and set to False only all multiples of 2, 3, 5, 7, 9, 11, 13, 17, 19, 23, 29 and 31.
    #    This will significantly improve the performance of your algorithm, especially if you
    #    decide to look for large prime numbers.
    
    return result

def get_primes_b(greater_than = 0, less_than=1000):
    #a) Create a 1000-element list primes with all elements initialized to True. List elements
    #    with prime indices (like 2, 3, 5, 7, 11, …) will remain True. All other list elements
    #    will eventually be set to False.")
    import math

    primes = []
    result = []
    for i in range(greater_than, less_than):
        primes.append(True)

    #b) Starting with index 2, if a given element is True iterate through the rest of the
    #    list and set to False every element in primes whose index is a multiple of the
    #    index for the element we’re currently processing. For list index 2, all elements
    #    beyond element 2 in the list that have indices which are multiples of 2 (i.e., 4,
    #    6, 8, 10, …, 998) will be set to False.

    for i, is_prime in enumerate(primes):
        if i >= 2 and is_prime == True:
            result.append(i)
            for j, is_prime in enumerate(primes):
                if j > i and j % i == 0:
                    primes[j] = False

    #c) Repeat Step (b) for the next True element. For list index 3 (which was initialized to True),
    #    all elements beyond element 3 in the list that have indices which are multiples of 3
    #    (i.e., 6, 9, 12, 15, …, 999) will be set to False; and so on. A subtle observation
    #    (think about why this is true): The square root of 999 is 31.6, you’ll need to test
    #    and set to False only all multiples of 2, 3, 5, 7, 9, 11, 13, 17, 19, 23, 29 and 31.
    #    This will significantly improve the performance of your algorithm, especially if you
    #    decide to look for large prime numbers.
    
    return result

MAX = 1000

start = time.time()
print(get_primes_a(less_than=MAX))
end = time.time()
elapsed_a = end - start

start = time.time()
print(get_primes_b(less_than=MAX))
end = time.time()
elapsed_b = end - start

print(f'elapsed_a: {elapsed_a} | {elapsed_a / elapsed_b}')
print(f'elapsed_b: {elapsed_b} | {elapsed_b / elapsed_a}')