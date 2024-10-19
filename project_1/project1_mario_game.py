from pico2d import *
import os

# 작업 디렉토리 변경
os.chdir("C:\\Githup_2024_2\\Drill\\project_1\\sprites")

# 캔버스 열기
open_canvas()

# 이미지 불러오기
character = load_image('small_mario_state.png')  # 애니메이션 이미지

frame = 0  # 애니메이션 프레임 초기값
x = 200  # 캐릭터의 초기 x 좌표
running = True  # 게임 루프 제어
dir = 0  # 이동 방향 (1이면 오른쪽, -1이면 왼쪽)

# 게임 루프
while running:
    clear_canvas()

    # 애니메이션 그리기 (프레임별로 캐릭터 이미지를 클립)
    character.clip_draw((frame + 1) * 35, 0, 40, 32, x, 200)

    update_canvas()

    # 프레임 업데이트
    frame = (frame + 1) % 3

    # 이동 처리 (dir 값에 따라 좌우 이동)
    x += dir * 5

    # 이벤트 처리 (키보드 입력)
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False  # 창 닫기 이벤트
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir = 1  # 오른쪽으로 이동
            elif event.key == SDLK_LEFT:
                dir = -1  # 왼쪽으로 이동
            elif event.key == SDLK_ESCAPE:
                running = False  # ESC키를 누르면 종료
        elif event.type == SDL_KEYUP:
            if event.key in (SDLK_LEFT, SDLK_RIGHT):
                dir = 0  # 방향키를 떼면 멈춤
    delay(0.05)

# 캔버스 닫기
close_canvas()
