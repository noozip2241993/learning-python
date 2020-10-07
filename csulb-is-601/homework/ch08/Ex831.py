'''
Power + Inc. produces AA batteries used in remote-controlled toy cars. The mean life of 
these batteries follows the normal probability distribution with a mean of 35.0 hours 
and a standard deviation of 5.5 hours. As a part of its quality assurance program, 
Power +, Inc. tests samples of 25 batteries.

a. What can you say about the shape of the distribution of the sample mean?
b. What is the standard error of the distribution of the sample mean?
c. What proportion of the samples will have a mean useful life of more than 36 hours?
d. What proportion of the samples will have a mean useful life greater than 34.5 hours?
e. What proportion of the samples will have a mean useful life between 34.5 and 36.0 hours?
f. What is the probability that the sampling error would be less than or more than 1 hour?
'''
import my_stat_functions as my_stats

MU = 35.0 #hours
SIGMA = 5.5 #hours
SAMPLE_SIZE = 25 #batteries

print('a. What can you say about the shape of the distribution of the sample mean?')
print('Without calculating anything yet, I would say that the distribution of the sample \
    mean will have a shape resembling a normal distribution. The Central Limit Theorom allows \
    for this conclusion.')

print('\nb. What is the standard error of the distribution of the sample mean?')
print(f'The standard error of the distribution of the sample mean is {my_stats.std_error_of_mean(SIGMA, SAMPLE_SIZE):.4f}')

print('\nc. What proportion of the samples will have a mean useful life of more than 36 hours?')
z_c = my_stats.z_value_known_sigma(36, MU, SIGMA, SAMPLE_SIZE)
area_c = .3186
p_c = .5000 - area_c
print('Because the sample mean is higher than the population mean and we are looking \n\
for the proportion above the sample mean we subtract it\'s area from .5000 to find the \n\
proportion we are interested in.')
print(f'z = {z_c:.4f} \np = .5000 - {area_c} = { p_c }')

print('\nd. What proportion of the samples will have a mean useful life greater than 34.5 hours?')
z_d = my_stats.z_value_known_sigma(34.5, MU, SIGMA, SAMPLE_SIZE)
area_d = .1736
p_d = .5000 + area_d
print('Because the sample mean is lower than the population mean and we are looking \n\
for the proportion above the sample mean we add it\'s area to .5000 to find the \n\
proportion we are interested in.')
print(f'z = {z_d:.4f} \np = .5000 + {area_d} = { p_d }')

print('\ne. What proportion of the samples will have a mean useful life between 34.5 and 36.0 hours?')
print(f'Because both sample means are on opposite sides of the population mean, we add their areas to get the desired proportion. \
\np = {area_c} + {area_d} = {area_c + area_d:.4f}')

print('\nf. What is the probability that the sampling error would be less than or more than 1 hour?')
#define the sample means
low_sample_mean = MU - 1
high_sample_mean = MU + 1
print(f'low sample mean = {low_sample_mean}')
print(f'high sample mean = {high_sample_mean}')

#find the z-values
z_low = my_stats.z_value_known_sigma(low_sample_mean, MU, SIGMA, SAMPLE_SIZE)
z_high = my_stats.z_value_known_sigma(high_sample_mean, MU, SIGMA, SAMPLE_SIZE)
print(f'z-low = {z_low:.4f}')
print(f'z-high = {z_high:.4f}')

#lookup the areas under the curve given the z-values
area_low = .3186
area_high = .3186
print(f'area low = {area_low:.4f}')
print(f'area high = {area_high:.4f}')

#the areas under the curve represent the area between the population mean and the z-value for the sample mean
#we want the areas under the curve beyond those z-values. The total area unter the curve is 1, because it's symmetrical
#each side of the population mean has an area of .5000. To find the area beyond our z-values we subtract them from .5000.
#this gives us the areas for each side of the population mean. Adding them gives us the total area we are looking to find.
p_low = .5000 - area_low
p_high = .5000 - area_high
p_all = p_low + p_high
print(f'proportion low = {p_low:.4f}')
print(f'proportion high = {p_high:.4f}')

print(f'proportion all = {p_all:.4f}')
