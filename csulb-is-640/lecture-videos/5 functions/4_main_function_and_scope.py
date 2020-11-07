def main():
    number = 42 # a local variable
    print_triple(number) # use of a local variable as an argument assigned to a function parameter

def print_triple(number):
    number *= 3 # to avoid subtle bugs, you shouldn't change the parameter value like this
    triple = number * 3 # you should instead use a new variable
    print(f'Triple of {number} is {triple}')

main()
