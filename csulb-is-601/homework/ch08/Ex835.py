'''
"In the United States, the mean age of men when they marry for the 
first time follows the normal distribution with a mean of 29 years. 
The standard deviation of the distribution is 2.5 years. For a random 
sample of 60 men, what is the likelihood that the age when they were 
first married is less than 29.3. years?"
'''
import my_stat_functions as my_stats

MU = 29
SIGMA = 2.5
SAMPLE_SIZE = 60
X_BAR = 29.3

z = my_stats.z_value_known_sigma(X_BAR, MU, SIGMA, SAMPLE_SIZE)
print(f'z = {z:.2f}')
area = .3238
print(f'Because the sample mean (X_BAR) is more than the population mean (MU), we add {area} to .5000 to get the area for z-values less than {z:2f}.')
print(f'{area} + .5000 = {area + .5000:.4f}')