"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # 把一些var都用instance var接住，以利後續使用
        self.ball_radius = ball_radius
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle_offset = paddle_offset
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_offset = brick_offset
        self.brick_spacing = brick_spacing
        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)
        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height, x=(self.window_width-paddle_width)/2, y=self.window_height - paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(width=ball_radius*2, height=ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window_width-self.ball.width)/2, y=(self.window_height-self.ball.width)/2)
        # Draw bricks
        """
        1.利用for loop來創造行跟列的bricks
        2.在for loop外設定bricks的y座標
        """
        self.brick_offset = brick_offset
        for i in range(self.brick_cols):
            # 每列都要從x座標為0開始打印，故x座標會在每列開始打印前重置
            x = 0
            for j in range(self.brick_rows):
                self.bricks = GRect(self.brick_width, self.brick_height, x=x, y=self.brick_offset)
                self.bricks.filled = True
                if i <= 1:
                    self.bricks.fill_color = 'red'
                elif 1 < i <= 3:
                    self.bricks.fill_color = 'orange'
                elif 3 < i <= 5:
                    self.bricks.fill_color = 'yellow'
                elif 5 < i <= 7:
                    self.bricks.fill_color = 'green'
                else:
                    self.bricks.fill_color = 'blue'
                self.window.add(self.bricks)
                x += self.brick_spacing + self.brick_width
            self.brick_offset += self.brick_spacing + self.brick_height
        # Default initial velocity for the ball
        # Initialize our mouse listeners
        self.__dx = 0
        self.__dy = 0
        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_move)
        # 設定球是否運動的開關
        self.is_ball_moved = False
        # 設定遊戲終止條件：life跟broken_bricks_num
        self.life = 0
        self.broken_bricks_num = self.brick_rows * self.brick_cols

    def ball_move(self, event):
        """
        1.is_ball_moved開關打開
        2.設定__dx,__dy之數值
        """
        self.is_ball_moved = True
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = - self.__dx

    def paddle_move(self, mouse):
        """
        :param mouse: 鼠標的位置
        :return: 利用onmousemoved讓paddle跟隨鼠標的位置移動，且鼠標的位置在paddle的中間
        """
        # 若已經通關或失敗，則跳出此function
        if self.life == 0 or self.broken_bricks_num == 0:
            return
        self.paddle.x = mouse.x - self.paddle.width/2
        # 設定條件讓paddle不會超過兩側
        if mouse.x - self.paddle.width/2 <= 0:
            self.paddle.x = 0
        elif mouse.x + self.paddle.width/2 >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width

    def get_vx(self):
        # 使球運動的x軸變數，利用getter讓User端得到加密後的數值
        return self.__dx

    def get_vy(self):
        # 使球運動的y軸變數，利用getter讓User端得到加密後的數值
        return self.__dy

    def set_vy(self):
        self.__dy = -self.__dy

    def check_collision(self):
        """
        確認是否碰撞bricks
        :return: 若碰到brick則啟動collision(obj)
        """
        x1 = self.ball.x
        y1 = self.ball.y
        x2 = self.ball.x + 2 * self.ball_radius
        y2 = y1
        x3 = x2
        y3 = self.ball.y + 2 * self.ball_radius
        x4 = x1
        y4 = y3

        obj1 = self.window.get_object_at(x1, y1)
        obj2 = self.window.get_object_at(x2, y2)
        obj3 = self.window.get_object_at(x3, y3)
        # option + shift + 下 = 換行
        obj4 = self.window.get_object_at(x4, y4)

        if obj1 is not None:
            self.collision(obj1)
        elif obj2 is not None:
            self.collision(obj2)
        elif obj3 is not None:
            self.collision(obj3)
        elif obj4 is not None:
            self.collision(obj4)

    def collision(self, obj):
        """
        :param obj: 在球的運動過程中，如果觸碰到的物件
        :return: 將__dy*-1或者消除bricks
        """
        if obj == self.paddle:
            self.__dy = -self.__dy
            # 尚未處理碰到板子側邊的狀況
        if obj != self.paddle and obj != self.ball:
            # 碰到bricks的狀況，broken_bricks_num需要-1，來判斷是否該終止遊戲
            self.__dy = -self.__dy
            self.window.remove(obj)
            self.broken_bricks_num -= 1

    def bounce(self):
        """
        :return:碰到牆壁時，需要把dx或dy轉為負數。碰到左右牆壁更改dx，碰到上面的牆要更改dy
        如果碰到下面的牆壁，則扣一命，並新增一顆球到視窗
        """
        if self.ball.x <= 0 or self.ball.x + self.ball.width > self.window.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy
        elif self.ball.y + self.ball.width >= self.window.height + self.ball.width:
            self.life -= 1
            print(self.life)
            # self.is_ball_moved = False
            self.__dy = 0
            self.__dx = 0
            if self.life != 0:
                self.ball = GOval(width=self.ball_radius * 2, height=self.ball_radius * 2)
                self.ball.filled = True
                self.window.add(self.ball, x=(self.window_width - self.ball.width) / 2, y=(self.window_height - self.ball.width) / 2)




