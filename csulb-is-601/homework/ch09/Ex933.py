'''
As part of their business promotional package, the Milwaukee Chamber of Commerce 
would like an estimate of the mean cost per month to lease a one-bedroom apartment. 
The mean cost per month for a random sample of 40 apartments currently available for 
lease is $1,147. The standard deviation of the sample is $50.

a. What is the point estimate of the population mean?
b. What is the point estimate of the population standard deviation?
c. What is the margin of error for a 98% confidence interval estimate?
d. Would it be reasonable to conclude that the population mean is $1,250 per month?
'''
import my_stat_functions as my_stats

SAMPLE_OF = 'apartments'
METRIC = 'cost per month'
SAMPLE_SIZE = 40
SAMPLE_MEAN = 1147
SAMPLE_STD_DEV = 50
CONF_LEVEL = .98
Z = 2.3275
T = 2.426

print('\na. What is the point estimate of the population mean?')
print(SAMPLE_MEAN)

print('\nb. What is the point estimate of the population standard deviation?')
print(SAMPLE_STD_DEV)

print('\nc. What is the margin of error for a 98% confidence interval estimate?')
margin_err = my_stats.margin_error_no_sigma(SAMPLE_STD_DEV, SAMPLE_SIZE, T, True)

print('\nd. Would it be reasonable to conclude that the population mean is $1,250 per month?')
conf_int = my_stats.confidence_interval_no_sigma(SAMPLE_MEAN, SAMPLE_STD_DEV, SAMPLE_SIZE, T, True)
print(f'1250.000 falls outside of our confidence interval at a 98% confidence level so, \
no it would not be reasonable to conclude that the population mean in $1,250.')