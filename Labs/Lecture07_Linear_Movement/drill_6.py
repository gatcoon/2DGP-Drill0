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
    
    global hand_x, hand_y, last_move_time
    current_time = time.time()
    if current_time - last_move_time >= 5:
        hand_x = random.randint(0, WIDTH)
        hand_y = random.randint(0, HEIGHT)
        last_move_time = current_time


def move_boy():
    global x, y

    distance = math.sqrt((hand_x - x) ** 2 + (hand_y - y) ** 2)

    if distance > 0:
        direction_x = (hand_x - x) / distance
        direction_y = (hand_y - y) / distance

        speed = 10
        x += direction_x * speed
        y += direction_y * speed

moving = True
x, y = WIDTH // 2, HEIGHT // 2
frame = 0
hand_x, hand_y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
last_move_time = time.time()

while moving:
    clear_canvas()
    ground.draw(WIDTH //2, HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    hand.draw(hand_x, hand_y)
    update_canvas()
    frame = (frame + 1) % 8

    move_hand()
    move_boy()

    delay(0.05)

close_canvas()
