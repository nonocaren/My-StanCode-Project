"""
File: bouncing_ball
Name:Caren Yang
-------------------------
This assignment
"""

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
START_Y = 4
TIME = 0

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
ball.filled = True
is_moving = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    # for i in range(3):
    window.add(ball, START_X, START_Y)
    onmouseclicked(start_game)


def start_game(e):
    global TIME, is_moving
    vy = 0
    vx = 0
    # ball.move(vx, vy)
    if not is_moving: # 程式執行的開關
        if TIME < 3:
            while True:
                ball.move(vx, vy)
                vy += GRAVITY
                if ball.y <= 0 or ball.y + SIZE >= window.height:
                    vy = -vy*REDUCE
                    vx += VX
                if ball.x <= 0 or ball.x + SIZE >= window.width:
                    window.add(ball, START_X, START_Y)
                    TIME += 1
                    break
                pause(DELAY)
                is_moving = True
    else:
        is_moving = False
        pass









if __name__ == "__main__":
    main()
