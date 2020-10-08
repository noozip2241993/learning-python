'''
The National Collegiate Athletic Association (NCAA) reported that college football assistant 
coaches spend a mean of 70 hours per week on coaching and recruiting during the season. A 
random sample of 50 assistant coaches showed the sample mean to be 68.6 hours, with a standard 
deviation of 8.2 hours.

a. Using the sample data, construct a 99% confidence interval for the population mean.
b. Does the 99% confidence interval include the value suggested by the NCAA? Interpret this result.
c. Suppose you decided to switch from a 99% to a 95% confidence interval. Without performing any 
calculations, will the interval increase, decrease, or stay the same? Explain your choice.
'''
import my_stat_functions as my_stats

SAMPLE_OF = 'college football assistant coaches'
METRIC = 'hours spend coaching and recruiting'
POPULATION_MEAN = 70
SAMPLE_SIZE = 50
SAMPLE_MEAN = 68.6
SAMPLE_STD_DEV = 8.2
CONF_LEVEL = .99
T1 = 2.680
T2 = 2.010

print('\na. Using the sample data, construct a 99% confidence interval for the population mean.')
conf_int = my_stats.confidence_interval_no_sigma(SAMPLE_MEAN, SAMPLE_STD_DEV, SAMPLE_SIZE, T1, True)

print('\nb. Does the 99% confidence interval include the value suggested by the NCAA? Interpret this result.')
print(f'The NCAA reports that {SAMPLE_OF} spend 70 hours per week on coaching and recruiting during the season. \
our observations indicate with 99% confidence that they spend from {conf_int[0]:.0f} to {conf_int[1]:.0f} hours. \
The NCAA\'s report does fall within that interval.')

print('\nc. Suppose you decided to switch from a 99% to a 95% confidence interval. Without performing any \
calculations, will the interval increase, decrease, or stay the same? Explain your choice.')
print(f'The interval will become narrower.')
conf_int2 = my_stats.confidence_interval_no_sigma(SAMPLE_MEAN, SAMPLE_STD_DEV, SAMPLE_SIZE, T2, True)