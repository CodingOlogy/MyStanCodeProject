"""
File: 
Name:
-------------------------
TODO: 兩點一線
"""
from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
window = GWindow()
SIZE = 10
count = 0
x1 = 0
y1 = 0
x2 = 0
y2 = 0
c1 = 0
c2 = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    1.while True
    2.利用count % 2是否==0來更新&判斷奇數次or偶數次(if)
    3.空心圓要用 onmouseclicked + GOval
    4.線的起點為空心圓的圓心->記得在位置減去SIZE/2，空心圓的位置要用變數去紀錄（x1,y1,x2,y2）
    """
    onmouseclicked(circle_line)


def circle_line(mouse):
    """
    1.在奇數點擊時設定為畫圓
    2.偶數次點擊時為畫線
    3.在畫線之後，要把原本的圓消失（window.remove）
    """
    global count, x1, y1, x2, y2, c1, c2
    count += 1
    circle = GOval(SIZE/2, SIZE/2, x=mouse.x-SIZE/2/2, y=mouse.y-SIZE/2/2)
    window.add(circle)
    circle_x = mouse.x-SIZE/2/2
    circle_y = mouse.y-SIZE/2/2

    if count % 2 != 0:
        x1 = circle_x
        y1 = circle_y
        c1 = circle
    else:
        x2 = circle_x
        y2 = circle_y
        c2 = circle
    if count % 2 == 0 and count >= 2:
        line = GLine(x1, y1, x2, y2)
        window.remove(c1)
        window.remove(c2)
        window.add(line)






if __name__ == "__main__":
    main()
