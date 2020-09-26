# You can query the current states of a pen using methods such 
# as `position`, `xcor`, `ycor`, `heading` and etc. The 
# following is a demo:

import turtle

TEXT_FONT = ('Arial', 18, 'normal')

pen = turtle.Pen()

pen.forward(100)
pen.left(90)
pen.forward(100)

position = pen.position()
pen.write(position, font=TEXT_FONT)

pen.goto(150,150)
x_coordinate = pen.xcor()
y_coordinate = pen.ycor()
coordinate = f'x: {x_coordinate}, y: {y_coordinate}'
pen.write(coordinate, font=TEXT_FONT)

pen.setheading(180)
pen.forward(200)
pen.write(pen.heading(), font=TEXT_FONT)

turtle.done()