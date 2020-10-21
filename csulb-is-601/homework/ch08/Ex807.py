'''
" population consists of the following five values: 12, 12, 14, 15, and 20.

a. List all samples of size 3, and compute the mean of each sample.
b. Compute the mean of the distribution of samplAe means and the population mean. Compare the two values.
c. Compare the dispersion in the population with that of the sample means."
'''
import itertools
import statistics as stat

POPULATION = [12, 12, 14, 15, 20]
SAMPLE_SIZE = 3

print('a.')
#List all samples of size 3
samples = list(itertools.combinations(POPULATION, SAMPLE_SIZE))
sample_means = []
for sample in samples:
    #compute the mean of each sample.
    mean = stat.mean(sample)
    sample_means.append(mean)
    
    print(f'Sample is {sample} : mean = {mean:.2f}')

print('\nb.')
#Compute the mean of the distribution of sample means and 
#the population mean. Compare the two values.
mean_of_sample_means = stat.mean(sample_means)
pop_mean = stat.mean(POPULATION)
print(f'{"mean of the distribution of sample means:":>45} {mean_of_sample_means:<.2f}')
print(f'{"population mean:":>45} {pop_mean:<.2f}')

print('\nc.')
#Compare the dispersion in the population with that 
#of the sample means.
pop_coeff_var = stat.stdev(POPULATION) / pop_mean
sample_coeff_var = stat.stdev(sample_means) / mean_of_sample_means
print(stat.stdev(sample_means))
print(mean_of_sample_means)
print(f'{"sample Coeff of Variation:":>45} {sample_coeff_var:<.2f}')
print(f'{"pop Coeff of Variation:":>45} {pop_coeff_var:<.2f}')