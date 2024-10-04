import turtle
import math
import random

def stop():
    turtle.bye()

def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(0)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(3)
    turtle.color(0, 0, 0)
    turtle.speed(0)

    turtle.onkey(stop, 'Escape')
    turtle.listen()

def draw_point(p):  # p tuple
    turtle.goto(p)
    random_color = (random.random(), random.random(), random.random())
    turtle.dot(3, random_color)

def draw_rounded_triangle():
    for t in range(0, 3601, 20):
        angle = math.radians(t / 10)


        r = 2 + 0.3 * math.cos(3 * angle)
        x = r * math.cos(angle)
        y = r * math.sin(angle)

        draw_point((x * 100, y * 100))

prepare_turtle_canvas()
draw_rounded_triangle()

turtle.done()
