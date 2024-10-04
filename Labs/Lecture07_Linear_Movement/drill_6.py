from pico2d import *

WIDTH, HEIGHT = 1280, 1024
open_canvas(WIDTH, HEIGHT)

ground = load_image('TUK_GROUND.png')
hand = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

def move_hand():

    pass



def move_boy():

    pass

moving = True
x, y = WIDTH // 2, HEIGHT // 2
frame = 0

while moving:
    clear_canvas()
    ground.draw(WIDTH //2, HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    move_hand()
    move_boy()

close_canvas()
