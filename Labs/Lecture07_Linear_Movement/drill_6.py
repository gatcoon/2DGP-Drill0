from pico2d import *
import random
import time
import math

WIDTH, HEIGHT = 1280, 1024
open_canvas(WIDTH, HEIGHT)

ground = load_image('TUK_GROUND.png')
hand = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

def move_hand():
    
    global hand_x, hand_y
    hand_x = random.randint(0, WIDTH)
    hand_y = random.randint(0, HEIGHT)


def move_boy():
    global x, y, direction

    distance = math.sqrt((hand_x - x) ** 2 + (hand_y - y) ** 2)

    if distance > 0:
        direction_x = (hand_x - x) / distance
        direction_y = (hand_y - y) / distance

        speed = 10
        x += direction_x * speed
        y += direction_y * speed

    if direction_x > 0:
            direction = 1
    elif direction_x < 0:
            direction = -1
    
    if distance < 5:
        move_hand()

moving = True
x, y = WIDTH // 2, HEIGHT // 2
frame = 0
hand_x, hand_y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
direction = 1

while moving:
    clear_canvas()
    ground.draw(WIDTH //2, HEIGHT // 2)
    if direction == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif direction == -1:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)

    hand.draw(hand_x, hand_y)
    update_canvas()
    frame = (frame + 1) % 8

    move_boy()

    delay(0.05)

close_canvas()

