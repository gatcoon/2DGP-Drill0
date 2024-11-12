import random
from pico2d import *
import game_framework
import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy
    global balls

    # 배경과 소년을 추가합니다.
    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    # 공이 왼쪽에서만 생성되도록 설정합니다.
    balls = [Ball(random.randint(0, 400), 60, 0) for _ in range(30)]
    game_world.add_objects(balls, 1)

    # 충돌 대상들을 개별적으로 등록합니다.
    for ball in balls:
        game_world.add_collision_pair('boy:ball', boy, ball)

    # 좀비 생성 및 충돌 쌍 등록
    zombies = [Zombie() for _ in range(5)]
    game_world.add_objects(zombies, 1)
    for zombie in zombies:
        for ball in balls:
            game_world.add_collision_pair('zombie:ball', zombie, ball)

def finish():
    game_world.clear()

def update():
    game_world.update()
    game_world.handle_collision()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass
