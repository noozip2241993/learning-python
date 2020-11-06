import os

FILE1 = 'test1.txt'
FILE2 = 'test2.txt'
WRITE_MODE = 'w'

def check_existence(message):
    is_exist_1 = os.path.exists(FILE1)
    is_exist_2 = os.path.exists(FILE2)
    print(f'{message} {FILE1} exists: {is_exist_1}, {FILE2} exists: {is_exist_2}')

with open(FILE1, WRITE_MODE) as names_file:
    names_file.write('test data\n')
check_existence('After create')

os.rename(FILE1, FILE2)
check_existence('After rename')

os.remove(FILE2)
check_existence('After remove')
    