from pico2d import *

from grass import Grass
from boy import Boy
from ball import Ball
import game_world


# Game object class here


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def reset_world():
    global running
    global boy

    running = True

    background_grass = Grass(y=70)
    game_world.add_object(background_grass, 0)  # depth=0으로 백그라운드에 추가

    boy = Boy() # 영숙 객체
    game_world.add_object(boy, 1)
    
    foreground_grass = Grass(y=50)
    game_world.add_object(foreground_grass, 1)  # depth=1로 포어그라운드에 추가



def update_world():
    game_world.update()



def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
