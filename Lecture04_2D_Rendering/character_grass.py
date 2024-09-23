from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


while(1):
    x = 400
    y = 90
    r = 200
    a = -90

    #삼각형
    while (x < 800):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        #delay(0.01)
    
    while (x > 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        y = y + 2
        #delay(0.01)
        
    while (x > 0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        y = y - 2
        #delay(0.01)
    
    while (x < 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        #delay(0.01)
    
    #원
    while (a > -450):
        clear_canvas_now()
        grass.draw_now(400, 30)
        x = 400 + r * math.cos(a / 360 * 2 * math.pi)
        y = 300 + r * math.sin(a / 360 * 2 * math.pi)
        character.draw_now(x, y)
        a = a - 2
        delay(0.01)


close_canvas()
