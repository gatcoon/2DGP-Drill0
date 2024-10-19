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

# 게임 루프
while running:
    clear_canvas()

    # 애니메이션 그리기 (프레임별로 캐릭터 이미지를 클립)
    character.clip_draw((frame + 1) * 35, 0, 40, 32, x, 200)

    update_canvas()

    # 프레임 업데이트
    frame = (frame + 1) % 3

    delay(0.05)

# 캔버스 닫기
close_canvas()
