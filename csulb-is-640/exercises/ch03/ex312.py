'''A palindrome is a number, word or text phrase that reads the same backwards or forwards. 
For example, each of the following five-digit integers is a palindrome: 12321, 55555, 45554 
and 11611. Write a script that reads in a five-digit integer and determines whether it’s a 
palindrome. [Hint: Use the // and % operators to separate the number into its digits.]'''

#initialization
user_input = input('Input a 5-digit integer: ')
number = int(user_input)
length = len(user_input)
term_output = f'{user_input} is a palindrome.'
input_chars = []

#processing
print(user_input)

#split input into list of chars
for i in range(length):
    input_chars.append(number // 10**(length -1 - i) % 10)

#check characters for palindrome matching
print(input_chars)
for i in range(length // 2):
    pos_a = i # next leftmost char position
    pos_b = length - 1 - i # next rightmost char position
    print(f'{pos_a:02} = {input_chars[pos_a]} : {pos_b:02} = {input_chars[pos_b]}') #display this

    # loop through characters from outside toward the middle checking for matches each time.
    # if the positions cross it means we have passed the middle position(s)
    # and there is nothing else to evaluate. 
    if input_chars[pos_a] != input_chars[pos_b] and pos_a < pos_b :
        term_output = f'{user_input} is not a palindrome.'

#termination
print(term_output)