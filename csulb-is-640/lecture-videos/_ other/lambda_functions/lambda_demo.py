#Lambda arguments:expression
x = lambda a: a*a
print(x(3))

def new(a):
    return a*a
print(new(3))

# lambda functions are best used within other higher-order functions
def new_func(x):
    return(lambda y: x + y)
t = new_func(3)
u = new_func(2)

print(t(3))
print(u(3))

# using lambda within filter()
my_list = [2, 3, 4, 5, 6, 7, 8]

# get a list of the my_list elements that produce a result of 2 when divided by 3
new_list = list(filter(lambda a: (a / 3 == 2), my_list))
print(new_list)

# using lambda within map()
# get a list of whether each my_list element does not produce a result of 2 when divided by 3
new_list = list(map(lambda a: (a / 3 != 2), my_list))
print(new_list)

# using lambda within reduce()
from functools import reduce
#reduce(function, sequence)
# add the elements of a list 23 + 21 + 45 + 98
print(reduce(lambda a, b: a + b, [23, 21, 45, 98]))

# solve algebra expressions with lambda
# linear expressions
s = lambda a: a * a
print(s(4))

#3x + 4y
d = lambda x, y: 3 * x + 4 * y
print(d(4, 7))

#quadratic equations
#(a + b)**2

x = lambda a, b: (a + b)**2
print(x(3, 4))
