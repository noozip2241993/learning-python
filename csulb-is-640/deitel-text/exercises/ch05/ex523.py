'''
5.23 (Functional-Style Programming: Order of filter and map Calls) 
When combining filter and map operations, the order in which they’re performed matters. 
Consider a list numbers containing 10, 3, 7, 1, 9, 4, 2, 8, 5, 6 and the following code:

    In [1] : numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
    In [2] : list(map(lambda x: x * 2,
        ...: filter(lambda x: x % 2 == 0, numbers)))
        ...:
    Out[3] : [20, 8, 4, 16, 12]


Reorder this code to call map first and filter second. What happens and why?
'''

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

out_list = list(map(lambda x: x * 2, filter(lambda  x: x % 2 == 0, numbers)))
print(out_list)
print('Calling filter frist eliminates all odd values from the list \'numbers\'\nthen multiplies the remaining values by 2.')

out_list = list(filter(lambda  x: x % 2 == 0, map(lambda x: x * 2, numbers)))
print(out_list)
print('Calling map first multiplies all values by 2. The odd values on the list \'numbers\' become even \nthen filter tries to eliminate all odd values, of which there are none.')