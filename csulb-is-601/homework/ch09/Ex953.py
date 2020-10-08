'''
It is estimated that 60% of U.S. households subscribe to cable TV. You would like to verify 
this statement for your class in mass communications. If you want your estimate to be within 
5 percentage points, with a 95% level of confidence, how many households should you sample?
'''
import my_stat_functions as my_stats

MAX_ERROR = .05
CONF_LEVEL = .95
Z = 1.96
POP_PROPORTION = .60

sample_size = my_stats.sample_size_population_proportion(MAX_ERROR, Z, POP_PROPORTION, True)