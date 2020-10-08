'''
The owner of Britten’s Egg Farm wants to estimate the mean number of eggs produced 
per chicken. A sample of 20 chickens shows they produced an average of 20 eggs per 
month with a standard deviation of 2 eggs per month.

a. What is the value of the population mean? What is the best estimate of this value?
b. Explain why we need to use the t-distribution. What assumption do you need to make?
c. For a 95% confidence interval, what is the value of t?
d. What is the margin of error?
e. Develop the 95% confidence interval for the population mean.
f. Would it be reasonable to conclude that the population mean is 21 eggs? What about 25 eggs?
'''
import my_stat_functions as my_stats
SAMPLE_OF = 'chickens'
METRIC = 'eggs per month'
SAMPLE_SIZE = 20
X_BAR = 20
S = 2
t_95 = 2.093 #per .95 and degrees of freedom = SAMPLE_SIZE - 1 = 19, the Area under normal curve for t is 2.093


print('a. What is the value of the population mean? What is the best estimate of this value?')
print(f'The sample mean of ${X_BAR} is the point estimate of the population mean. It indicates that \
\ngiven that a sample of {SAMPLE_SIZE} {SAMPLE_OF} is representative of all {SAMPLE_OF}, the average \
\nnumber of {METRIC} is {X_BAR}.')

print('\nb. Explain why we need to use the t-distribution. What assumption do you need to make?')
print(f'We need to use the t-distribution because we don\'t know what the population mean is. \
\nA consequence of this is that we have to assume that the confidence interval at a given confidence \
\nlevel will be wider than if we knew the population std deviation and count us the z-distribution.')

print('\nc. For a 95% confidence interval, what is the value of t?')
print(t_95)

print('\nd. What is the margin of error?')
margin_err = my_stats.margin_error_no_sigma(S, SAMPLE_SIZE, t_95, verbose=True)

print('\ne. Develop the 95% confidence interval for the population mean.')
conf_int = my_stats.confidence_interval_no_sigma(X_BAR, S, SAMPLE_SIZE, t_95, verbose=True)

print('\nf. Would it be reasonable to conclude that the population mean is 21 eggs? What about 25 eggs?')
print('Both values are outside the confidence interval and therefore not reasonable to expect with a 95% confidence level.')