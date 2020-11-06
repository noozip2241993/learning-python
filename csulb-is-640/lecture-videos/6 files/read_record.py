FILENAME = 'scores.txt'
READ_MODE = 'r'

#reading records from a file
with open(FILENAME, READ_MODE) as names_file:
    for line in names_file:
        # meaningful fields
        name, score = line.split() #default delimiter is whitespace chars
        print(f'Name: {name}\t Score: {score}')

        # # generic fields
        # fields = line.split()
        # print(f'Field 1: {fields[0]}, Field 2: {fields[1]}')