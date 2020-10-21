'''
5.16 (Sorting Letters and Removing Duplicates) Insert 20 random letters in the range
'a' through 'f' into a list. Perform the following tasks and display your results:
a) Sort the list in ascending order.
b) Sort the list in descending order.
c) Get the unique values sort them in ascending order.
'''
from random import randint

COUNT = 20
START = ord('a')
END = ord('f')

to_char = [chr(randint(START, END)) for x in range(COUNT)]
print(sorted(to_char))
print(sorted(to_char, reverse=True))
print(sorted(set(to_char)))