#import os 
#dir_path = os.path.dirname(os.path.realpath(__file__))

with open ('accounts.txt', mode='w') as accounts:
    print('100 Jones 24.98', file=accounts)
    accounts.write('200 Doe 345.67\n')
    accounts.write('300 White 0.00\n')
    accounts.write('400 Stone -42.16\n')
    accounts.write('500 Rich 224.62\n')

