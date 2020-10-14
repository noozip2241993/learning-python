print("5.7 (Duplicate Elimination)\n\
Create a function that receives a list and returns a (possibly shorter) \n\
list containing only the unique values in sorted order. Test your function \n\
with a list of numbers and a list of strings.")

numbers = [1,1,1,2,3,4,5,6,6,7,8,76,45,32,32]
strings = ['Michelle', 'Eric', 'Eric', 'Michelle']

def unique_vals(source=[], verbose=False):
    result = []
    for val in (source):
        if val not in result:
            result.append(val)
    if verbose:
        print(result)
    return sorted(result)

unique_vals(numbers, True)
unique_vals(strings, True)