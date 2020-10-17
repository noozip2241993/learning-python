
import turtle
from game_constants import *

def draw_target(pen):
    # Draw the target.
    pen.hideturtle()
    pen.speed(0)
    pen.penup()
    pen.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
    pen.pendown()
    pen.setheading(EAST)
    pen.forward(TARGET_WIDTH)
    pen.setheading(NORTH)
    pen.forward(TARGET_WIDTH)
    pen.setheading(WEST)
    pen.forward(TARGET_WIDTH)
    pen.setheading(SOUTH)
    pen.forward(TARGET_WIDTH)
    pen.penup()

    # Center the turtle.
    pen.home()
    pen.showturtle()
    pen.speed(PROJECTILE_SPEED)

def get_angle_distance():
    angle = int(input("Enter the projectile's angle 0-360: "))
    distance = int(input(f'Enter the launch distance (1-{MAX_DISTANCE}): '))
    return angle, distance

def launch_turtle(pen, angle, distance):
    # Set the heading.
    pen.setheading(angle)

    # Launch the projectile.
    pen.pendown()
    pen.forward(distance)

def show_hit_message(pen):
    xcor = pen.xcor()
    ycor = pen.ycor()

    # Did it hit the target?
    is_in_x = ((xcor >= TARGET_LLEFT_X) and 
        (xcor <= (TARGET_LLEFT_X + TARGET_WIDTH)))
    is_in_y = ((ycor >= TARGET_LLEFT_Y) and
        (ycor <= (TARGET_LLEFT_Y + TARGET_WIDTH)))
    is_hit = is_in_x and is_in_y

    # show message
    if is_hit:
        print('Target hit!')
    else:
        print('You missed the target.')
