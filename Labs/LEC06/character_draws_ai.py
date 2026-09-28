from pico2d import *

# 캔버스 준비
open_canvas(800, 600)
character = load_image('character.png')

# 도형 정보를 한곳에 모아두기
CENTER = (400, 300)          # 원의 중심
RADIUS = 200                # 원의 반지름
RECTANGLE = [(50, 550), (750, 550), (750, 50), (50, 50)]  # 사각형 꼭짓점
TRIANGLE = [(400, 500), (100, 100), (700, 100)]           # 삼각형 꼭짓점
STEP = 5                    # 도형을 따라 움직이는 간격
MOVE_TIME = 0.01            # 한 번 움직일 때의 대기 시간
QUIT_KEYS = (SDLK_q,)       # 누르면 종료되는 키

running = True              # False 가 되면 메인 루프가 종료됨


def draw_character(x, y):  # 캐릭터 그리기 함수
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(MOVE_TIME)


def line_positions(start, end):  # 두 점을 잇는 선 위의 좌표를 순서대로 만들어 내기
    x1, y1 = start
    x2, y2 = end
    length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    count = int(length // STEP)
    if count == 0:
        count = 1
    for i in range(count + 1):
        t = i / count
        yield (x1 + (x2 - x1) * t, y1 + (y2 - y1) * t)


def circle_positions(cx, cy, radius):  # 원 위의 좌표를 순서대로 만들어 내기
    for degree in range(360):
        theta = math.radians(degree)
        yield (cx + radius * math.cos(theta), cy + radius * math.sin(theta))


def shape_positions(points):  # 꼭짓점 목록을 순서대로 연결한 좌표들
    for i in range(len(points)):
        for position in line_positions(points[i], points[(i + 1) % len(points)]):
            yield position


def shape_sequence():  # 원 -> 사각형 -> 삼각형을 계속 반복하는 좌표열
    while True:
        for position in circle_positions(CENTER[0], CENTER[1], RADIUS):
            yield position
        for position in shape_positions(RECTANGLE):
            yield position
        for position in shape_positions(TRIANGLE):
            yield position


def handle_events():  # 이벤트를 읽어 종료할지 결정하기 - 이걸 부르지 않으면 창이 응답중지로 표시됨
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key in QUIT_KEYS:
            running = False
    return running


# 메인 - 한 번 움직일 때마다 이벤트를 먼저 처리하므로 창이 멈추지 않는다
positions = shape_sequence()
while running:
    if not handle_events():
        break
    x, y = next(positions)
    draw_character(x, y)

close_canvas()
