'''
Write a script that displays the following triangle patterns separately, one below the other. 
Separate each pattern from the next by one blank line. Use for loops to generate the patterns. 
Display all asterisks (*) with a single statement of the form
    print('*', end='')
which causes the asterisks to display side by side. [Hint: For the last two patterns, begin
each line with zero or more space characters.]
'''

CHAR = '*'
PAD = ' '

#pattern a
print('(a)')
for z in range(0, 10):
    for y in range(0, z + 1):
        print(CHAR, end='')
    print('')
print('')

#pattern b
print('(b)')
for z in range(0, 10):
    for y in range(0, 10 - z):
        print(CHAR, end='')
    print('')
print('')

#pattern c
print('(c)')
for z in range(0, 10):
    for y in range(0, z):
        print(PAD, end='')
    for x in range(z, 10):
        print(CHAR, end='')
    print('')
print('')

#pattern d
print('(d)')
for z in range(0, 10):
    for y in range(0, 10 - z - 1):
        print(PAD, end='')
    for x in range(10 - z - 1, 10):
        print(CHAR, end='')
    print('')
print('')