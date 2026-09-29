from pico2d import *

open_canvas()

character = load_image('megaman.png')

frame_lefts = [225, 395, 437, 479]
frame_top = 28
frame_width = 41
frame_height = 40
frame_bottom = character.h - frame_top - frame_height

scale = 3
center_x = 400
center_y = 300

repeat_count = 5
frame = 0

for repeat in range(repeat_count):
    for step in range(len(frame_lefts)):
        clear_canvas()

        character.clip_draw(
            frame_lefts[frame], frame_bottom, frame_width, frame_height,
            center_x, center_y,
            frame_width * scale, frame_height * scale
        )

        update_canvas()

        frame = (frame + 1) % len(frame_lefts)
        delay(0.1)

delay(1.0)

close_canvas()
