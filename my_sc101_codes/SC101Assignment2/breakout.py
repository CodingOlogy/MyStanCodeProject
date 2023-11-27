"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    graphics.life = NUM_LIVES
    # Add the animation loop here!
    while True:
        if graphics.life == 0 or graphics.broken_bricks_num == 0:
            break
        graphics.bounce()
        graphics.check_collision()
        graphics.ball.move(graphics.get_vx(), graphics.get_vy())
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
