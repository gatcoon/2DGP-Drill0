from pico2d import *
import game_world
import game_framework
import random


class Ball:
    image = None

    def __init__(self, x=None, y=None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)

    def draw(self):
        # 월드 좌표에서 화면 좌표로 변환
        import server
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom
        self.image.draw(sx, sy)
        draw_rectangle(sx - 10, sy - 10, sx + 10, sy + 10)  # 충돌 영역 디버깅

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        if group == "boy:ball":
            game_world.remove_object(self)  # 공 제거
            print("Ball eaten!")  # 디버깅 메시지
