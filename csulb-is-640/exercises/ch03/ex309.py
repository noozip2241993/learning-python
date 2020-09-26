'''In Exercise 2.11, you wrote a script that separated a five-digit integer into its individual digits and displayed them. Reimplement your
script to use a loop that in each iteration “picks off” one digit (left to right) using the //
and % operators, then displays that digit.'''

user_input = input('Input a 5-digit integer: ')
number = int(user_input)
length = len(user_input)

print(user_input)
for i in range(length):
    print(f'{i} : {number // 10**(length - i - 1) % 10}')