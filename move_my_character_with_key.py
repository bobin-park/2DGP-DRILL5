#과제 파일
from pico2d import *

TUK_WIDTH,TUK_HEIGHT = 1280,1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

x, y = TUK_WIDTH//2,TUK_HEIGHT//2
running = True
frame=0

dir_x, dir_y = 0, 0
def handle_events():
    global running, dir_x, dir_y
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_ESCAPE:
                exit()
        elif event.type == SDL_KEYUP:
            dir_x = 0
            dir_y = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    x += dir_x * 5
    y += dir_y * 5
    character.clip_draw( frame*100,100*1,100, 100, x,y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8