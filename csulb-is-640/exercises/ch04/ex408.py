'''(Rounding Numbers) Investigate built-in function round at
https://docs.python.org/3/library/functions.html#round
then use it to round the float value 13.56449 to the nearest integer, tenths, hundredths
and thousandths positions.'''
NUMBER = 13.56449
nearest_int = round(NUMBER,0)
nearest_tenth = round(NUMBER,1)
nearest_hund = round(NUMBER,2)
print(f'{nearest_int}\n{nearest_tenth}\n{nearest_hund}')