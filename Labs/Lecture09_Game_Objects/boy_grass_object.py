import random

from pdb import runctx

from pico2d import *

# Game object class here
class Grass:
    # 생성자 함수 : 객체의 초기 상태를 설정
    def __init__(self):
        # 모양없는 납작한 붕어빵의 초기모습결정
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400,30)

    pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        # 공의 크기와 이미지를 랜덤하게 설정 (작은 공 또는 큰 공)
        if random.choice([True, False]):
            self.image = load_image('ball21x21.png')
            self.size = 21
        else:
            self.image = load_image('ball41x41.png')
            self.size = 41

        self.x = random.randint(0, 800)
        self.y = 599
        self.speed = 5

    def update(self):
        # 공이 바닥에 닿으면 멈추도록 설정
        if self.y > 30 + self.size / 2:
            self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global team
    global balls
    global world

    running = True
    world = []

    grass = Grass() # 잔디를 찍어낸다. 생성한다
    world.append(grass)

    team = [Boy() for i in range(10)]
    world += team

    balls = [Ball() for i in range(20)]  # 20개의 공 생성
    world += balls

running = True


def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()

# initialization code
reset_world()

# game main loop code
running = True
while running:
    # game logic
    handle_events()
    update_world() # 상호작용을 시뮬레이션
    render_world() # 그 결과 보여준다.
    delay(0.05)


# finalization code

close_canvas()
