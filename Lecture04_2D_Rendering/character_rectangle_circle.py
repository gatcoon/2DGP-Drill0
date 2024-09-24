from pico2d import *

def run_rectangle():
    print('RECTANGLE')
    pass

def run_circle():
    print('CIRCLE')
    pass


open_canvas()

#fill here
grass = load_image('grass.png')
boy = load_image('character.png')

while True:
    run_circle()
    run_rectangle()


close_canvas()
