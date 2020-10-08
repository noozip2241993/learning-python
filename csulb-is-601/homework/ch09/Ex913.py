'''
Merrill Lynch Securities and Health Care Retirement Inc. are two large 
employers in downtown Toledo, Ohio. They are considering jointly offering 
child care for their employees. As a part of the feasibility study, they 
wish to estimate the mean weekly child-care cost of their employees. 
A sample of 10 employees who use child care reveals the following amounts 
spent last week.

107, 92, 97, 95, 105, 101, 91, 99, 95, 104

Develop a 90% confidence interval for the population mean. Interpret the result.
'''
import my_stat_functions as my_stats

SAMPLE_OF = 'employees'
METRIC = 'weekly child-care cost'
SAMPLE = (107, 92, 97, 95, 105, 101, 91, 99, 95, 104)
SAMPLE_SIZE = len(SAMPLE)
X_BAR = my_stats.sample_mean(SAMPLE)
S = my_stats.sample_std_dev(SAMPLE)
t_90 = 1.833

print('Develop a 90% confidence interval for the population mean. Interpret the result.')
conf_int = my_stats.confidence_interval_no_sigma(X_BAR, S, SAMPLE_SIZE, t_90, True)
print(f'With 90% confidence we can assume that the average {METRIC} of all \
{SAMPLE_OF} is somewhere between ${conf_int[0]:.2f} and ${conf_int[1]:.2f}')