import turtle
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
    turtle.speed(100)
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
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p): # p tuple,
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line(p1, p2):
    # fill here

    # 두 개 점만 그리기
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    a = (y2-y1)/(x2-x1) # 기울기 계산
    b = y1 - x1 * a # 절편값 계산

    for x in range(x1, x2, 10):
        y = a * x + b
        draw_point((x, y))

    draw_point(p2)

    pass

prepare_turtle_canvas()


# fill here
p1 = (-100, -100) # tuple 로 정의한 점 1
p2 = (300, 150) # tuple 로 정의한 점 2
draw_line(p1, p2)

draw_line((-100, -100), (-100, 500))

turtle.done()