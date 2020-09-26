'''(Temperature Conversion) Implement a fahrenheit function that returns the
Fahrenheit equivalent of a Celsius temperature. Use the following formula:
    F = (9 / 5) * C + 32
Use this function to print a chart showing the Fahrenheit equivalents of all Celsius temperatures in the range 0–100 degrees. Use one digit of precision for the results. Print the
outputs in a neat tabular format.'''
MIN_TEMP = 0
MAX_TEMP = 100

def fahrenheit(celcius):
    return (9 / 5) * celcius + 32

for i in range(MIN_TEMP, MAX_TEMP + 1):
    if i == 0:
        print('  Cel : Fah')
        print('---------------')
    print(f'{i:>5.1f} : {fahrenheit(i):<5.1f}')