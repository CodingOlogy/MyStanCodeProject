"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Bmo
    This is my first American cartoon series, and it's definitely not because of its simple design that I chose it.
    """
    """
    TODO:
    1.先做出最大的軀體+上色(aquamarine)
    2.做顯示螢幕+上色(azure)
    3.做出按鈕(limegreen, blue, red, yellow, aqua)
    4.做出表情（eye, smile）
    """
    window = GWindow(width=800, height=400, title='')
    body = GRect(200, 350, x=250, y=30)
    body.filled = True
    body.fill_color = 'aquamarine'
    window.add(body)
    monitor = GRect(150, 150, x=275, y=50)
    monitor.filled = True
    monitor.fill_color = 'azure'
    window.add(monitor)
    bottom1 = GRect(70, 10, x=275, y=70 + monitor.height)
    bottom1.filled = True
    bottom1.fill_color = 'green'
    window.add(bottom1)
    bottom2 = GRect(35, 10, x=275, y=120 + monitor.height + bottom1.height)
    bottom2.filled = True
    bottom2.fill_color = 'yellow'
    window.add(bottom2)
    bottom3 = GRect(10, 35, x=287.5, y=107 + monitor.height + bottom1.height)
    bottom3.filled = True
    bottom3.fill_color = 'yellow'
    window.add(bottom3)
    bottom4 = GRect(35, 10, x=275, y=330)
    bottom4.filled = True
    bottom4.fill_color = 'blue'
    window.add(bottom4)
    bottom5 = GRect(35, 10, x=320, y=330)
    bottom5.filled = True
    bottom5.fill_color = 'blue'
    window.add(bottom5)
    bottom6 = GOval(15, 15, x=390, y=70 + monitor.height)
    bottom6.filled = True
    bottom6.fill_color = 'blue'
    window.add(bottom6)
    bottom7 = GPolygon()
    bottom7.add_vertex((380, 120 + monitor.height + bottom1.height))
    bottom7.add_vertex((400, 120 + monitor.height + bottom1.height))
    bottom7.add_vertex((390, 100 + monitor.height + bottom1.height))
    bottom7.filled = True
    bottom7.fill_color = 'aqua'
    window.add(bottom7)
    bottom8 = GOval(25, 25, x=380, y=150 + monitor.height)
    bottom8.filled = True
    bottom8.fill_color = 'red'
    window.add(bottom8)
    bottom9 = GOval(15, 15, x=410, y=130 + monitor.height)
    bottom9.filled = True
    bottom9.fill_color = 'yellow'
    window.add(bottom9)
    eye1 = GOval(5, 5, x=310, y=80)
    eye1.filled = True
    window.add(eye1)
    eye2 = GOval(5, 5, x=380, y=80)
    eye2.filled = True
    window.add(eye2)
    smile = GArc(80, 100, 210, 130, x=310, y=90)
    window.add(smile)
    bmo = GLabel('Hi!, I am BMO!', x=50, y=50)
    bmo.font = '-20'
    window.add(bmo)


if __name__ == '__main__':
    main()
