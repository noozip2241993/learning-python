'''
Use a loop to find the two largest values of 10 numbers entered.
'''

#initialization
valid_input = False
while not valid_input:
    user_input = input("Enter any 10 numbers separated by a single space: ")
    my_nums_str = user_input.split(' ')
    my_nums = list(map(float,my_nums_str))
    if len(my_nums) == 10: valid_input = True
    else: print('Invalid input, try again.')
print(my_nums)
current_largest = my_nums[0]
prior_largest = my_nums[0]

#processing
for i in my_nums:
    if i >= current_largest:
        prior_largest = current_largest
        current_largest = i

#termination
print(f'largest = {current_largest}\nsecond largest = {prior_largest}')