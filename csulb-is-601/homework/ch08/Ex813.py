'''
Consider all of the coins (pennies, nickels, quarters, etc.) in your pocket 
or purse as a population. Make a frequency table beginning with the current 
year and counting backward to record the ages (in years) of the coins. 
For example, if the current year is 2019, then a coin with 2017 stamped on 
it is 2 years old.

a. Draw a histogram or other graph showing the population distribution.
b. Randomly select five coins and record the mean age of the sampled coins. Repeat 
this sampling process 20 times. Now draw a histogram or other graph showing the 
distribution of the sample means.
c.Compare the shapes of the two histograms. Why are the two distributions different?
'''
import matplotlib.pyplot as plt
import pandas as pd
import random
import statistics as stat

COIN_YEARS_POP = [2006, 2015, 2013, 2006, 1999, 1991, 
                    2008, 2001, 2006, 1979, 1987, 2004, 
                    1992, 2014, 1989, 1982, 1982, 1978,
                    2002, 2006, 1981, 1974, 2007, 1973,
                    1992, 1981, 1978, 1990, 2006, 1996,
                    2015, 1979, 1989, 2006, 1990, 1980,
                    1989, 1990, 1963, 1964, 1982]
SAMPLE_SIZE = 5
SAMPLE_COUNT = 30
NUM_BINS = 7
X_MIN = 1960
X_MAX = 2020
Y_MIN = 0
Y_MAX = 15
AXES = [X_MIN, X_MAX, Y_MIN, Y_MAX]

print('a.')
# print a freq table for the population 
df1 = pd.DataFrame({'Coin Year' : COIN_YEARS_POP})
freq_table1 = pd.crosstab(index=df1['Coin Year'], columns='Frequency')
print(freq_table1)

print('b.')
# generate samples and record their means
samples = []
sample_means = []
for index in range(SAMPLE_COUNT):
    this_sample = random.sample(COIN_YEARS_POP, SAMPLE_SIZE)
    samples.append(this_sample)
    this_mean = int(stat.mean(this_sample))
    sample_means.append(this_mean)


# print a freq table for the sample means
df2 = pd.DataFrame({'Sample Means' : sample_means})
freq_table2 = pd.crosstab(index=df2['Sample Means'], columns='Frequency')
print(freq_table2)

#plot the pop and sample means
df1.plot.hist(bins=NUM_BINS, rwidth=.5)
plt.axis(AXES)
df2.plot.hist(bins=NUM_BINS, rwidth=.5)
plt.axis(AXES)
plt.show()

print('c.')
print('The two plots are different because the plot of the sample means tends toward a \
normal distribution regardless of the shape of the population distribution.')