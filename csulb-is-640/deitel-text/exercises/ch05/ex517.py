'''
5.17 (Filter/Map Performance) With regard to the following code:
    numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
    list(map(lambda x: x ** 2,
    filter(lambda x: x % 2 != 0, numbers)))

    a) How many times does the filter operation call its lambda argument?
    b) How many times does the map operation call its lambda argument?
    c) If you reverse the filter and map operations, how many times does the map operation call its lambda argument?

To help you answer the preceding questions, define functions that perform the same tasks
as the lambdas. In each function, include a print statement so you can see each time the
function is called. Finally, replace the lambdas in the preceding code with the names of
your functions.
'''

def get_rando_numbers(count=100, min=1, max=20):
    from random import randint
    COUNT = count
    START = min
    END = max
    return [randint(START, END) for x in range(COUNT)]

def square_it(x):
    #print('maps square_it called')
    return x**2

def is_odd(x):
    result = False
    if x % 2 != 0:
        result = True
    #print('filters is_odd called')
    return result

def lambda_performance_test(verbose=False):
    import time

    numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
    numbers = get_rando_numbers()

    #method a
    start_time = time.time()

    list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers)))

    end_time = time.time()
    duration_a = end_time - start_time

    #method b
    start_time = time.time()

    list(map(square_it, filter(is_odd, numbers)))

    end_time = time.time()
    duration_b = end_time - start_time
    #'a) How many times does the filter operation call its lambda argument? 10')
    #'b) How many times does the map operation call its lambda argument? 5')

    #method c
    start_time = time.time()

    list(filter(is_odd, map(square_it, numbers)))

    end_time = time.time()
    duration_c = end_time - start_time
    #a) How many times does the filter operation call its lambda argument? 10')
    #'b) How many times does the map operation call its lambda argument? 10')


    durations = [duration_a, duration_b, duration_c]

    if verbose:
        print(f'with lambdas: {duration_a}')
        print(f'no lambdas map|filter: {duration_b}')
        print(f'no lambdas filter|map: {duration_c}')
    
    return durations

def stress_test(func, observations=100):
    # given a function and a number of observations
    # run that function over and over and return a
    # list of it's output for each time it ran.
    # designed for functions that return a list
    # of elapsed durations for the runtime of three
    # blocks of code. 
    results = []
    for i in range(observations):
        results.append(func())
    return results

# run the stress test
test_results = stress_test(lambda_performance_test, 1000)

#collate the results
method_a_results = [(x[0]) for x in test_results]
method_b_results = [(x[1]) for x in test_results]
method_c_results = [(x[2]) for x in test_results]

#generate test result stats
import statistics as stats
n = len(test_results) #observations
mean_a = stats.mean(method_a_results) #average execution time for method_a
mean_b = stats.mean(method_b_results) #average execution time for method_b
mean_c = stats.mean(method_c_results) #average execution time for method_c

#report the results out
print(f'observations (n): {n}')
print(f'average execution time for method a: {mean_a:.6f}')
print(f'average execution time for method b: {mean_b:.6f}')
print(f'average execution time for method c: {mean_c:.6f}')