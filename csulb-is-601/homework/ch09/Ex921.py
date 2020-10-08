'''
The estimate of the population proportion should be within plus or minus .05, 
with a 95% level of confidence. The best estimate of the population proportion 
is .15. How large a sample is required?
'''
import my_stat_functions as my_stats

MARGIN_ERROR = .05
CONF_LEVEL = .95
Z = 1.96
POP_PROPORTION = .15

sample_size = my_stats.sample_size_population_proportion(MARGIN_ERROR, Z, POP_PROPORTION, True)