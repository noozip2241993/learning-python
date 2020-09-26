'''
Write a script that inputs a purchase price of a dollar or less for an item. 
Assume the purchaser pays with a dollar bill. Determine the amount of change 
the cashier should give back to the purchaser. Display the change using the 
fewest number of pennies, nickels, dimes and quarters. For example, if the 
purchaser is due 73 cents in change, the script would output: 

Your change is:

2 quarters

2 dimes

3 pennies
'''

#initialization
my_input = .27
COIN_VALS = [25, 10, 5, 1]
change = (1 - my_input) * 100
q = 0
d = 0
n = 0
p = 0

#processing
q = int(change // COIN_VALS[0])
change -= q * COIN_VALS[0]
d = int(change // COIN_VALS[1])
change -= d * COIN_VALS[1]
n = int(change // COIN_VALS[2])
change -= n * COIN_VALS[2]
p = int(change // COIN_VALS[3])
change -= p * COIN_VALS[3]

#termination
print('Your change is:')
print(f'{q} quarters\n{d} dimes\n{n} nickles\n{p} pennies')