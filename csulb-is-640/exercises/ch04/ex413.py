'''(Arbitrary Argument List) Calculate the product of a series of integers that are
passed to the function product, which receives an arbitrary argument list. Test 
your function with several calls, each with a different number of arguments.'''

def product(int1=0, int2=0, *ints):
    product = int1
    product *= int2
    for i in ints:
        product *= i
    
    print(f'The product of {int1}, {int2}, {ints} is {product}.')

product(1,2)
product(1,2,3)
product(1,2,3,4,5,6,7,8,9)

product()
product(50)