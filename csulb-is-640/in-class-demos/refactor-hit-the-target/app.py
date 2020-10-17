import turtle
from game_constants import SCREEN_WIDTH, SCREEN_HEIGHT
from hit_target_game import draw_target, get_angle_distance, launch_turtle, show_hit_message

def setup_window():
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    pen = turtle.Pen()
    return pen

# Hit the Target Game
def main():
    pen = setup_window()

    draw_target(pen)

    angle, distance = get_angle_distance()

    launch_turtle(pen, angle, distance)

    show_hit_message(pen)

    turtle.done()

if __name__ == "__main__":
    main()