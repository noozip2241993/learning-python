'''
World population has grown considerably over the centuries. Continued growth could 
eventually challenge the limits of breathable air, drinkable water, arable land and 
other limited resources. There’s evidence that growth has been slowing in recent 
years and that world population could peak some time this century, then start to 
decline.

For this exercise, research world population growth issues. This is a controversial 
topic, so be sure to investigate various viewpoints. Get estimates for the current 
world population and its growth rate. Write a script that calculates world population 
growth each year for the next 100 years, using the simplifying assumption that the 
current growth rate will stay constant. Print the results in a table. The first column 
should display the year from 1 to 100. The second column should display the anticipated 
world population at the end of that year. The third column should display the numerical 
increase in the world population that would occur that year. Using your results, 
determine the years in which the population would be double and eventually quadruple 
what it is today.
'''

cur_world_pop_est = 7.8
prior_world_pop_est = 6.0
cur_year = 2020
prior_year = 1999

annual_growth_rate = (cur_world_pop_est - prior_world_pop_est) / (cur_year - prior_year)

index = 0
MAX_YEAR = 100
pop = cur_world_pop_est
inc = 0
HEADER = 'Index | Year | Population | Increase'

print(HEADER)
for i in range(MAX_YEAR):
    index += 1
    cur_year += 1
    inc = pop * annual_growth_rate
    pop += inc
    print(f'{index:<5} | {cur_year:<4} | {pop:9,.3f}B | {inc:,.3f}B')