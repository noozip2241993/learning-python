'''
Nike’s annual report says that the average American buys 6.5 pairs of sports shoes per year. 
Suppose a sample of 81 customers is surveyed and the population standard deviation of sports 
shoes purchased per year is 2.1.

a. What is the standard error of the mean in this experiment?
b. What is the probability that the sample mean is between six and seven pairs of sports shoes?
c. What is the probability that the difference between the sample mean and the population mean is less than 0.25 pair?
d. What is the likelihood the sample mean is greater than seven pairs?
'''
import my_stat_functions as my_stats
MU = 6.5 #pair shoes
SIGMA = 2.1 #pair shoes
SAMPLE_SIZE = 81 #customers
X_BAR_A = 6
X_BAR_B = 7

print('a. What is the standard error of the mean in this experiment?')
std_error = my_stats.std_error_of_mean(SIGMA, SAMPLE_SIZE)
print(f'{std_error:.4f}')

print('\nb. What is the probability that the sample mean is between six and seven pairs of sports shoes?')
z_a = my_stats.z_value_known_sigma(X_BAR_A, MU, SIGMA, SAMPLE_SIZE)
print(f'z_a = {z_a:.2f}')
area_a = .4838

z_b = my_stats.z_value_known_sigma(X_BAR_B, MU, SIGMA, SAMPLE_SIZE)
print(f'z_b = {z_b:.2f}')
area_b = .4838

print(f'Because the sample means (X_BAR_A = {X_BAR_A} and X_BAR_B = {X_BAR_B}) are on opposite sides of the \
population mean (MU {MU}), we add them to get the area for z-values between them.')
print(f'{area_a} + {area_b} = { area_a + area_b:.4f}')

print('\nc. What is the probability that the difference between the sample mean and the population mean is less than 0.25 pair?')
difference = .25
#define the sample means
low_sample_mean = MU - difference
high_sample_mean = MU + difference
print(f'low sample mean = {low_sample_mean}')
print(f'high sample mean = {high_sample_mean}')

#find the z-values
z_low = my_stats.z_value_known_sigma(low_sample_mean, MU, SIGMA, SAMPLE_SIZE)
z_high = my_stats.z_value_known_sigma(high_sample_mean, MU, SIGMA, SAMPLE_SIZE)
print(f'z-low = {z_low:.4f}')
print(f'z-high = {z_high:.4f}')

#lookup the areas under the curve given the z-values
area_low = .3577
area_high = .3577
print(f'area low = {area_low:.4f}')
print(f'area high = {area_high:.4f}')

#the areas under the curve represent the area between the population mean and the z-value for the sample means.
#Adding them gives us the total area we are looking to find.
p_low = area_low
p_high = area_high
p_all = p_low + p_high
print(f'proportion low = {p_low:.4f}')
print(f'proportion high = {p_high:.4f}')
print(f'proportion all = {p_all:.4f}')

print('\nd. What is the likelihood the sample mean is greater than seven pairs?')
print(f'Because the sample mean (X_BAR_B {X_BAR_B}) is more than the population mean (MU {MU}), \
we subtract {area_b:.4f} from .5000 to get the area for z-values greater than {z_b:2f}.')
print(f'.5000 - {area_b:.4f} = { .5000 - area_b:.4f}')