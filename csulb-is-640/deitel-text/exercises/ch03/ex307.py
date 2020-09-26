'''In Exercise 2.8, you wrote a script to calculate the squares and cubes of the numbers from 0 through 5, 
then printed the resulting values in table format. Reimplement your script using a for loop and the f-string 
capabilities you learned in this chapter to produce the following table with the numbers right aligned in 
each column.
    |   number|   square|   cube|
    |--------:|--------:|------:|
    | 0       | 0       | 0     |
    | 1       | 1       | 1     |
    | 2       | 4       | 8     |
    | 3       | 9       | 27    |
    | 4       | 16      | 64    |
    | 5       | 25      | 125   |'''

col1_head = 'number'
col2_head = 'square'
col3_head = 'cube'
col1_len = len(col1_head)
col2_len = len(col2_head)
col3_len = len(col2_head)

print(f'{col1_head}\t{col2_head}\t{col3_head}')
my_int = 0

for x in range(0,6):
    line_str = f'{my_int**1:>6}\t'
    line_str += f'{my_int**2:>6}\t'
    line_str += f'{my_int**3:>4}'
    print(line_str)
    my_int += 1