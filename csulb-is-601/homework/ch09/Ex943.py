'''
In 2003, the Accreditation Council for Graduate Medical Education (ACGME) implemented 
new rules limiting work hours for all residents. A key component of these rules is 
that residents should work no more than 80 hours per week. The following is the number 
of weekly hours worked in 2017 by a sample of residents at the Tidelands Medical Center.

84, 86, 84, 86, 79, 82, 87, 81, 84, 78, 74, 86

a. What is the point estimate of the population mean for the number of weekly hours worked at the Tidelands Medical Center?
b. What is the point estimate of the population standard deviation?
c. What is the margin of error for a 90% confidence interval estimate?
d. Develop a 90% confidence interval for the population mean.
e. Is the Tidelands Medical Center within the ACGME guideline? Why?
'''
import my_stat_functions as my_stats

SAMPLE = (84, 86, 84, 86, 79, 82, 87, 81, 84, 78, 74, 86)
sample_mean = my_stats.sample_mean(SAMPLE)
sample_std_dev = my_stats.sample_std_dev(SAMPLE)
sample_size = len(SAMPLE)
CONF_LEVEL = .90
t_value = 1.796

print('\na. What is the point estimate of the population mean for the number of weekly hours worked at the Tidelands Medical Center?')
print(f'{sample_mean:.2f}')

print('\nb. What is the point estimate of the population standard deviation?')
print(f'{sample_std_dev:.2f}')

print('\nc. What is the margin of error for a 90% confidence interval estimate?')
margin_err = my_stats.margin_error_no_sigma(sample_std_dev, sample_size, t_value, True)

print('\nd. Develop a 90% confidence interval for the population mean.')
conf_int = my_stats.confidence_interval_no_sigma(sample_mean, sample_std_dev, sample_size, t_value, True)

print('\ne. Is the Tidelands Medical Center within the ACGME guideline? Why?')
print(f'The ACGME guideline is no more than 80 hours per week. That falls below our interval for \
the population mean and is therefore we are 90% confident that it is not realistic')