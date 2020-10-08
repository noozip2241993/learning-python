'''
"Bob Nale is the owner of Nale’s Quick Fill. Bob would like 
to estimate the mean number of gallons of gasoline sold to 
his customers. Assume the number of gallons sold follows the 
normal distribution with a population standard deviation of 
2.30 gallons. From his records, he selects a random sample 
of 60 sales and finds the mean number of gallons sold is 8.60.

a. What is the point estimate of the population mean?
b. Develop a 99% confidence interval for the population mean.
c. Interpret the meaning of part (b).
'''
import my_stat_functions as my_stats

SIGMA = 2.30
SAMPLE_SIZE = 60
X_BAR = 8.60

print('a. What is the point estimate of the population mean?')
print(f'The sample mean of ${X_BAR} is the point estimate of the population mean. It indicates that given that a sample of {SAMPLE_SIZE} \
customers is representative of all customers, the average number of gallons sold is {X_BAR}.')

print('\nb. Develop a 99% confidence interval for the population mean.')
print('per .99 / 2 = .4950 = Area under normal curve for z of 2.575')
z = 2.575
conf_int = my_stats.confidence_interval(X_BAR, SIGMA, SAMPLE_SIZE, z, True)

print('\nc. Interpret the meaning of part (b).')
print(f'By sampling {SAMPLE_SIZE} customer sales, Bob can be 99% confident that the average number of gallons sold to across all customers is \
somewhere between {conf_int[0]:.1f} and {conf_int[1]:.1f} gallons.')
print(f'Stated differently, if Bob were to take 100 random samples each comprised of {SAMPLE_SIZE} sales, \
and calculate the confidence interval of each, the population mean would be within 99 of those intervals.')
