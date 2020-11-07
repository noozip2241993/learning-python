import os

READ_MODE = 'r'
filename = input('Please type the filename: ')

#try first to avoid exceptions
if os.path.isfile(filename):
    with open(filename, READ_MODE) as file:
        print(f'Process {filename}')
        # process the file content here
else:
    print(f'{filename} is not a valid file, please check that you input the correct filename.')

