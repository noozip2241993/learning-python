'''Modify the script of Fig. 3.3 to validate its inputs. For any input, 
if the value entered is other than 1 or 2, keep looping until the user enters a correct 
value. Use one counter to keep track of the number of passes, then calculate the number 
of failures after all the user’s inputs have been received.'''

REQ_INPUT_COUNT = 2

#Validate input
valid_input = False
tot_invalid_trys = 0
while not valid_input:
    init_invalid_try = tot_invalid_trys
    numbers = []

    #get user input
    for i in range(REQ_INPUT_COUNT):
        this_input = int(input('Enter an integer number, must be either 1 or 2: '))
        numbers.append(this_input)
    #apply validation rules and count invalid tries
    for n in numbers:
        if n != 1 and n != 2:
            print (n, 'is invalid. Must be either 1 or 2.')
            tot_invalid_trys += 1
    #check whether invalid try occured and exit loop if not
    if tot_invalid_trys == init_invalid_try:
        valid_input = True

#Sum the numbers
total = 0
for n in numbers:
    total += n

#Report results
print('The sum of', numbers, 'is', total)
print('The number of invalid input attempts was', tot_invalid_trys)