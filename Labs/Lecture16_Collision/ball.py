from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self, x=400, y=300, velocity=1, is_fired=False):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.is_fired = is_fired  # 발사된 공인지 여부를 나타내는 속성
        self.is_removed = False  # 객체가 삭제되었는지 여부를 추적하는 속성

    def draw(self):
        if not self.is_removed:
            self.image.draw(self.x, self.y)
            left, bottom, right, top = self.get_bb()
            draw_rectangle(left, bottom, right, top)

    def update(self):
        if not self.is_removed:
            self.x += self.velocity * 100 * game_framework.frame_time
            if self.x < 25 or self.x > 1600 - 25:
                game_world.remove_object(self)
                self.is_removed = True  # 삭제되었음을 표시

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        if not self.is_removed:  # 삭제되지 않은 경우에만 실행
            if group == 'boy:ball' or group == 'boy:zombie':
                game_world.remove_object(self)  # 충돌 시 공을 제거
                self.is_removed = True  # 삭제되었음을 표시
