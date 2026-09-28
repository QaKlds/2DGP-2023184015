# 실습 과제 진행
from pico2d import *

#맨처음 해야할 일은.
open_canvas(800, 600)
character = load_image('character.png')

def draw_character(x, y): #캐릭터 그리기 함수
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)

def draw_top():
    for x in range(50, 750, 5):
        draw_character(x, 550)

def draw_right():
    for y in range(550, 50, -5):
        draw_character(750, y)

def draw_bottom():
    for x in range(750, 50, -5):
        draw_character(x, 50)

def draw_left():
    for y in range(50, 550, 5):
        draw_character(50, y)

def move_circle():
    for degree in range(360): 
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        draw_character(x,y)

def draw_A():
    for x in range(400, 700, 5):
        y = (-4 / 3) * (x - 400) + 500
        draw_character(x, y)

def draw_B():
    for x in range(700, 100, -5):
        y = 100
        draw_character(x, y)

def draw_C():
    for x in range(100, 400, 5):
        y = (4 / 3) * (x - 100) + 100
        draw_character(x, y)

def move_rectangle():
    draw_top()
    draw_right()
    draw_bottom()
    draw_left()

def move_triangle():
    draw_A()
    draw_B()
    draw_C()



while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass

close_canvas()