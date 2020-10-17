# in VS Code Shift+Ctrl+L yets you change all instances of selected characters at once
# Ctrl+/ will toggle comments

def myCeil(number=0):
    in_num = number
    if in_num == int(in_num):
        result = int(in_num)
    else:
        result = int(in_num) + 1
    return result

import math
def moys_ceil(num):
    num_st = int(str(num).split('.')[0])
    x = num % num_st
    if x != 0:
        return num_st + 1
    else:
        return num_st

for i in range(0, 10):
    this_number = 3 + i/10
    print(f'{this_number} : {moys_ceil(this_number)}')


# Was Ying Liu's MS interview question
# write a function to convert a str to an int without using int()
def str_to_int(str_to_convert='345'):
    in_str = str_to_convert
    int_part , _ = in_str.split('.')
    ZERO = ord('0')
    int_place = len(int_part)
    result = 0
    # construct the int part
    for char in int_part:
        int_place -= 1
        char_to_int = ord(char) - ZERO
        multiple = 10**(int_place)
        result += char_to_int * multiple
    return result



test_str_to_int = '345.99'
print(f'Original : {test_str_to_int} | {type(test_str_to_int)}')

my_result = str_to_int(test_str_to_int)
print(f'My function : {my_result} | {type(my_result)}')

built_in_result = str_to_int(test_str_to_int)
print(f'int() function : {built_in_result} | {type(built_in_result)}')