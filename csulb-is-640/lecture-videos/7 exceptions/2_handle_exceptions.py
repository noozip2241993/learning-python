import sys
FILENAME = 'test.txt'

try:
    with open(FILENAME) as file:
        pass #process file data here
except OSError as error:
    print(f'Unable to open file {FILENAME}. Error message: {error}')

try:
    # all statements in this block are part of the exception handling
    number = 1 / 0
    int('abc')
except OSError as error:
    print(f'Unable to open file {FILENAME}. Error message: {error}')
except ValueError as error:
    print(f'Value error message: {error}')
# except ZeroDivisionError as error:
#     print(f'Division error message: {error}')
except:
    error = sys.exc_info()[0] #get error info
    print(f'Unexpected error: {error}')
else:
    print('no exceptions')
finally:
    print('this always executes') #typically a place to release system resources

print('After the handling code, program keeps running.')