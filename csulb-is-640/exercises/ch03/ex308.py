'''In Exercise 2.10, you wrote a script that input three integers, then displayed the 
sum, average, product, smallest and largest of those values. Reimplement your script 
with a loop that inputs four integers.'''

#initialization
MAX_INPUT_COUNT = 4
input_count = 0
my_ints = []

#processing
while input_count < MAX_INPUT_COUNT:
    my_input = int(input(f'Enter integer number {input_count + 1} of {MAX_INPUT_COUNT}: '))
    my_ints.append(my_input)
    input_count += 1

my_sum = sum(my_ints)
my_ave = sum(my_ints) / len(my_ints)
my_prod = 1
for i in my_ints:
    my_prod *= i
my_min = min(my_ints)
my_max = max(my_ints)

#termination
print(my_ints)
print(f'Sum: {my_sum}')
print(f'Average: {my_ave}')
print(f'Product: {my_prod}')
print(f'Smallest: {my_min}')
print(f'Largest: {my_max}')