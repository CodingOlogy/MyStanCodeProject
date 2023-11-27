"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    # 橫線的總長度，用來計算垂直線區域的總寬度
    line_width = width - 2*GRAPH_MARGIN_SIZE
    # x座標為邊緣距離+line_width除以垂直線的數目(len(YEARS))再乘上year_index
    x_coordinate = GRAPH_MARGIN_SIZE + line_width // len(YEARS)*year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # 畫垂直線
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW, )


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    # 將CANVAS_HEIGHT分割成最高的名次，讓視覺上更直觀
    y_index = (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE) / MAX_RANK
    for i in range(len(lookup_names)):
        for j in range(len(YEARS)):
            # 處理畫線數量>顏色數量的情況
            if i < len(COLORS):
                color = COLORS[i]
            elif i >= len(COLORS):
                # 用來計算畫線的數目是COLORS長度的幾倍
                count = int(i / len(COLORS))
                color = COLORS[int(i-len(COLORS)*count)]
            # 前一年的年份不在資料內
            no_year_data = str(YEARS[j]) not in name_data[lookup_names[i]]
            # 後一年的年份也不再資料內
            if j+1 < len(YEARS):
                no_year_data_2 = str(YEARS[j+1]) not in name_data[lookup_names[i]]
            # 取前位座標
            if no_year_data:
                rank = '*'
                x1 = get_x_coordinate(CANVAS_WIDTH, j)
                y1 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                canvas.create_text(x1 + TEXT_DX, y1, text=lookup_names[i]+' '+rank, fill=color, anchor= tkinter.SW)
            else:
                rank = name_data[lookup_names[i]][str(YEARS[j])]
                x1 = get_x_coordinate(CANVAS_WIDTH, j)
                y1 = int(name_data[lookup_names[i]][str(YEARS[j])])*y_index+GRAPH_MARGIN_SIZE
                y1 = int(y1)
                canvas.create_text(x1 + TEXT_DX, y1, text=lookup_names[i]+' '+rank, fill=color, anchor=tkinter.SW)
            # 後一年有資料
            if j+1 < len(YEARS) and not no_year_data_2:
                x2 = get_x_coordinate(CANVAS_WIDTH, j+1)
                y2 = int(name_data[lookup_names[i]][str(YEARS[j+1])])*y_index+GRAPH_MARGIN_SIZE
                y2 = int(y2)
                canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)
            # 後一年無資料
            elif j+1 < len(YEARS) and no_year_data_2:
                x2 = get_x_coordinate(CANVAS_WIDTH, j + 1)
                y2 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
