# 6 Getting Input
# The `turtle` module provide two input functions:
# - `turtle.textinput(title, prompt)`: pop up an input box for a string.
# - `turtle.numinput(title, prompt, default=None, minval=None, maxval=None)`:
#           pop up an input box for a number. You can provide optinoal default 
#           value, minimum and maximum value. It asks you to input again if the 
#           number is out of range.

import turtle

DEFAULT_NUMBER = 1000
MIN_NUMBER = 10
MAX_NUMBER = 10_000

turtle.bgcolor('blue')

pen = turtle.Pen()

num = turtle.numinput('Poker', 'Your stakes', DEFAULT_NUMBER, minval=MIN_NUMBER, maxval=MAX_NUMBER)

pen.color('orange')
pen.write(num, font=('Arial', 28, 'normal'))

turtle.done()

# In the above code, please distinguish two different types of calls: 
#   `turtle.bgcolor()`, `turtle.pen()`, `turtle.numinput()`, and `turtle.done()` 
#   are functions in the `turtle` module. `pen.color()` and `pen.write()` 
#   are methods of an instance/object of a `Turtle` class. The instance is bound 
#   to variable `pen`.
#
# It is a best practice to define constant values using meaningful variables names 
# that use uppercase words seperated by underscore.