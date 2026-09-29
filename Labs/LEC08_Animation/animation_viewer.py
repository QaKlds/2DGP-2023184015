from pico2d import *

open_canvas()

character = load_image('megaman.png')

row1_frames = [
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


play_animation(row1_frames)
delay(pause_time)

# play_animation(row2_frames)
# delay(pause_time)

# play_animation(row4_frames)
# delay(pause_time)

close_canvas()


# { (12,70), (32,0) },  {(33,70), (62,0)}, {(63,70), (109, 0)}, {(110,70), (148, 0)}, {(148, 70), (184, 0)}, {(184,70), (223, 0)}, {(224,70), (267, 0)}, {(268,70),(310,0)}, {(310, 70),(353, 0)}, {(353, 70), (395, 0)}, {(395. 70), (437,0)}, {(437, 70), (479, 0)}, {(479, 70), (521, 0)}    