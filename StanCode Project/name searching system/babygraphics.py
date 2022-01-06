"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
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
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
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
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_line = (width - 2*GRAPH_MARGIN_SIZE) / len(YEARS)
    x = GRAPH_MARGIN_SIZE + x_line*year_index
    return int(x)


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # top line and base line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)

    # draw line for each year
    for year in range(len(YEARS)):
        # loop through the constant and feed the get_x_coordinate to obtain x value
        x = get_x_coordinate(CANVAS_WIDTH, year)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[year], anchor=tkinter.NW)


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

    # Write your code below this line
    #################################
    for name in lookup_names:
        switch = True
        draw_line = False
        name_dic = name_data[name]

        year1_x = 0
        year1_y = 0
        year2_x = 0
        year2_y = 0

        for year in YEARS:
            x = lookup_names.index(name)

            while x >= len(COLORS):
                x -= len(COLORS)
            color = COLORS[x]

            if switch:
                switch = False
                year1_x = get_x_coordinate(CANVAS_WIDTH, YEARS.index(int(year)))

                if str(year) in name_dic: # check if the data is in the database of the name in that year

                    rank = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * int(name_dic[str(year)]) / MAX_RANK
                    # the y coordinate of the rank

                    year1_y = rank + GRAPH_MARGIN_SIZE
                    rank2 = int(name_dic[str(year)]) # the number of the rank
                    canvas.create_text(year1_x + TEXT_DX, year1_y, text=name + str(rank2), anchor=tkinter.NW,
                                       fill=color)
                else:
                    year1_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    canvas.create_text(year1_x + TEXT_DX, year1_y, text=name + '*', anchor=tkinter.SW, fill=color)

            else:
                # same as above
                switch = True
                year2_x = get_x_coordinate(CANVAS_WIDTH, YEARS.index(int(year)))

                if str(year) in name_dic:
                    rank = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * int(name_dic[str(year)]) / MAX_RANK
                    year2_y = rank + GRAPH_MARGIN_SIZE
                    rank2 = int(name_dic[str(year)])
                    canvas.create_text(year2_x + TEXT_DX, year2_y, text=name + str(rank2), anchor=tkinter.NW,
                                       fill=color)
                else:
                    year2_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    canvas.create_text(year2_x + TEXT_DX, year2_y, text=name + '*', anchor=tkinter.SW, fill=color)

            if draw_line:
                canvas.create_line(year1_x, year1_y, year2_x, year2_y, fill=color, width=LINE_WIDTH)
            draw_line = True


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
