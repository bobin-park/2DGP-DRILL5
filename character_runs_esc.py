from pico2d import *

open_canvas()
grass = load_image('grass.png')
TUK_WIDTH,TUK_HEIGHT = 1280,1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

frame =0

def handle_events():
    global running
    global x,y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT: #window의 x버튼
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x,y=event.x,TUK_HEIGHT-1-event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE: #esc키를 눌렀을 떄
               running = False
    pass

running = True
x,y = TUK_WIDTH//2,TUK_HEIGHT//2 # // == 정수 나누기
hide_cursor() #커서 숨김

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    character.clip_draw(frame*100,100*1,100,100,x,y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)

# for x in range(0, 800, 5):
#
#     clear_canvas()
#     grass.draw(400, 30)
#     character.clip_draw(frame * 100, 100, 100, 100, x, 90)
#     update_canvas()
#     handle_events()
#     if not running:
#         break;
#
#     frame = (frame + 1) % 8
#     delay(0.05)
#
#
# close_canvas()
