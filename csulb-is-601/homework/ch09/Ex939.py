'''
A student conducted a study and reported that the 95% confidence interval 
for the mean ranged from 46 to 54. He was sure that the mean of the sample 
was 50, that the standard deviation of the sample was 16, and that the 
sample size was at least 30, but could not remember the exact number. 
Can you help him out?
'''
import my_stat_functions as my_stats

CONF_LEVEL = .95
REPORTED_CONF_INT = (46, 54)
SAMPLE_MEAN = 50
SAMPLE_STD_DEV = 16
MAX_ERROR = 50 - REPORTED_CONF_INT[0]
Z = 1.96

sample_size = my_stats.sample_size_population_mean(Z, MAX_ERROR, SAMPLE_STD_DEV, True)