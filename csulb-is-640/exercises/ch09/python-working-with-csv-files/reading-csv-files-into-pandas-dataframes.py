import pandas as pd

# Read a csv using pandas dataframes
df = pd.read_csv('accounts.csv', names=['account', 'name', 'balance'])
print(df)

'''
The names keyword argument specifies the DataFrame ’s 
column names. If you do not supply this argument, 
read_csv assumes that the CSV file’s first row is 
a comma-delimited list of column names
'''

# Save a pandas dataframe to as a csv file
df.to_csv('accounts_from_dataframe.csv', index=False)

'''
The index=False keyword argument indicates that the row 
names ( 0 – 4 at the left of the DataFrame’s output) 
are not written to the file. The resulting file contains
the column names as the first row.
'''


