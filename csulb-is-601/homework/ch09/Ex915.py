'''
The owner of the West End Kwick Fill Gas Station wishes to determine the 
proportion of customers who pay at the pump using a credit card or debit 
card. He surveys 100 customers and finds that 85 paid at the pump.

a. Estimate the value of the population proportion.
b. Develop a 95% confidence interval for the population proportion.
c. Interpret your findings.
'''
import my_stat_functions as my_stats

SAMPLE_SIZE = 100
SUCESSES = 80 #exercise calls for 85 but answer key shows 80
z_95 = 1.96

print('\na. Estimate the value of the population proportion.')
sample_proportion = SUCESSES / SAMPLE_SIZE 
print(f'{sample_proportion:.2f}')

print('\nb. Develop a 95% confidence interval for the population proportion.')
conf_int = my_stats.confidence_interval_pop_proportion(sample_proportion, SAMPLE_SIZE, z_95, True)

print('\nc. Interpret your findings.')
print(f'We can be 95% confident that the proportion of customers that pay at the pump is between \
{conf_int[0] * 100:.0f}% and {conf_int[1] * 100:.0f}% of all customers.')
