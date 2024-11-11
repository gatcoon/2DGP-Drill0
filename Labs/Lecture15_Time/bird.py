from pico2d import *
import game_framework
import random

# Bird Fly Speed
PIXEL_PER_METER = (10.0 / 0.3)
FLY_SPEED_KMPH = 15.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Bird:

    def __init__(self):
        self.image = load_image('bird_animation.png')
        self.x, self.y = random.randint(100, 1500), random.randint(300, 500)
        self.speed = FLY_SPEED_PPS
        self.dir = 1
        self.frame = 0
        self.width = 170  # 새의 가로 크기
        self.height = 130  # 새의 세로 크기

    def update(self):
        # 새의 방향에 따라 속도만큼 이동
        self.x += self.dir * self.speed * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

        # 화면의 왼쪽이나 오른쪽을 벗어날 경우 방향 반전
        if self.x < 0 or self.x > 1600:
            self.dir *= -1

    def draw(self):
        # 방향에 따라 좌우 반전하여 그리기
        if self.dir == 1:
            self.image.clip_draw(int(self.frame) * self.width + 10, 0, self.width, self.height, self.x, self.y)
        else:
            self.image.clip_composite_draw(int(self.frame) * self.width , 0, self.width, self.height, 0, 'h', self.x, self.y, self.width, self.height)