FILENAME = 'names.txt'
READ_MODE = 'r'

with open(FILENAME, READ_MODE) as names_file:
    #nice way
    for line in names_file:
        text_content = line.rstrip('\n')
        print(text_content)

    # #ugly way - error prone
    # line = names_file.readline()
    # while line != '':
    #     text_content = line.rstrip('\n')
    #     print(text_content)
    #     line = names_file.readline()

    # #read all lines to a list. not great for large files.
    # lines = names_file.readlines()
    # for line in lines:
    #     print(line.rstrip('\n'))

        