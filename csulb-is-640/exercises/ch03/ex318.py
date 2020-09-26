'''
Modify your script from Exercise 3.17 to display all four patterns side-by-side 
(as shown above) by making clever use of nested for loops. Separate each triangle 
from the next by three horizontal spaces. [Hint: One for loop should control the 
row number. Its nested for loops should calculate from the row number the
appropriate number of asterisks and spaces for each of the four patterns.]
'''

#initializaion
LABELS = ['(a)', '(b)', '(c)', '(d)']
CHARS = ['*', ' ']
MAX_ROWS = 10
PATTERN_WIDTH = 10
SEP_WIDTH = 3
MAX_COLS = (len(LABELS) * PATTERN_WIDTH) + (len(LABELS) - 1) * SEP_WIDTH
NEXT_ROW_DIRECTION =    [1,  0, -1,  1,  0, -1]

char_index = 0
char_toggles =  [1, 13, 23, 26, 36, 48]

#processing
#print header
header = ''
for i in range(len(LABELS)):
    header += f'{LABELS[i]}          '
print(header)

#print rows
# this process depends on predefining a set of column position values at
# which the character printed toggles back and forth between two values.
for r in range(0, MAX_ROWS):
    for c in range(0, MAX_COLS):
        # as we loop through the column positions in each row
        # 1) check whether we should toggle to the other character, if yes do so
        if c in char_toggles:
            char_index = (char_index + 1) % 2
        # 2) print a character
        print(CHARS[char_index], end='')
    
    #change toggle points based on the cooresponding value in NEXT_ROW_DIRECTION.
    next_toggles = []
    for i in range(0, len(char_toggles)):
        next_toggles.append(char_toggles[i] + NEXT_ROW_DIRECTION[i])
    char_toggles = next_toggles
    print('')
print('')

