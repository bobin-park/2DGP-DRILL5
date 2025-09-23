from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

# fill here
running = True

def handle_events():
    # fill here
    # global running  # 함수 내 사용되는 지역 변수가 아닌 전역 변수임을 명시함
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT: #window의 x버튼
            running = False
            #running가 전역변수가 아닌 지역변수로 인식됨
            # 즉, esc를 눌렀을 떄 running 라는 지역 변수가 생성되는 것으로 인식
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE: #esc키를 눌렀을 떄
            running = False
    pass

frame = 0
for x in range(0, 800, 5):

    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    # fill here
    handle_events()
    if not running:
        break;

    frame = (frame + 1) % 8
    delay(0.05)


close_canvas()
