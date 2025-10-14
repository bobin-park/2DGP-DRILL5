#과제 파일
from pico2d import *

TUK_WIDTH,TUK_HEIGHT = 1280,1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

x, y = TUK_WIDTH//2,TUK_HEIGHT//2
running = False
frame=0

def handle_events():
    global x,y
    global running
    events=get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key  ==SDLK_UP:
            y+=10
            running = True
        elif event.type == SDL_KEYDOWN and event.key  ==SDLK_DOWN:
            y-=10
            running = True
        elif event.type == SDL_KEYDOWN and event.key  ==SDLK_LEFT:
            x-=10
            running = True
        elif event.type == SDL_KEYDOWN and event.key  ==SDLK_RIGHT:
            x+=10
            running = True



while 1:
    # global frame
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    if running:
        frame+1
    character.clip_draw( frame*100,100*1,100, 100, x,y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8