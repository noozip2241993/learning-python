FILENAME = 'names.txt'
WRITE_MODE = 'w'

with open(FILENAME, WRITE_MODE) as names_file:
    names_file.write('Alice\n')
    names_file.write('Bob\n')
    names_file.write('Cindy\n')