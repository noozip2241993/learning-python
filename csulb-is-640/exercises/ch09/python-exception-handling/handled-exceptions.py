''' Simple exception handling
Place in a try suite a significant logical section of a program in which several statements
can raise exceptions, rather than wrapping a separate try statement around every state-
ment that raises an exception. However, for proper exception-handling granularity, each
try statement should enclose a section of code small enough that, when an exception
occurs, the specific context is known and the except handlers can process the exception
properly. If many statements in a try suite raise the same exception types, multiple try
statements may be required to determine each exception’s context.
'''

while True:
    try:
        number1 = int(input('Enter numerator: '))
        number2 = int(input('Enter denominator: '))
        result = number1 / number2
    except ValueError: # tried to convert non-numeric value to int
        print('You must enter two integers\n')
    except ZeroDivisionError: # denominator was 0
        print('Attempted to divide by zero\n')
    else: # executes only if no exceptions occur
        print(f'{number1:.3f} / {number2:.3f} = {result:.3f}')
        break #terminate the loop
    finally:
        print('finally always executes')

