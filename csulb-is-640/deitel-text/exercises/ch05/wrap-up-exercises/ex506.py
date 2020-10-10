print("5.6 (Functions Returning Tuples)\n\
Define a function rotate that receives three arguments and returns a tuple in which the \n\
first argument is at index 1, the second argument is at index 2 and the third argument is \n\
at index 0. Define variables a, b and c containing 'Doug', 22 and 1984. Then call the function \n\
three times. For each call, unpack its result into a, b and c, then display their values.")

a = 'Doug'
b = 22
c = 1984

def rotate(a, b, c):
    return (c, a ,b)

for i in range(0,3):
    a, b, c = rotate(a, b, c)
    print(a,b,c)