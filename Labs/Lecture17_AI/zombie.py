from pico2d import *

import random
import math
import game_framework
import game_world
from behavior_tree import BehaviorTree, Action, Sequence, Condition, Selector
import play_mode


# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10.0

animation_names = ['Walk', 'Idle']


class Zombie:
    images = None

    def load_images(self):
        if Zombie.images == None:
            Zombie.images = {}
            for name in animation_names:
                Zombie.images[name] = [load_image(f"./zombie/{name} ({i}).png") for i in range(1, 11)]
            Zombie.font = load_font('ENCR10B.TTF', 40)
            Zombie.marker_image = load_image('hand_arrow.png')


    def __init__(self, x=None, y=None):
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)
        self.load_images()
        self.dir = 0.0      # radian 값으로 방향을 표시
        self.speed = 0.0
        self.frame = random.randint(0, 9)
        self.state = 'Idle'
        self.ball_count = 0

        self.build_behavior_tree()

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        # fill here
        self.bt.run()


    def draw(self):
        Zombie.marker_image.draw(self.x - 10, self.y - 10)
        if math.cos(self.dir) < 0:
            Zombie.images[self.state][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
        else:
            Zombie.images[self.state][int(self.frame)].draw(self.x, self.y, 100, 100)
        self.font.draw(self.x - 10, self.y + 60, f'{self.ball_count}', (0, 0, 255))
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

    def handle_collision(self, group, other):
        if group == 'zombie:ball':
            self.ball_count += 1

    def distance_less_than(self, x1, y1, x2, y2, r):
        distance2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
        return distance2 < (PIXEL_PER_METER * r) ** 2

    def is_boy_nearby(self, r):
        return BehaviorTree.SUCCESS if self.distance_less_than(play_mode.boy.x, play_mode.boy.y, self.x, self.y, r) else BehaviorTree.FAIL

    def move_slightly_to(self, tx, ty):
        self.dir = math.atan2(ty - self.y, tx - self.x)
        distance = RUN_SPEED_PPS * game_framework.frame_time
        self.x += distance * math.cos(self.dir)
        self.y += distance * math.sin(self.dir)

    def move_to(self, r=0.5):
        self.state = 'Walk'
        self.move_slightly_to(self.tx, self.ty)
        return BehaviorTree.SUCCESS if self.distance_less_than(self.tx, self.ty, self.x, self.y, r) else BehaviorTree.RUNNING

    def set_random_location(self):
        self.tx, self.ty = random.randint(100, 1180), random.randint(100, 924)
        return BehaviorTree.SUCCESS

    def move_to_boy(self, r=0.5):
        self.state = 'Walk'
        self.move_slightly_to(play_mode.boy.x, play_mode.boy.y)
        return BehaviorTree.SUCCESS if self.distance_less_than(play_mode.boy.x, play_mode.boy.y, self.x, self.y, r) else BehaviorTree.RUNNING

    def flee_from_boy(self, r=0.5):
        self.state = 'Walk'
        angle = math.atan2(self.y - play_mode.boy.y, self.x - play_mode.boy.x)
        distance = RUN_SPEED_PPS * game_framework.frame_time
        self.x += distance * math.cos(angle)
        self.y += distance * math.sin(angle)
        return BehaviorTree.SUCCESS if not self.is_boy_nearby(r) else BehaviorTree.RUNNING

    def has_fewer_balls(self):
        return BehaviorTree.SUCCESS if self.ball_count < play_mode.boy.ball_count else BehaviorTree.FAIL

    def has_more_balls(self):
        return BehaviorTree.SUCCESS if self.ball_count > play_mode.boy.ball_count else BehaviorTree.FAIL

    def build_behavior_tree(self):
        # 소년을 추적
        c1 = Condition('소년이 근처에 있는가?', self.is_boy_nearby, 7)
        c2 = Condition('공을 소년보다 많이 가지고 있는가?', self.has_more_balls)
        a1 = Action('소년에게 접근', self.move_to_boy)
        chase_boy = Sequence('소년을 추적', c1, c2, a1)

        # 소년에게서 도망
        c3 = Condition('소년이 근처에 있는가?', self.is_boy_nearby, 7)
        c4 = Condition('공을 소년보다 적게 가지고 있는가?', self.has_fewer_balls)
        a2 = Action('소년에게서 도망', self.flee_from_boy)
        flee_boy = Sequence('소년에게서 도망', c3, c4, a2)

        # 배회
        a3 = Action('랜덤 위치 설정', self.set_random_location)
        a4 = Action('랜덤 위치로 이동', self.move_to)
        wander = Sequence('배회', a3, a4)

        # 선택 동작: 추적, 도망, 배회
        root = Selector('추적, 도망 또는 배회', chase_boy, flee_boy, wander)
        self.bt = BehaviorTree(root)
