'''
Recent studies indicate that the typical 50-year-old woman spends 
$350 per year for personal-care products. The distribution of the 
amounts spent follows a normal distribution with a standard deviation 
of $45 per year. We select a random sample of 40 women. The mean amount 
spent for those sampled is $335. 

What is the likelihood of finding a sample mean this large or larger 
from the specified population?
'''
import my_stat_functions as my_stats

MU = 350
SIGMA = 45
SAMPLE_SIZE = 40
X_BAR = 335

z = my_stats.z_value_known_sigma(X_BAR, MU, SIGMA, SAMPLE_SIZE)
print(f'z = {z:.2f}')
area = .4826
print(f'Because the sample mean (X_BAR) is less than the population mean (MU), we add {area} to .5000 to get the area for z-values greater than {z:2f}.')
print(f'{area} + .5000 = {area + .5000:.4f}')