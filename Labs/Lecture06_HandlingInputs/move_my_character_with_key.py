from pico2d import *

open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('character_walk_sprites.png')


def handle_events():
    global running, dir_x, dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

running = True
x = 800 // 2
y = 90
frame = 0
dir_x = 0
dir_y = 0

while running:
    clear_canvas()
    grass.draw(400, 100)
    character.clip_draw(frame * 240 + 80, 10, 190, 200, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 10
    x += dir_x * 5
    y += dir_y * 5
    delay(0.05)


close_canvas()

