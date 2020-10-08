'''
Netflix is considering a new romcom (romantic comedy) series. Before making a final decision, 
the producers design an experiment to estimate the proportion of viewers who would watch the 
series. A random sample of 400 viewers was selected and asked to watch the first two episodes. 
After viewing the episodes, 250 viewers indicated they would watch the new series.

a. Estimate the value of the population proportion of people who would watch the new series.
b. Develop a 99% confidence interval for the population proportion of people who would watch the new series.
c. Interpret your findings.
'''
import my_stat_functions as my_stats

SAMPLE_OF = 'viewers'
METRIC = 'would watch the new series'
SAMPLE_SIZE = 400
SUCESSES = 250
CONF_LEVEL = .99
Z = 2.575

print('\na. Estimate the value of the population proportion.')
sample_proportion = SUCESSES / SAMPLE_SIZE 
print(f'{sample_proportion:.3f}')

print(f'\nb. Develop a {CONF_LEVEL * 100:.0f}% confidence interval for the population proportion.')
conf_int = my_stats.confidence_interval_pop_proportion(sample_proportion, SAMPLE_SIZE, Z, True)

print('\nc. Interpret your findings.')
print(f'We can be {CONF_LEVEL * 100:.0f}% confident that the proportion of {SAMPLE_OF} that {METRIC} is between \
{conf_int[0] * 100:.0f}% and {conf_int[1] * 100:.0f}% of all customers.')
