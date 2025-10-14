import time
from pico2d import *

TUK_WIDTH,TUK_HEIGHT = 1280,1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

x, y = TUK_WIDTH//2,TUK_HEIGHT//2
running = False
right = True
frame=0

dir_x, dir_y = 0, 0
def handle_events():
    global running, dir_x, dir_y,right
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            running = True
            if event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_LEFT:
                right = False
                dir_x -= 1
            elif event.key == SDLK_RIGHT:
                right = True
                dir_x += 1
            elif event.key == SDLK_ESCAPE:
                exit()
        elif event.type == SDL_KEYUP:
            dir_x = 0
            dir_y = 0
            running=False

while 1:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)
    x += dir_x * 5
    y += dir_y * 5
    if x < 25:
        x = 25
    if x > TUK_WIDTH - 25:
        x = TUK_WIDTH - 25
    if y < 150:
        y = 150
    if y > TUK_HEIGHT - 100:
        y = TUK_HEIGHT - 100
    if running:
        frame = (frame + 1) % 8
        if right:
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
        else:
            character.clip_composite_draw(frame * 100, 100 , 100, 100, 0, 'h', x, y, 100, 100)

    else:
        frame = (frame + 1) % 8
        if right:
            character.clip_draw(frame * 100, 300, 100, 100, x, y)
        else:
            character.clip_composite_draw(frame * 100, 300, 100, 100,0, 'h', x, y, 100, 100)
    update_canvas()
    handle_events()
    time.sleep(0.05)