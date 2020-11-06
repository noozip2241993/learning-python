import os

FILENAME = 'scores.txt'
TEMP_FILE = 'temp'
READ_MODE = 'r'
WRITE_MODE = 'w'

# open a source file for read
source_file = open(FILENAME, READ_MODE)

# open a temp file for write
temp_file = open(TEMP_FILE, WRITE_MODE)

# read data from the source file, make required changes and save to the temp file
with source_file, temp_file:
    for line in source_file:
        name, score = line.split()

        if name == 'Bob':
            score = 90
        
        if name == 'Cindy':
            name = 'Cynthia'
        
        temp_file.write(f'{name} {score}\n')

# remove the source file
os.remove(FILENAME)

# rename the temp file to the name of the source file
os.rename(TEMP_FILE, FILENAME)
