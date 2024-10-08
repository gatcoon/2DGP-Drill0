from pdb import runctx

from pico2d import *

# Game object class here
class Grass:
    # 생성자 함수 : 객체의 초기 상태를 설정
    def __init__(self):
        # 모양없는 납작한 붕어빵의 초기모습결정
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400,30)

    pass



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass

    running = True
    grass = Grass() # 잔디를 찍어낸다. 생성한다


running = True


def update_world():
    grass.update() # 객체의 상태를 업데이트, 시뮬레이션
    pass

def render_world():
    clear_canvas()
    grass.draw()
    update_canvas()

open_canvas()

# initialization code
reset_world()

# game main loop code
running = True
while running:
    # game logic
    handle_events()
    update_world() # 상호작용을 시뮬레이션
    render_world() # 그 결과 보여준다.
    delay(0.05)


# finalization code

close_canvas()
