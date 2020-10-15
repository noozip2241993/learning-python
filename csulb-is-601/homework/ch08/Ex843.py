'''
"Over the past decade, the mean number of hacking attacks experienced by members of the Information Systems 
Security Association is 510 per year with a standard deviation of 14.28 attacks. The number of attacks per 
year is normally distributed. Suppose nothing in this environment changes.

a. What is the likelihood this group will suffer an average of more than 600 attacks in the next 10 years?
b. Compute the probability the mean number of attacks over the next 10 years is between 500 and 600.
c. What is the possibility they will experience an average of less than 500 attacks over the next 10 years?"
'''
import my_stat_functions as my_stats

MU = 510 #attacks
SIGMA = 14.28 #attacks
SAMPLE_SIZE = 10 #years
X_BAR_A = 600 #attacks
X_BAR_B = 500 #attacks

print('a. What is the likelihood this group will suffer an average of more than 600 attacks in the next 10 years?')
z = my_stats.z_value_known_sigma(X_BAR_A, MU, SIGMA, SAMPLE_SIZE)
print(f'z = {z:.2f}')
area = .5000
print(f'Because the sample mean (X_BAR {X_BAR_A}) is more than the population mean (MU {MU}), we subtract {area:.4f} from .5000 to get the area for z-values greater than {z:2f}.')
print(f'.5000 - {area} = { .5000 - area:.4f}')

print('b. Compute the probability the mean number of attacks over the next 10 years is between 500 and 600.')
z = my_stats.z_value_known_sigma(X_BAR_B, MU, SIGMA, SAMPLE_SIZE)
print(f'z = {z:.2f}')
area = .4864
print(f'Because the sample mean (X_BAR {X_BAR_B}) is less than the population mean (MU {MU}), we add {area:.4f} to .5000 to get the area for z-values greater than {z:2f}.')
print(f'.5000 + {area} = { .5000 + area:.4f}')

print('c. What is the possibility they will experience an average of less than 500 attacks over the next 10 years?')
z = my_stats.z_value_known_sigma(X_BAR_B, MU, SIGMA, SAMPLE_SIZE)
print(f'z = {z:.2f}')
area = .4864
print(f'Because the sample mean (X_BAR {X_BAR_B}) is less than the population mean (MU {MU}), we subtract {area:.4f} from .5000 to get the area for z-values less than {z:2f}.')
print(f'.5000 - {area} = { .5000 - area:.4f}')