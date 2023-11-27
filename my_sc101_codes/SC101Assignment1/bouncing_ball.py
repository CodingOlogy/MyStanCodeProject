"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
ball = GOval
can_fall = True  # 判斷球是否可落下
max_right_border_count = 3  # 判斷超過右側的最大次數
right_border_count = 0  # 判斷超過右側的次數

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global ball, right_border_count
    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    window.add(ball)
    ball.filled = True
    window.add(ball)
    onmouseclicked(move)


def move(mouse):
    global right_border_count, can_fall
    vy = 0
    if right_border_count >= max_right_border_count:
        return
    # 如果球處於不可落下狀態（落下中），必須直接跳出function避免讓球移動
    if not can_fall:
        return
    # 前面兩個判斷式如果都通過，代表可以讓球落下，而為了讓球落下中滑鼠不能點擊讓球二次落下，要把can_fall的開關關閉
    can_fall = False
    while True:
        ball.move(VX, vy)
        vy += GRAVITY
        pause(DELAY)
        # 當球觸地
        if ball.y >= 500 - SIZE:
            # 垂直移動變成負數
            vy = -vy
            # 乘上反彈的係數
            vy *= REDUCE
        # 如果球超出右側
        if ball.x > window.width:
            right_border_count += 1
            # 重置起點
            ball.x = START_X
            ball.y = START_Y
            # 重置球的位置之後，開關就可以打開
            can_fall = True
            # 為了不讓while loop一直跑，要跳出迴圈
            break


if __name__ == "__main__":
    main()
