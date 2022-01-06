"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.





class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)
        self.paddle_offset = PADDLE_OFFSET
        self.cnt = brick_cols*brick_rows

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (self.window_width - self.paddle.width) / 2, self.window_height - paddle_offset)


        # Center a filled ball in the graphical window
        self.ball_radius = BALL_RADIUS
        self.ball = GOval(ball_radius, ball_radius)
        self.ball.filled = True
        self.set_ball_position()
        self.window.add(self.ball, (self.window_width - self.ball.width) / 2,
                        (self.window_height - self.ball.height) / 2)
        # Default initial velocity for the ball
        self.__dx = 1
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        onmousemoved(self.play)

        # Show the player the result
        self.result = GLabel('You Win!')
        self.result.font = "-45"
        self.result.color = 'red'

        # Draw bricks
        brick_x = 0
        brick_y = brick_offset
        for i in range(brick_cols):
            brick_y += (brick_height + brick_spacing)
            for j in range(brick_rows):
                brick_x = (brick_width + brick_spacing) * j
                self.brick = GRect(brick_width, brick_height, x=brick_x, y=brick_y)
                self.brick.filled = True
                self.window.add(self.brick)

                if i == 0 or i == 1:
                    self.brick.fill_color = 'mintcream'
                if i == 2 or i == 3:
                    self.brick.fill_color = 'lightblue'
                if i == 4 or i == 5:
                    self.brick.fill_color = 'skyblue'
                if i == 6 or i == 7:
                    self.brick.fill_color = 'steelblue'
                if i == 8 or i == 9:
                    self.brick.fill_color = 'navy'


    def play(self, event):
        """
        This function help to keep the paddle in window
        :param event: mouse's data
        """
        self.paddle.x = event.x - self.paddle.width / 2
        if (event.x - self.paddle.width / 2) < 0:
            self.paddle.x = 0
        if (event.x - self.paddle.width / 2) > self.window_width - self.paddle.width:
            self.paddle.x = self.window_width - self.paddle.width

        self.paddle.y = self.window_height - self.paddle_offset

    def set_ball_position(self):
        self.ball.x = (0, self.window.width - self.ball.width)
        self.ball.y = (0, self.window.height - self.ball.height)

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    # def bounce_back(self):
    #     if self.ball_bot_right is self.paddle:
    #         self.__dy = -self.__dy
    #     if self.ball_bot_left is self.paddle:
    #         self.__dy = -self.__dy

    def set_ball_velocity(self):
        """
        This function can change x's velocity randomly
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = random.randint(1, INITIAL_Y_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
