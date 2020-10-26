'''
5.18 (Summing the Triples of the Even Integers from 2 through 10) Starting with a list
containing 1 through 10, use filter, map and sum to calculate the total of the triples of
the even integers from 2 through 10. Reimplement your code with list comprehensions
rather than filter and map.
'''

#via lambdas and map / filter
numbers = [n for n in range(1, 10)]
numbers = list(map(lambda x: x ** 3, filter(lambda x: x % 2 == 0, numbers)))
print(numbers)
print(sum(numbers))

#via list comprehension
print(sum([n ** 3 for n in range(1, 10) if n % 2 == 0]))