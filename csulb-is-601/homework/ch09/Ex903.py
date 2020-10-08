'''
A sample of 250 observations is selected from a normal population with a population standard deviation of 25. The sample mean is 20.

a. Determine the standard error of the mean.
b. Explain why we can use formula (9–1) to determine the 95% confidence interval.
c. Determine the 95% confidence interval for the population mean.
'''
import my_stat_functions as my_stats

SAMPLE_SIZE = 250
SIGMA = 25
X_BAR = 20
Z_VALUE = 1.96 #per .95 / 2 = .4750 = Area under normal curve for z of 1.96

print('a. Determine the standard error of the mean.')
std_error = my_stats.std_error_of_mean(SIGMA, SAMPLE_SIZE, True)

print('\nb. Explain why we can use formula (9–1) to determine the 95% confidence interval.')
print('We have been given the information that the population is normally distributed and we know the population standard deviation. \
    The Central Limit Thereom allows us to assume that the distribution of sample means is also normally distributed. ')
print('\nc. Determine the 95% confidence interval for the population mean.')
conf_int = my_stats.confidence_interval(X_BAR, SIGMA, SAMPLE_SIZE, Z_VALUE, True)