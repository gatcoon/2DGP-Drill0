import random
from pico2d import *
import game_framework
import game_world
from ball import Ball  # Ball 클래스를 import하여 모든 공과 상호작용 가능

# Zombie 이동 및 애니메이션 속도 설정
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel per 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10

animation_names = ['Walk']

class Zombie:
    images = None

    def load_images(self):
        if Zombie.images is None:
            Zombie.images = {}
            for name in animation_names:
                Zombie.images[name] = [load_image(f"./zombie/{name} ({i}).png") for i in range(1, 11)]

    def __init__(self):
        self.x, self.y = random.randint(1600 - 800, 1600), 150
        self.size = 200  # 초기 크기 설정
        self.life = 2    # 생명 수치 (2번 맞으면 삭제)
        self.load_images()
        self.frame = random.randint(0, 9)
        self.dir = random.choice([-1, 1])

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += RUN_SPEED_PPS * self.dir * game_framework.frame_time
        if self.x > 1600:
            self.dir = -1
        elif self.x < 800:
            self.dir = 1
        self.x = clamp(800, self.x, 1600)

    def draw(self):
        if self.dir < 0:
            Zombie.images['Walk'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, self.size, self.size)
        else:
            Zombie.images['Walk'][int(self.frame)].draw(self.x, self.y, self.size, self.size)

        # 충돌 박스 표시
        left, bottom, right, top = self.get_bb()
        draw_rectangle(left, bottom, right, top)

    def handle_collision(self, group, other):
        # 모든 공과의 충돌을 처리하고, 생명을 줄이며 두 번째 충돌 시 제거
        if group == 'zombie:ball' and isinstance(other, Ball):
            if self.life == 2:  # 첫 번째 충돌에서만 크기를 줄입니다.
                self.size /= 2  # 크기 절반으로 줄이기
                self.y -= 10    # 높이 조정
            self.life -= 1
            if self.life <= 0:  # 두 번째 충돌 시 좀비 삭제
                game_world.remove_object(self)
        elif group == 'boy:zombie':
            game_framework.quit()  # 소년과 충돌하면 게임 종료

    def get_bb(self):
        half_size = self.size / 2
        return self.x - half_size, self.y - half_size, self.x + half_size, self.y + half_size