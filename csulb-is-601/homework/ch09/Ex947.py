'''
HighTech Inc. randomly tests its employees about company policies. 
Last year in the 400 random tests conducted, 14 employees failed the test.

a. What is the point estimate of the population proportion?
b. What is the margin of error for a 99% confidence interval estimate?
c. Compute the 99% confidence interval for the population proportion.
d. Is it reasonable to conclude that 5% of the employees cannot pass the company policy test? Why?
'''
import my_stat_functions as my_stats
OBSERVATIONS = 400
SUCESSES = 14 #In this case the wording is confusing employees failing the test is a sucessful result in our experiment 
sample_proportion = SUCESSES / OBSERVATIONS
CONF_LEVEL = .99
T = 2.576

print('\na. What is the point estimate of the population proportion?')
print(sample_proportion)

print('\nb. What is the margin of error for a 99% confidence interval estimate?')
margin_error = my_stats.margin_error_pop_proportion(sample_proportion, OBSERVATIONS, T, True)

print('\nc. Compute the 99% confidence interval for the population proportion.')
conf_int = my_stats.confidence_interval_pop_proportion(sample_proportion, OBSERVATIONS, T, True)

print('\nd. Is it reasonable to conclude that 5% of the employees cannot pass the company policy test? Why?')
print(f'Because .0500 falls within the confidence interval from {conf_int[0]:.4f} to {conf_int[1]:.4f} we can conclude with 99% \
\nconfidence that it is reasonable to conclude that 5% of the employees cannot pass the company policy test.')