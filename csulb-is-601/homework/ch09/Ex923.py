'''
A large on-demand, video streaming company is designing a large-scale survey 
to determine the mean amount of time corporate executives watch on-demand 
television. A small pilot survey of 10 executives indicated that the mean time 
per week is 12 hours, with a standard deviation of 3 hours. The estimate of the 
mean viewing time should be within 0.25 hour. The 95% level of confidence is to 
be used. How many executives should be surveyed?
'''
import my_stat_functions as my_stats

SAMPLE_OF = 'corporate executives'
METRIC = 'viewing time'
UNIT = 'hours per week'
SAMPLE_SIZE = 10
SAMPLE_MEAN = 12
SAMPLE_STD_DEV = 3
MAX_ERROR = .25
CONF_LEVEL = .95
Z = 1.96

sample_size = my_stats.sample_size_population_mean(Z, MAX_ERROR, SAMPLE_STD_DEV, True)