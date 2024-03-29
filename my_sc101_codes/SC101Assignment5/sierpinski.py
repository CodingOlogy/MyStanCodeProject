"""
File: sierpinski.py
Name: 
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO:
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: 代表要畫幾層的三角形，同時代表需要將原本的三角形邊長切一半幾次
	:param length: 第一個三角形的邊長
	:param upper_left_x: 第一個三角形左上頂點之x座標
	:param upper_left_y: 第一個三角形左上頂點之y座標
	:return: 一個三角形的每三個角落都會新增三個邊長為1/2的三角形，重複order-1次
	"""
	# Base Case: 當order K的邊長已經被切了一半「Order常數次」，代表不需要再畫了，因為最小的三角形邊長，最多只會切一半至Order常數-1次。
	if length == LENGTH * pow(0.5, ORDER):
		pass
	else:
		# 三個邊長
		line1 = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		line2 = GLine(upper_left_x, upper_left_y, upper_left_x + 0.5 * length, upper_left_y + 0.866 * length)
		line3 = GLine(upper_left_x + 0.5 * length, upper_left_y + 0.866 * length, upper_left_x + length, upper_left_y)
		window.add(line1)
		window.add(line2)
		window.add(line3)
		# call itself
		# 左上角的三角形
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
		# 右上的三角形
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 2, upper_left_y)
		# 下面的三角形
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 2 / 2, upper_left_y + length / 2 * 0.866)


if __name__ == '__main__':
	main()
