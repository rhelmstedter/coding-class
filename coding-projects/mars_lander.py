import math
import random
import time
import turtle

# TODO Set up the game window
window = turtle.Screen()
window.tracer(0)
window.setup(0.6, 0.6)
window.title("The Python Mars Landing Game")
window.bgcolor("black")
width = window.window_width()
height = window.window_height()

# TODO Create stars
n_of_stars = 100
stars = turtle.Turtle()
stars.hideturtle()
stars.penup()
stars.color("white")
for _ in range(n_of_stars):
    x_pos = random.randint(-width // 2, width // 2)
    y_pos = random.randint(-height // 2, height // 2)
    stars.setposition(x_pos, y_pos)
    stars.dot(random.randint(2, 6))

# TODO Create Mars
mars = turtle.Turtle()
mars.penup()
mars.color("#A1241B")
mars.sety(-height * 2.8)
mars.dot(height * 5)

# TODO mars lander design parameters
branch_size = width / 16
n_of_discs = 5
disc_color = "light gray"
center_color = "white"
landing_gear_color = "white"

# TODO Set initial conditions
mars_lander = turtle.Turtle()
mars_lander.penup()
mars_lander.hideturtle()
mars_lander.setposition(-width / 3, height / 3)
mars_lander.rotation = random.randint(-9, 9)
mars_lander.clockwise_thruster = False
mars_lander.anticlockwise_thruster = False
mars_lander.travel_speed = random.randint(1, 3)
mars_lander.travel_direction = random.randint(-45, 0)

# TODO mars lander movement parameters
rotation_step = 0.2
speed_step = 0.1
gravity = 0.03

# TODO Landing parameters
landing_pad_position = 0, -height / 2.1
module_landing_position = (
    landing_pad_position[0],
    landing_pad_position[1] + branch_size,
)
landing_pos_tolerance_x = 20
landing_pos_tolerance_y = 5
landing_orientation = 270  # vertically downwards
landing_orientation_tolerance = 15

# TODO Create landing pad
landing_pad = turtle.Turtle()
landing_pad.hideturtle()
landing_pad.penup()
landing_pad.setposition(landing_pad_position)
landing_pad.pendown()
landing_pad.pensize(10)
landing_pad.forward(branch_size / 2)
landing_pad.forward(-branch_size)
landing_pad.forward(branch_size / 2)


def draw_mars_lander():
    mars_lander.clear()
    # "save" the starting position and orientation
    position = mars_lander.position()
    heading = mars_lander.heading()

    mars_lander.pendown()
    mars_lander.pensize(5)

    # Landing gear
    mars_lander.color(landing_gear_color)
    mars_lander.forward(branch_size)
    mars_lander.left(90)
    mars_lander.forward(branch_size / 2)
    mars_lander.forward(-branch_size)
    mars_lander.forward(branch_size / 2)
    mars_lander.right(90)
    mars_lander.forward(-branch_size)
    mars_lander.pensize(1)

    # Pods around the edge of the module
    mars_lander.color(disc_color)
    for _ in range(n_of_discs - 1):
        mars_lander.right(360 / n_of_discs)
        mars_lander.forward(branch_size)
        mars_lander.dot(branch_size / 2)
        mars_lander.forward(-branch_size)
    # Center part of the mars lander
    mars_lander.color(center_color)
    mars_lander.dot(branch_size)
    mars_lander.penup()

    # reset the turtle to initial position and orientation
    mars_lander.setposition(position)
    mars_lander.setheading(heading)


# Create burning fuel
burning_fuel = turtle.Turtle()
burning_fuel.penup()
burning_fuel.hideturtle()


def draw_burning_fuel(thruster):
    # Place turtle in the correct location
    # depending on which thruster is on
    if thruster == "clockwise":
        direction = 1
    elif thruster == "anticlockwise":
        direction = -1
    burning_fuel.penup()
    burning_fuel.setposition(mars_lander.position())
    burning_fuel.setheading(mars_lander.heading())
    burning_fuel.right(direction * 360 / n_of_discs)
    burning_fuel.forward(branch_size)
    burning_fuel.left(direction * 360 / n_of_discs)

    # Draw burning fuel
    burning_fuel.pendown()
    burning_fuel.pensize(8)
    burning_fuel.color("yellow")
    burning_fuel.forward(branch_size + 5)
    burning_fuel.backward(branch_size + 5)
    burning_fuel.left(5)
    burning_fuel.color("red")
    burning_fuel.pensize(5)
    for _ in range(2):
        burning_fuel.forward(branch_size + 5)
        burning_fuel.backward(branch_size + 5)
        burning_fuel.right(10)


def turn_on_clockwise_thruster():
    mars_lander.clockwise_thruster = True


def turn_on_anticlockwise_thruster():
    mars_lander.anticlockwise_thruster = True


def turn_off_clockwise_thruster():
    mars_lander.clockwise_thruster = False


def turn_off_anticlockwise_thruster():
    mars_lander.anticlockwise_thruster = False


window.onkeypress(turn_on_clockwise_thruster, "Right")
window.onkeypress(turn_on_anticlockwise_thruster, "Left")
window.onkeyrelease(turn_off_clockwise_thruster, "Right")
window.onkeyrelease(turn_off_anticlockwise_thruster, "Left")
window.listen()


def apply_force(mode):
    # Initial components of mars lander velocity
    tangential = mars_lander.travel_speed
    normal = 0

    if mode == "gravity":
        force_direction = -90
        step = gravity
    elif mode == "thrusters":
        force_direction = mars_lander.heading() + 180
        step = speed_step

    angle = math.radians(force_direction - mars_lander.travel_direction)

    # New components of mars lander velocity
    tangential += step * math.cos(angle)
    normal += step * math.sin(angle)

    direction_change = math.degrees(math.atan2(normal, tangential))
    mars_lander.travel_direction += direction_change

    mars_lander.travel_speed = math.sqrt(normal**2 + tangential**2)


def check_landing():
    if (
        abs(mars_lander.xcor() - module_landing_position[0]) < landing_pos_tolerance_x
        and abs(mars_lander.ycor() - module_landing_position[1])
        < landing_pos_tolerance_y
    ):
        if (
            abs(mars_lander.heading() - landing_orientation)
            < landing_orientation_tolerance
        ):
            mars_lander.setposition(module_landing_position)
            mars_lander.setheading(landing_orientation)
            draw_mars_lander()
            burning_fuel.clear()
            return True
        else:
            burning_fuel.clear()
            return False  # Crash on landing pad - wrong angle
    if mars_lander.ycor() < -height / 2:
        burning_fuel.clear()
        return False  # Crash below mars surface
    return None  # No successful or unsuccessful landing yet


while True:
    burning_fuel.clear()
    # Apply thrust if both thrusters are on
    if mars_lander.clockwise_thruster and mars_lander.anticlockwise_thruster:
        apply_force("thrusters")
    # Change rotational speed of mars lander
    if mars_lander.clockwise_thruster:
        draw_burning_fuel("clockwise")
        mars_lander.rotation -= rotation_step
    if mars_lander.anticlockwise_thruster:
        draw_burning_fuel("anticlockwise")
        mars_lander.rotation += rotation_step
    # Rotate mars lander
    mars_lander.left(mars_lander.rotation)

    # Apply effect of gravity
    apply_force("gravity")

    # Translate mars lander
    x = mars_lander.travel_speed * math.cos(math.radians(mars_lander.travel_direction))
    y = mars_lander.travel_speed * math.sin(math.radians(mars_lander.travel_direction))
    mars_lander.setx(mars_lander.xcor() + x)
    mars_lander.sety(mars_lander.ycor() + y)

    draw_mars_lander()

    successful_landing = check_landing()
    if successful_landing is not None:
        if successful_landing:
            print("Well Done! You've landed successfully")
        else:
            window.bgcolor("red")
            print("The mars lander crashed")
        break

    time.sleep(0.05)
    window.update()

turtle.done()
