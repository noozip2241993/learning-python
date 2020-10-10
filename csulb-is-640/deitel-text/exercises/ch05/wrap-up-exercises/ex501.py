'''
(What’s Wrong with This Code?)

print('c) name = 'amanda' 
name[0] = 'A'
d) numbers = [1, 2, 3, 4, 5]
numbers[3.4]
e) student_tuple = ('Amanda', 'Blue', [98, 75, 87])
student_tuple[0] = 'Ariana'
f) ('Monday', 87, 65) + 'Tuesday'
g) 'A' += ('B', 'C')
h) x = 7
del x
print(x)
i) numbers = [1, 2, 3, 4, 5]
numbers.index(10)
j) numbers = [1, 2, 3, 4, 5]
numbers.extend(6, 7, 8)
k) numbers = [1, 2, 3, 4, 5]
numbers.remove(10)
l) values = []
values.pop()
'''

print('What, if anything, is wrong with each of the following code segments?')

print('\na) day, high_temperature = (\'Monday\', 87, 65)')
try:
    day, high_temperature = ('Monday', 87, 65)
    print(day)
    print(high_temperature)
except:
    print('the tuple has three elements but only two are assigned.')

print('\nb) numbers = [1, 2, 3, 4, 5]\nnumbers[10]')
try:
    numbers = [1, 2, 3, 4, 5]
    numbers[10]
except:
    print('the list numbers has a len of 5 with a max index of 4, numbers[10] \
attempts to call for an item in numbers at an index that does not exist.')

try:
    print('\nc) name = \'amanda\' \nname[0] = \'A\'')
    name = 'amanda'
    name[0] = 'A'
except:
    print('strings are not mutable. Their characters cannot be changed.')

try:
    print('d) numbers = [1, 2, 3, 4, 5] \nnumbers[3.4]')
    numbers = [1, 2, 3, 4, 5]
    numbers[3.4]
except:
    print('float values are not valid list indexes.')

try:
    print('e) student_tuple = (\'Amanda\', \'Blue\', [98, 75, 87]) \nstudent_tuple[0] = \'Ariana\'')
    student_tuple = ('Amanda', 'Blue', [98, 75, 87])
    student_tuple[0] = 'Ariana'
except:
    print('Tuple\'s are not mutable. Their elements can not be changed.')

try:
    print('f) (\'Monday\', 87, 65) + \'Tuesday\'')
    print(('Monday', 87, 65))
    print(('Monday', 87, 65) + 'Tuesday')
except:
    print('Tuple\'s are not mutable.')

try:
    print("'A' += ('B', 'C')")
    #'A' += ('B', 'C')
except:
    print("syntax error. 'A' is not assignable"  )

try:
    print("h) x = 7\ndel x\nprint(x)")
    x = 7
    del x
    print(x)
except:
    print("'print(x)' calls a variable after it has been deleted.")

try:
    print("i) numbers = [1, 2, 3, 4, 5]\nnumbers.index(10)")
    numbers = [1, 2, 3, 4, 5]
    numbers.index(10)
except:
    print("the list 'numbers' does not have 10 as an element therefore .index(10) does not exist either.")

try:
    print("j) numbers = [1, 2, 3, 4, 5]\nnumbers.extend(6, 7, 8)")
    numbers = [1, 2, 3, 4, 5]
    numbers.extend(6, 7, 8)
except:
    print(".extend takes in a sequence item as an argument. 'numbers.extend(6, 7, 8)' should be numbers.extend([6, 7, 8])")

try:
    print("k) numbers = [1, 2, 3, 4, 5]\nnumbers.remove(10)")
    numbers = [1, 2, 3, 4, 5]
    numbers.remove(10)
except:
    print("The value '10' is not on the list")

try:
    print("l) values = []\nvalues.pop()")
    values = []
    values.pop()
except:
    print("Can't .pop from an empty list.")