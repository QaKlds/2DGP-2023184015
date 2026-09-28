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


def draw_character(x, y):  # 캐릭터 그리기 함수
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)


def draw_line(start, end):  # 두 점을 잇는 선을 따라 움직이기
    x1, y1 = start
    x2, y2 = end
    length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    count = int(length // STEP)
    if count == 0:
        count = 1
    for i in range(count + 1):
        t = i / count
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t
        draw_character(x, y)


def draw_circle(cx, cy, radius):  # 원 그리기
    for degree in range(360):
        theta = math.radians(degree)
        x = cx + radius * math.cos(theta)
        y = cy + radius * math.sin(theta)
        draw_character(x, y)


def draw_shape(points):  # 꼭짓점 목록을 순서대로 연결해서 도형 그리기
    for i in range(len(points)):
        draw_line(points[i], points[(i + 1) % len(points)])


def move_circle():  # 원 그리기
    draw_circle(CENTER[0], CENTER[1], RADIUS)


def move_rectangle():  # 사각형 그리기
    draw_shape(RECTANGLE)


def move_triangle():  # 삼각형 그리기
    draw_shape(TRIANGLE)


while True:  # 메인 - 원, 사각형, 삼각형을 계속 반복
    move_circle()
    move_rectangle()
    move_triangle()

close_canvas()
