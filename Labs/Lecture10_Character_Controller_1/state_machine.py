# 이벤트 체그 함수를 정의
# 상태 이벤트 e = (종류, 실제값) 튜블로 정의
from sdl2 import SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def time_out(e):
    return e[0] == 'TIME_OUT'





class StateMachine:

    def __init__(self, obj):
        self.obj = obj # 어떤 객체를 위한 상태머신인지 알려줌. obj = boy.self
        # 상태 이벤트를 보관할 이벤트 리스트
        self.event_q = []

    def start(self, state):
        self.cur_state = state # 시작 상태를 받아서, 그걸로 현재 상태를 정의
        #self.cur_state.enter(self.obj, ('START', 0))
        pass

    def update(self):
        self.cur_state.do(self.obj) # Idle.do()
        # 혹시 이벤트가 있나???
        if self.event_q: # list는 멤버가 있으면 True
            e = self.event_q.pop(0)
            # 이시점에서 우리한테 주어진 정보는?
            # e
            # cur_state
            # 현재 상태와 현재 발생한 이벤트에 따라서
            # 다음 상태를 결정하는 방법은??
            # 상태 변환 테이블을 이용
            for check_event, next_state in self.transitions[self.cur_state].items():
                if check_event(e):
                    self.cur_state.exit(self.obj)
                    self.cur_state = next_state
                    self.cur_state.enter(self.obj)

    def draw(self):
        self.cur_state.draw(self.obj)

    def add_event(self, e):
        self.event_q.append(e)

    def set_transitions(self, transitions):
        self.transitions = transitions