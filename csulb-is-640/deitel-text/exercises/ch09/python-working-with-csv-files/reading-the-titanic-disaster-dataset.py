import pandas as pd
titanic = pd.read_csv('https://vincentarelbundock.github.io/' +
    'Rdatasets/csv/carData/TitanicSurvival.csv')
pd.set_option('precision', 2) # format for floating-point values
print(titanic.head())
print(titanic.tail())
titanic.columns = ['name', 'survived', 'sex', 'age', 'class']
print(titanic.head())
print('Descriptive Statistics for all data')
print(titanic.describe())
print('Descriptive Statistics for survivors')
print((titanic.survived == 'yes').describe())

import matplotlib.pyplot as plt
plt.hist(titanic.age)
plt.show()