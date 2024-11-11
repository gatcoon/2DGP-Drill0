import game_framework
import game_world
import play_mode

from pico2d import clear_canvas, load_image, get_events, update_canvas
from sdl2 import SDL_QuitEvent, SDL_QUIT, SDLK_ESCAPE, SDL_KEYDOWN, SDLK_SPACE, SDLK_0, SDLK_1, SDLK_2

from pannel import Pannel


def init():
    global pannel
    pannel = Pannel()
    game_world.add_object(pannel, 3)

def finish():
    game_world.remove_object(pannel)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_0):
            play_mode.boy.set_item('NONE')  # NONE 선택
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
            play_mode.boy.set_item('SmallBall')  # SmallBall 선택
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
            play_mode.boy.set_item('BigBall')  # BigBall 선택

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def update(): pass

def paused(): pass
def resume(): pass