'''
"In the law firm Tybo and Associates, there are six partners. 
Listed is the number of cases each partner actually tried in 
court last month.

Partner    Number of Cases
Ruud        3
Wu          6
Sass        3
Flores      3
Wilhelms    0
Schueller   1

a. How many different samples of size 3 are possible?
b. List all possible samples of size 3, and compute the mean number of cases in each sample.
c. Compare the mean of the distribution of sample means to the population mean.
d. On a chart similar to Chart 8–2, compare the dispersion in the population with that of the sample means."
'''
import itertools
import statistics as stat
import matplotlib.pyplot as plt

PARTNER_CASES = (('Ruud', 3), ('Wu', 6), ('Sass', 3), ('Flores', 3), ('Wilhelms', 0), ('Schueller', 1))
SAMPLE_SIZE = 3
case_count_pop = []

for element in PARTNER_CASES:
    case_count_pop.append(element[1])

print('a.')
samples = list(itertools.combinations(case_count_pop, SAMPLE_SIZE))
print(f'There are {len(samples)} different samples of size {SAMPLE_SIZE} are possible')

print('\nb.')
sample_means = []
i = 1
for sample in samples:
    mean = stat.mean(sample)
    sample_means.append(mean)
    print(f'{i:>2}: Sample is {sample} : mean = {mean:.2f}')
    i += 1

print('\nc.')
#Compute the mean of the distribution of sample means and 
#the population mean. Compare the two values.
mean_of_sample_means = stat.mean(sample_means)
pop_mean = stat.mean(case_count_pop)
print(f'{"mean of the distribution of sample means:":>45} {mean_of_sample_means:<.2f}')
print(f'{"population mean:":>45} {pop_mean:<.2f}')

print('\nd.')
#Compare the dispersion in the population with that 
#of the sample means.
pop_coeff_var = stat.stdev(case_count_pop) / pop_mean
sample_coeff_var = stat.stdev(sample_means) / mean_of_sample_means

print(f'{"sample Coeff of Variation:":>45} {sample_coeff_var:<.2f}')
print(f'{"pop Coeff of Variation:":>45} {pop_coeff_var:<.2f}')

NUM_BINS = 6
pop_dispers = plt.figure(1)
plt.hist(x=case_count_pop, bins=NUM_BINS, rwidth=.5)
plt.axis([0, 6, 0, 5])

sample_mean_dispers = plt.figure(2)
plt.hist(x=sample_means, bins=NUM_BINS, rwidth=.5)
plt.axis([0, 6, 0, 5])

plt.show()