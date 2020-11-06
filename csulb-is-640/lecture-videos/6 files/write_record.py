FILENAME = 'scores.txt'
WRITE_MODE = 'w'

#writing records to a file
with open(FILENAME, WRITE_MODE) as names_file:
    names_file.write('Alice 97\n')
    
    name = 'Bob'
    score = 93
    names_file.write(f'{name} {score}\n')

    names_file.write('Cindy 95\n')