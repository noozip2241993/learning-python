# global variables should be avoided because any function can
# change them.

# the only valid case for a global variable is to define a 
# constant. That is a variable that you know you never
# intend to change. PI is an example of a constant.
PI = 3.1416

def main():
    radius = 42
    print_area(radius)

def print_area(radius):
    area = radius * radius * PI
    print(f'The area is {area: .2f}')

main()