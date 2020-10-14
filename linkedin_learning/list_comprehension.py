'''
FROM:
LINKEDIN LEARNING
List comprehension
From the course: Python Essential Training
Bill Weinman
    Tech Advocate, Entrepreneur, Programming Expert 
'''

def main():
    seq = range(11) # the first list

    #list comprehensions
    seq2 = [x * 2 for x in seq] #everything in the first list times 2
    seq3 = [x for x in seq if x % 3 != 0] #everything in the first list that is not divisible by 3
    seq4 = [(x, x**2) for x in seq] #everything in the first list and it's square each pair in a tuple
    from math import pi
    seq5 = [round(pi, i) for i in seq] #pi rounded to every decimal place in the first list (calling a function in a list comprhension)
    seq6 = { x: x**2 for x in seq} #everything in the first list and it's square all in a dictionary
    seq7 = {x for x in 'superduper' if x not in 'pd'} #a set of all characters in 'superduper' that are not 'p' or 'd'. a set is just unique letters.

    #print each resulting list
    print_list(seq)
    print_list(seq2)
    print_list(seq3)
    print_list(seq4)
    print_list(seq5)
    print(seq6)
    print_list(seq7)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()