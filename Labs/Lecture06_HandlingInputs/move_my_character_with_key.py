from pico2d import *

open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('character_walk_sprites.png')


def handle_events():
    global running, dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1

running = True
x = 800 // 2
frame = 0
dir = 0

while running:
    clear_canvas()
    grass.draw(400, 100)
    character.clip_draw(frame*240 + 80, 10, 190, 200, x, 90)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 10
    x += dir * 5
    delay(0.05)


close_canvas()

