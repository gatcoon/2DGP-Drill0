from pico2d import *
from state_machine import StateMachine, jump_down, land
from mario_states import Idle, Walk, Jump

class Mario:
    def __init__(self):
        self.x, self.y = 200, 100
        self.velocity = 0
        self.jump_speed = 0
        self.is_jumping = False
        self.ground_level = 100
        self.gravity = 0.5
        self.frame = 0
        self.facing_direction = 1  # 1: 오른쪽, -1: 왼쪽
        self.image = load_image('C:/Githup_2024_2/Drill/project_1/sprites/small_mario_state.png')

        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions({
            Idle: {jump_down: Jump},
            Walk: {jump_down: Jump},
            Jump: {land: Idle}
        })

    def update(self):
        self.state_machine.update()

    def draw(self):
        if self.facing_direction == 1:
            # 오른쪽 방향
            self.image.clip_draw(self.frame * 38, 0, 38, 32, self.x, self.y)
        else:
            # 왼쪽 방향, 좌우 반전
            self.image.clip_composite_draw(
                self.frame * 38, 0, 38, 32, 0, 'h', self.x, self.y, 38, 32
            )

    def handle_event(self, event):
        # 방향키 입력은 velocity와 facing_direction을 제어
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                self.velocity = 5
                self.facing_direction = 1  # 오른쪽
            elif event.key == SDLK_LEFT:
                self.velocity = -5
                self.facing_direction = -1  # 왼쪽
            elif event.key == SDLK_UP and not self.is_jumping:  # 점프 중 추가 점프 방지
                self.state_machine.add_event(('INPUT', event))

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT and self.velocity > 0:  # 오른쪽 키 떼면 이동 멈춤
                self.velocity = 0
            elif event.key == SDLK_LEFT and self.velocity < 0:  # 왼쪽 키 떼면 이동 멈춤
                self.velocity = 0

        # 다른 이벤트를 상태 머신에 전달
        self.state_machine.add_event(('INPUT', event))

    def get_bb(self):
        return self.x - 19, self.y - 16, self.x + 19, self.y + 16  # 크기에 맞는 충돌 박스 설정
