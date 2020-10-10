'''
(What’s Does This Code Do?) 
'''
print('What does the following function do, based on the sequence it receives as an argument? \n\
def mystery(sequence): \n\
return sequence == sorted(sequence)')

def mystery(sequence):
    return sequence == sorted(sequence)

my_list = [1, 3, 6, 2, 4]
print(my_list)
print(mystery(my_list))

print('Given a sequence, this function creates a new sequence that contains the same values \n\
as the original sequence but sorted, then the function returns whether that new sequence IS \n\
the original sequence.')