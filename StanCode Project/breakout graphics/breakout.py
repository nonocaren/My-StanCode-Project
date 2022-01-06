"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This lesson teach us how to use class and object to create a game using ball to hit the brick and remove them.
While creating this game, we also have to learn to separate our code into user file and coder file.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel
from campy.gui.events.mouse import onmouseclicked

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts
graphics = BreakoutGraphics()
live = NUM_LIVES
is_moving = False

# add live lable
lives = GLabel('Life: ' + str(live))

# all bricks
all_bricks = graphics.cnt
# get velocity
vx = graphics.get_dx()
vy = graphics.get_dy()

def main():
    global graphics
    onmouseclicked(moving_ball)
    lives.color = 'dimgray'
    lives.font = '-45'
    graphics.window.add(lives, 0, lives.height)

def moving_ball(event):
    global live, lives, is_moving, all_bricks, vx, vy
    if not is_moving:
        if live > 0:
            while True:
                graphics.ball.move(vx, vy)
                # ball hit paddle will bounce back
                if graphics.ball.y + graphics.ball.height >= graphics.paddle.y:
                    if graphics.ball.x >= graphics.paddle.x:
                        if graphics.ball.x + graphics.ball.width <= graphics.paddle.x + graphics.paddle.width:
                            vy = -vy

                graphics.set_ball_velocity()

                # check if still have ball and print 'Win'
                if all_bricks == 0:
                    graphics.window.add(graphics.result, (graphics.window_width - graphics.result.width) / 2,
                        (graphics.window_height - graphics.result.height) / 2)
                    break

                # ball hit the wall will bounce randomly
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window_width:
                    vx = -vx
                    graphics.set_ball_velocity()
                if graphics.ball.y <= 0 or graphics.ball.y + graphics.ball.height >= graphics.window_height:
                    vy = -vy
                    graphics.set_ball_velocity()

                # if ball fall out of window will minus 1 live and break
                if graphics.ball.y + graphics.ball.height >= graphics.window_height:
                    graphics.window.add(graphics.ball, (graphics.window_width - graphics.ball.width) / 2,
                                    (graphics.window_height - graphics.ball.height) / 2)
                    live -= 1
                    lives.text = 'Lives: ' + str(live)
                    break

                # ball's 4 corner
                ball_top_left = graphics.window.get_object_at(graphics.ball.x + graphics.ball_radius, graphics.ball.y)
                ball_bot_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball_radius)
                ball_top_right = graphics.window.get_object_at(graphics.ball.x + graphics.ball_radius*2,
                                                               graphics.ball.y + graphics.ball_radius)
                ball_bot_right = graphics.window.get_object_at(graphics.ball.x + graphics.ball_radius,
                                                               graphics.ball.y + graphics.ball_radius*2)

                # remove bricks
                if ball_top_left is not None and ball_top_left is not graphics.paddle and ball_top_left is not lives:
                    graphics.window.remove(ball_top_left)
                    vy = -vy
                    all_bricks = all_bricks - 1

                if ball_bot_left is not None and ball_bot_left is not graphics.paddle and ball_bot_left is not lives:
                    graphics.window.remove(ball_bot_left)
                    vx = -vx
                    all_bricks = all_bricks - 1

                if ball_top_right is not None and ball_top_right is not graphics.paddle and ball_top_right is not lives:
                    graphics.window.remove(ball_top_right)
                    vx = -vx
                    all_bricks = all_bricks - 1

                if ball_bot_right is not None and ball_bot_right is not graphics.paddle and ball_bot_right is not lives:
                    graphics.window.remove(ball_bot_right)
                    vy = -vy
                    all_bricks = all_bricks - 1
                pause(FRAME_RATE)
                is_moving = True

        else:
            lose = GLabel('You Lose!')
            lose.color = 'darkslateblue'
            lose.font = '-50'
            graphics.window.add(lose, (graphics.window_width - lose.width) / 2,
                                (graphics.window_height - graphics.ball.height) / 2)
    else:
        is_moving = False


if __name__ == '__main__':
    main()
