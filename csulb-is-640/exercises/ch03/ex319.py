'''
A right triangle can have sides that are all integers. The set of three integer values for 
the sides of a right triangle is called a Pythagorean triple. These three sides must satisfy 
the relationship that the sum of the squares of two of the sides is equal to the square of 
the hypotenuse. Find all Pythagorean triples for side1, side2 and hypotenuse (such as 3, 4 
and 5) all no larger than 20. Use a triple-nested for-loop that tries all possibilities. This 
is an example of “brute-force” computing. You’ll learn in more advanced computer science courses 
that there are many interesting problems for which there is no known algorithmic approach 
other than sheer brute force.
'''

side1 = 0
side2 = 0
side3 = 0
MAX = 20

for a in range(1, MAX + 1):
    for b in range(1, MAX + 1):
        for c in range(1, MAX + 1):
            l_side = a**2 + b**2
            r_side = c**2
            if l_side == r_side:
                print(f'[{a},{b},{c}] : {a}**2 + {b}**2 = {c}**2 : {a**2 + b**2} = {c**2}')