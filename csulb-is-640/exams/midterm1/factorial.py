'''
Calculate the factorial of any non-negative integer
# 1 ask the user for a non-negative integer
# 2 validate input 
# 2.1 is non-negative
# 2.2 can be cast as an integer
# 2.3 reprompt the user if either is false not
# 3 Loop through the range of integers starting with 0 and ending with the input (inclusively)
# 3.1 track the incremental factorial value in a variable
# 3.2 multiply the incremental factorial by the current integer in the range
# 3.3 assign that product to the incremental factorial variable
# 4 display the resulting factorial value
'''

def factorial():
    valid_input = False
    number = ''
    while not valid_input:
        # 1 ask the user for a non-negative integer
        raw_input = input('Enter any non-negative integer: ')

        # 2 validate input
        err_message = f'{raw_input} is not a non-negative integer. Please try again.' 
        # 2.2 can be cast as an integer
        try:
            number = int(raw_input)
            # 2.1 is non-negative
            if number >= 0:
                valid_input = True
            else:
                valid_input = False
        except:
            valid_input = False
        # 2.3 reprompt the user if either is false not
        if not valid_input:
            print(err_message)

    # 3 Loop through the range of integers starting with 0 and ending with the input (inclusively)
    # 3.1 track the incremental factorial value in a variable
    factorial = 1 # starting with a value of 1 represents 0!
    for item in range(1, number + 1):
        # 3.2 multiply the incremental factorial by the current integer in the range
        # 3.3 assign that product to the incremental factorial variable
        factorial *= item

    # 4 display the resulting factorial value
    print(f'{number}! is {factorial}.')

factorial()