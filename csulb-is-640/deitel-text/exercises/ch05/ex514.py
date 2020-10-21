'''
5.14 (Is a Sequence Sorted?) Create a function is_ordered that receives a sequence and
returns True if the elements are in sorted order. Test your function with sorted and unsorted lists, tuples and strings.
'''

def is_ordered(sequence):
    # make the input a list
    in_seq = list(sequence)

    #check whether the input list equals it's sorted version
    if in_seq == sorted(in_seq):
        return True
    else:
        return False

def test_is_ordered():
    # initialize test variables
    unsorted_string = 'hello'
    unsorted_tuple = ( 3, 4, 2, 1, 5, 8, 7) 
    unsorted_list = [10, 9, 5, 6, 2, 4, 7, 11]
    sorted_string = ''.join(sorted(unsorted_string))
    sorted_tuple = tuple(sorted(unsorted_tuple))
    sorted_list = sorted(unsorted_list)

    # put test variables in a list
    test_vars = []
    test_vars.append(unsorted_string)
    test_vars.append(unsorted_tuple)
    test_vars.append(unsorted_list)
    test_vars.append(sorted_string)
    test_vars.append(sorted_tuple)
    test_vars.append(sorted_list)

    #test each variable and print the results
    for var in test_vars:
        print(f'{var} : {is_ordered(var)}')
    
test_is_ordered()
