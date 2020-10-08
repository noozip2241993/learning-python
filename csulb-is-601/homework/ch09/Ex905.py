'''
A research firm surveyed 49 randomly selected Americans to determine 
the mean amount spent on coffee during 1 week. The sample mean was $20 
per week. The population distribution is normal with a standard 
deviation of $5.

a. What is the point estimate of the population mean? Explain what it indicates.
b. Using the 95% level of confidence, determine the confidence interval for μ. Explain what it indicates.
'''
import my_stat_functions as my_stats

SAMPLE_SIZE = 49
X_BAR = 20
SIGMA = 5

print('a. What is the point estimate of the population mean? Explain what it indicates.')
print(f'The sample mean of ${X_BAR} is the point estimate of the population mean. It indicates that given that a sample of {SAMPLE_SIZE} \
Americans is representative of all Americans, the average amount spent on coffee during 1 week is ${X_BAR}.')

print('\nb. Using the 95% level of confidence, determine the confidence interval for μ. Explain what it indicates.')
conf_int = my_stats.confidence_interval(X_BAR, SIGMA, SAMPLE_SIZE, 1.96, True)