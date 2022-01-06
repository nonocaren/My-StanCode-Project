"""
File: draw_line
Name: Caren Yang
-------------------------
This assignment is to practice the combination of campy and mouse event function.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant control the size of the circle that show up when the mouse click
SIZE = 5
# Global Variable
window = GWindow()
line = GLine(0, 0, 0, 0)
TIME = 0
x = 0
y = 0

oval = GOval(SIZE, SIZE)



def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(create) #點擊後會出現圓，並且得知它起點座標位置


def create(e):
    global TIME
    global x, y
    # while True:
    if TIME % 2 == 0:
        oval.filled = True
        oval.color = 'purple'
        oval.fill_color = 'purple'
        window.add(oval, e.x-SIZE/2, e.y-SIZE/2)  # 滑鼠點的位置在圓心
        x = e.x
        y = e.y
        TIME += 1
    else:
        oval1 = GOval(SIZE, SIZE)
        oval1.filled = False
        window.add(oval1, e.x, e.y)
        line1 = GLine(x, y, e.x, e.y)
        line1.color = 'purple'
        TIME += 1
        window.add(line1)
        window.remove(oval)
        window.remove(oval1)



if __name__ == "__main__":
    main()
