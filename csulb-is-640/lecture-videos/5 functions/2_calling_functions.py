
def greet(first_name, last_name, prefix='Hello'):
    print(f'{prefix} {first_name} {last_name}')

greet(prefix='Hi', first_name='Elton', last_name='John') # keyword arguments explicitly assign the argument to the parameter by name
greet('Alicia', 'Keys') # positional arguments are implicitly assigned to the parameters by position
greet('Bob', 'Dylan', 'Hi') # illustrates parameters assigned default arguments in the function def can optionally be assigned another value 

# Syntax errors
# The default arguments must be at the end of the parameter list.
# If you use a keyword argument, it must be after positional arguments.