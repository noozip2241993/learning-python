import turtle

pen = turtle.Pen()

pen.speed(1)
pen.dot(20, 'blue')
pen.circle(50)
pen.width(10)
pen.forward(50)
pen.color('brown')
pen.up()
pen.forward(30)
pen.down()
pen.write('hi', font=('Arial', 18, 'normal'))
pen.shape('blank')

turtle.done()