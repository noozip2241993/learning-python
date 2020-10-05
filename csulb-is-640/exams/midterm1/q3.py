'''
The program https://github.com/ying-teaching/python/blob/master/3-decision-structure/hit_the_target.py 
is a hit the target source code that takes user inputs of an angle and a distance and determine if the 
project hit the target - a square whose low left corner is at (100, 250).

Please change the code to perform the following tasks:
-	Change the target from a square to a circle that is centered at (100, 250). Using the following constants
    o	TARGET_CENTER_X = 100  # Target's Center X
    o	TARGET_CENTER_Y = 250  # Target's Center Y
    o	TARGET_RADIUS = 30     # Circle radius
-	The code ask the user to input angle and distance to hit the circle target.
-	Change the code to let a user try inputting many times until the user hit the target. 
    i.e, keep asking the user to input an angle and a distance, exit in two conditions:
    o	when the user hit the target.
    o	when user input -1 as an angle or a distance.

'''
def hit_the_target():
    import turtle
    import math

    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    MAX_DISTANCE = 350

    TARGET_CENTER_X = 100  # Target's Center X
    TARGET_CENTER_Y = 250  # Target's Center Y
    TARGET_RADIUS = 30 / 2 # Circle radius

    PEN_SPEED = 0
    EXIT_VALUE = -1
    
    #1 open a 600 by 600 pixel window
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    pen = turtle.Pen()

    #2 draw a circle at 100, 250 with 30 radius
    pen.hideturtle()
    pen.speed(PEN_SPEED)
    pen.penup()
    pen.goto(TARGET_CENTER_X, TARGET_CENTER_Y)
    pen.pendown()
    pen.circle(TARGET_RADIUS)

    def user_try():
        try_again = True
        #3 return the pen to origin
        pen.hideturtle()
        pen.penup()
        pen.home()
        pen.showturtle()

        #4 prompt user for angle and distance
        #4.1 Exit immediately if either angle or distance is the EXIT_VALUE
        angle = int(input(f"Enter the projectile's angle (0-359) ({EXIT_VALUE} to EXIT): "))
        distance = int(input(f"Enter the launch distance (1-{MAX_DISTANCE}) ({EXIT_VALUE} to EXIT): "))
        if angle == EXIT_VALUE or distance == EXIT_VALUE:
            turtle.done()

        try:
            #5 move the pen per the angle and distance provided
            pen.speed(PEN_SPEED + 1)
            pen.pendown()
            def move_pen(angle, distance):
                pen.setheading(angle)
                pen.forward(distance)
            move_pen(angle, distance)

            #6 determine if it hit
            #6.1 hit is if the pen position is within the circle
            x_pos = pen.xcor()
            y_pos = pen.ycor()

            hit = False
            hit_value = math.sqrt((x_pos - TARGET_CENTER_X)**2 + (y_pos - TARGET_CENTER_Y)**2)
            if hit_value <= TARGET_RADIUS:
                hit = True
            
            #7 show a hit / miss message to the user
            if hit:
                print('Hit!')
                try_again = False
                turtle.done()
            else:
                print('Miss!')
                try_again = True
        
            if try_again:
                user_try()
            else:
                turtle.done()
        except:
            print('Hope you had fun. Goodbye!')
    user_try()

hit_the_target()