'''Reimplement Exercise 2.12 to use a loop that calculates and displays the amount of money you’ll have each year at the ends of years 1 through 30.'''

p = 1000 #principal
r = .07 #annual rate of return
n_list = [ 10, 20, 30] #years invested

for n in n_list:
    print(f'After {n} years, ${p*((1+r)**n):,.2f} will be on deposit.')