import turtle

# 키보드 입력
turtle.listen()

# 거북이 생성
turtle.shape("turtle")
turtle.penup()

# 초기 위치
start_position = (0, 0)
turtle.goto(start_position)
turtle.pendown()

# 스탬프 찍기 함수
def stamp():
    turtle.stamp()

def move_up():
    turtle.setheading(90)
    x, y = turtle.position()  # 현재 위치 가져오기
    turtle.goto(x, y + 50)
    stamp()

def move_down():
    turtle.setheading(270)
    x, y = turtle.position()
    turtle.goto(x, y - 50)
    stamp()

def move_left():
    turtle.setheading(180)
    x, y = turtle.position()
    turtle.goto(x - 50, y)
    stamp()

def move_right():
    turtle.setheading(0)
    x, y = turtle.position()
    turtle.goto(x + 50, y)
    stamp()

# 거북이 초기화 함수
def reset_position():
    turtle.clear()  # 모든 스탬프와 경로 지우기
    turtle.penup()
    turtle.goto(start_position)  # 시작 위치로 돌아가기
    turtle.pendown()  # 펜을 내려서 경로 다시 그리기 시작

# 키보드 입럭
turtle.onkey(move_up, "w")
turtle.onkey(move_down, "s")
turtle.onkey(move_left, "a")
turtle.onkey(move_right, "d")
turtle.onkey(reset_position, "Escape")  # ESC키로 초기화

