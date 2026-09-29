from pico2d import *

open_canvas()

character = load_image('megaman.png')

row1_frames = [
    (225, 28, 41, 40),
    (395, 28, 41, 40),
    (437, 28, 41, 40),
    (479, 28, 41, 40)
]

row2_frames = [
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

row4_frames = [
    (75, 204, 42, 40),
    (122, 207, 32, 37),
    (155, 209, 30, 35),
    (187, 207, 32, 37),
    (223, 206, 44, 35),
    (269, 209, 42, 35),
    (311, 205, 42, 38),
    (353, 203, 39, 36),
    (396, 203, 39, 36)
]

scale = 3
center_x = 400
baseline = 240
repeat_count = 5
frame_time = 0.1
pause_time = 1.0


def play_animation(frames):
    frame = 0

    for repeat in range(repeat_count):
        for step in range(len(frames)):
            left, top, width, height = frames[frame]

            clear_canvas()

            character.clip_draw(
                left, character.h - top - height, width, height,
                center_x, baseline + (height * scale) // 2,
                width * scale, height * scale
            )

            update_canvas()

            frame = (frame + 1) % len(frames)
            delay(frame_time)


# play_animation(row1_frames)
# delay(pause_time)

# play_animation(row2_frames)
# delay(pause_time)

play_animation(row4_frames)
delay(pause_time)

close_canvas()
