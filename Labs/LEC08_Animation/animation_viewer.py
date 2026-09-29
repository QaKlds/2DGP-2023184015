# pico2d 라이브러리 전체를 불러온다
from pico2d import *

# 800 x 600 크기의 캔버스(화면)를 연다
open_canvas()

# 스프라이트시트 이미지(megaman.png)를 불러온다
character = load_image('megaman.png')

# 등장 애니메이션: 13프레임
# 각 프레임은 (left, top, width, height) = (왼쪽 x, 위쪽 y, 가로길이, 세로길이)
# 좌표는 이미지 기준이며 왼쪽 위가 (0, 0)이다
appear_frame = [
    (12, 0, 20, 70),
    (33, 0, 29, 70),
    (63, 0, 46, 70),
    (110, 0, 38, 70),
    (148, 0, 36, 70),
    (184, 0, 39, 70),
    (224, 0, 43, 70),
    (268, 0, 42, 70),
    (310, 0, 43, 70),
    (353, 0, 42, 70),
    (395, 0, 42, 70),
    (437, 0, 42, 70),
    (479, 0, 42, 70)
]

# 승리 포즈 애니메이션: 11프레임
victory_frame = [
    (34, 91, 40, 41),
    (81, 94, 38, 38),
    (122, 96, 38, 36),
    (165, 92, 32, 40),
    (201, 82, 36, 51),
    (240, 72, 31, 62),
    (277, 90, 42, 41),
    (320, 90, 46, 41),
    (369, 90, 41, 41),
    (413, 90, 41, 41),
    (457, 90, 41, 41)
]

# 달리기 애니메이션: 9프레임
run_frame = [
    (75, 200, 44, 45),
    (119, 200, 36, 45),
    (155, 200, 31, 45),
    (186, 200, 35, 45),
    (221, 200, 47, 45),
    (268, 200, 32, 45),
    (300, 200, 41, 45),
    (341, 200, 53, 45),
    (394, 200, 44, 45)
]

# 슬라이딩 애니메이션: 5프레임
# y좌표는 (299~339)로 모든 프레임 동일, x좌표는 (18~78), (78~132), (132~182), (182~221), (221~258)
sliding_frame = [
    (18, 299, 60, 40),
    (78, 299, 54, 40),
    (132, 299, 50, 40),
    (182, 299, 39, 40),
    (221, 299, 37, 40)
]

# 화면에 그릴 확대 배율 (원본 6배 크기로 확대해서 그린다)
scale = 6
# 캐릭터가 그려질 가로 중심 위치
center_x = 400
# 캐릭터의 발이 맞닿는 기준 높이
# scale을 6으로 키우면 가장 높은 프레임(등장, 높이 70)이 420px가 되므로
# baseline + 420 이 캔버스 높이 600 을 넘지 않도록 180 으로 내렸다
baseline = 180
# 애니메이션을 반복할 횟수
repeat_count = 5
# 한 프레임을 화면에 보여주는 시간(초)
frame_time = 0.1
# 애니메이션끼리 사이에 멈추는 시간(초)
pause_time = 1.0


# 애니메이션이 계속 돌고 있는지 나타내는 변수
running = True


# 키보드/마우스 이벤트를 처리하는 함수
# 이 함수가 없으면 이벤트가 계속 쌓여서 창이 멈추고 응답하지 않게 된다
def handle_events():
    global running

    for event in get_events():
        # 창을 닫는 이벤트
        if event.type == SDL_QUIT:
            running = False
        # 키를 누른 이벤트
        elif event.type == SDL_KEYDOWN:
            # Esc 키 또는 Q 키를 누르면 종료한다
            if event.key == SDLK_ESCAPE or event.key == SDLK_q:
                running = False


# 전달받은 frames 리스트를 반복 재생하는 함수
def play_animation(frames):
    # 현재 보여줄 프레임의 인덱스
    frame = 0

    # repeat_count 번 반복한다
    for repeat in range(repeat_count):
        # 프레임 개수만큼 순서대로 반복한다
        for step in range(len(frames)):
            # (left, top, width, height)를 각각 unpacking 한다
            left, top, width, height = frames[frame]

            # 화면을 지운다 (잔상을 없애기 위해 매 프레임마다 지운다)
            clear_canvas()

            # 스프라이트시트에서 프레임 부분만 잘라서 그린다
            character.clip_draw(
                # 원본에서 잘라낼 영역: 왼쪽 x, 아래쪽 y, 가로길이, 세로길이
                # pico2d의 y좌표는 아래쪽에서부터 올라가므로 위쪽 좌표에서 세로길이를 빼서 변환한다
                left, character.h - top - height, width, height,
                # 캔버스에 그릴 위치: 가로 중심, 세로 중심
                # 발 위치를 baseline에 맞추기 위해 세로 중심을 아래쪽으로 옮긴다
                center_x, baseline + (height * scale) // 2,
                # 그릴 크기: 원본 크기에 확대 배율을 곱한다
                width * scale, height * scale
            )

            # 화면에 실제로 반영한다
            update_canvas()

            # 키보드/마우스 이벤트를 처리한다 (이게 없으면 창이 멈춘다)
            handle_events()

            # 종료 신호가 들어오면 더 이상 그리지 않고 빠져나간다
            if not running:
                return

            # 다음 프레임으로 이동한다 (마지막 프레임 다음에는 처음으로 돌아간다)
            frame = (frame + 1) % len(frames)
            # 한 프레임을 보여줄 시간만큼 기다린다
            delay(frame_time)

        # 종료 신호가 들어오면 반복을 중단한다
        if not running:
            return


# 아래 4가지 애니메이션을 순서대로 무한 반복해서 재생한다
# (Esc 키 또는 Q 키를 누르거나 창을 닫으면 종료된다)
while running:
    # 등장 애니메이션 재생
    play_animation(appear_frame)
    # 등장 애니메이션 끝나고 잠시 멈춘다
    delay(pause_time)

    # 승리 포즈 애니메이션 재생
    play_animation(victory_frame)
    # 승리 포즈 애니메이션 끝나고 잠시 멈춘다
    delay(pause_time)

    # 달리기 애니메이션 재생
    play_animation(run_frame)
    # 달리기 애니메이션 끝나고 잠시 멈춘다
    delay(pause_time)

    # 슬라이딩 애니메이션 재생
    play_animation(sliding_frame)
    # 슬라이딩 애니메이션 끝나고 잠시 멈춘다
    delay(pause_time)

# 반복이 끝나면 캔버스(화면)를 닫는다
close_canvas()
