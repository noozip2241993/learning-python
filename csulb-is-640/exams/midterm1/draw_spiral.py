def draw_spiral():
    #1 define the following
    #1.1 number of circles
    #1.2 angle to increment by for each new circle
    #1.3 speed to draw at
    #1.4 the radius of each circle
    #2 open a turle draw screen
    #3 draw the circles
    #4 keep the window open when done

    #1 define the following
    #1.1 number of circles
    #1.2 angle to increment by for each new circle
    #1.3 speed to draw at
    #1.4 the radius of each circle
    CIRCLE_COUNT = 36
    CIRCLE_RADIUS = 100
    ANGLE = 360 / CIRCLE_COUNT
    SPEED = 1

    #2 open a turle draw screen
    import turtle
    pen = turtle.Pen()

    #3 draw the circles
    pen.speed(SPEED)
    pen.hideturtle()
    for item in range(CIRCLE_COUNT):
        pen.circle(CIRCLE_RADIUS)
        pen.left(ANGLE)
    
    #4 keep the window open when done
    turtle.done()

draw_spiral()