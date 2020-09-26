import turtle

pen = turtle.Pen()

# slow motion at speed 1. Speed 10 is the fastest.
pen.speed(1)

pen.forward(50)
pen.right(90)
pen.forward(50)
pen.left(90)
pen.backward(100)
pen.sety(50)
pen.forward(150)

# for heading: 0 - east, 90 - north, 180 - west, 270 - south
pen.setheading(220)
pen.forward(100)
pen.goto(30,30)
pen.home()

turtle.done()