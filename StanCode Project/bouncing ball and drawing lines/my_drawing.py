"""
File: R2D2
Name:Caren Yang
----------------------
This file use campy to draw on a GWindow object
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    This is the code to print R2D2 from Star Wars on the window.
    """
    window = GWindow(width=800, height=500, title='R2D2')
    head = GOval(150, 150, x=350, y=100)
    head.filled = True
    head.color = 'grey'
    head.fill_color = 'grey'
    window.add(head)
    body = GRect(160, 160, x=345, y=200)
    body.filled = True
    body.color = 'grey'
    body.fill_color = 'grey'
    window.add(body)
    head_deco1 = GRect(50, 10, x=368, y=120)
    head_deco1.color = 'navy'
    head_deco1.filled = True
    head_deco1.fill_color = 'navy'
    window.add(head_deco1)
    head_deco2 = GRect(50, 10, x=430, y=120)
    head_deco2.color = 'navy'
    head_deco2.filled = True
    head_deco2.fill_color = 'navy'
    window.add(head_deco2)
    eye = GRect(35, 35, x=405, y=140)
    eye.filled = True
    eye.fill_color = 'navy'
    eye.color = 'navy'
    window.add(eye)
    eye1 = GOval(30, 30, x=408, y=143)
    eye1.filled = True
    window.add(eye1)
    body1 = GRect(25, 100, x=353, y=208)
    body1.filled = True
    body1.color = 'white'
    body1.fill_color = 'white'
    window.add(body1)
    head_deco3 = GRect(25, 18, x=353, y=180)
    head_deco3.color = 'navy'
    head_deco3.filled = True
    head_deco3.fill_color = 'navy'
    window.add(head_deco3)
    head_deco4 = GRect(20, 7, x=380, y=180)
    head_deco4.color = 'navy'
    head_deco4.filled = True
    head_deco4.fill_color = 'navy'
    window.add(head_deco4)
    head_deco5 = GRect(20, 7, x=380, y=191)
    head_deco5.color = 'navy'
    head_deco5.filled = True
    head_deco5.fill_color = 'navy'
    window.add(head_deco5)
    head_deco6 = GRect(40, 18, x=403, y=180)
    head_deco6.color = 'navy'
    head_deco6.filled = True
    head_deco6.fill_color = 'navy'
    window.add(head_deco6)
    head_deco6_1 = GOval(15, 15, x=423, y=181)
    head_deco6_1.filled = True
    head_deco6_1.color = 'red'
    head_deco6_1.fill_color = 'red'
    window.add(head_deco6_1)
    head_deco7 = GRect(24, 18, x=447, y=180)
    head_deco7.color = 'navy'
    head_deco7.filled = True
    head_deco7.fill_color = 'navy'
    window.add(head_deco7)
    head_deco7_1 = GOval(13, 13, x=453, y=183)
    head_deco7_1.filled = True
    head_deco7_1.color = 'grey'
    head_deco7_1.fill_color = 'grey'
    window.add(head_deco7_1)
    head_deco8 = GRect(22, 18, x=475, y=180)
    head_deco8.color = 'navy'
    head_deco8.filled = True
    head_deco8.fill_color = 'navy'
    window.add(head_deco8)
    body2 = GRect(80, 3, x=385, y=208)
    body2.filled = True
    body2.color = 'navy'
    body2.fill_color = 'navy'
    window.add(body2)
    body3 = GRect(80, 3, x=385, y=215)
    body3.filled = True
    body3.color = 'navy'
    body3.fill_color = 'navy'
    window.add(body3)
    body4 = GRect(80, 3, x=385, y=223)
    body4.filled = True
    body4.color = 'navy'
    body4.fill_color = 'navy'
    window.add(body4)
    body5 = GRect(23, 25, x=385, y=230)
    body5.filled = True
    body5.color = 'white'
    body5.fill_color = 'white'
    window.add(body5)
    body6 = GRect(33, 25, x=413, y=230)
    body6.filled = True
    body6.color = 'navy'
    body6.fill_color = 'navy'
    window.add(body6)
    body7 = GRect(18, 80, x=450, y=230)
    body7.filled = True
    body7.color = 'white'
    body7.fill_color = 'white'
    window.add(body7)
    body8 = GRect(11, 6, x=385, y=260)
    body8.filled = True
    body8.color = 'white'
    body8.fill_color = 'white'
    window.add(body8)
    body9 = GRect(11, 6, x=385, y=272)
    body9.filled = True
    body9.color = 'white'
    body9.fill_color = 'white'
    window.add(body9)
    body10 = GRect(11, 6, x=385, y=284)
    body10.filled = True
    body10.color = 'white'
    body10.fill_color = 'white'
    window.add(body10)
    body11 = GRect(11, 6, x=385, y=296)
    body11.filled = True
    body11.color = 'white'
    body11.fill_color = 'white'
    window.add(body11)
    body12 = GRect(8, 45, x=399, y=260)
    body12.filled = True
    body12.color = 'white'
    body12.fill_color = 'white'
    window.add(body12)
    body12 = GRect(30, 45, x=414, y=260)
    body12.filled = True
    body12.color = 'navy'
    body12.fill_color = 'navy'
    window.add(body12)
    body13 = GRect(25, 100, x=475, y=208)
    body13.filled = True
    body13.color = 'white'
    body13.fill_color = 'white'
    window.add(body13)
    body14 = GRect(25, 20, x=354, y=313)
    body14.filled = True
    body14.color = 'white'
    body14.fill_color = 'white'
    window.add(body14)
    body15 = GRect(25, 20, x=385, y=313)
    body15.filled = True
    body15.color = 'white'
    body15.fill_color = 'white'
    window.add(body15)
    body16 = GOval(25, 20, x=415, y=313)
    body16.filled = True
    window.add(body16)
    body17 = GOval(18, 15, x=419, y=316)
    body17.filled = True
    body17.fill_color = 'grey'
    window.add(body17)
    body18 = GRect(20, 20, x=450, y=313)
    body18.filled = True
    body18.color = 'white'
    body18.fill_color = 'white'
    window.add(body18)
    body19 = GRect(10, 20, x=353, y=338)
    body19.filled = True
    body19.color = 'white'
    body19.fill_color = 'white'
    window.add(body19)
    body20 = GRect(8, 20, x=368, y=338)
    body20.filled = True
    body20.color = 'white'
    body20.fill_color = 'white'
    window.add(body20)
    body21 = GRect(25, 20, x=475, y=313)
    body21.filled = True
    body21.color = 'white'
    body21.fill_color = 'white'
    window.add(body21)
    body22 = GRect(25, 20, x=383, y=338)
    body22.filled = True
    body22.color = 'white'
    body22.fill_color = 'white'
    window.add(body22)
    body22 = GRect(28, 20, x=383, y=338)
    body22.filled = True
    body22.color = 'white'
    body22.fill_color = 'white'
    window.add(body22)
    body22 = GRect(25, 20, x=417, y=338)
    body22.filled = True
    body22.color = 'white'
    body22.fill_color = 'white'
    window.add(body22)
    body23 = GRect(15, 20, x=450, y=338)
    body23.filled = True
    body23.color = 'white'
    body23.fill_color = 'white'
    window.add(body23)
    body24 = GRect(15, 20, x=470, y=338)
    body24.filled = True
    body24.color = 'white'
    body24.fill_color = 'white'
    window.add(body24)
    body25 = GRect(12, 20, x=490, y=338)
    body25.filled = True
    body25.color = 'white'
    body25.fill_color = 'white'
    window.add(body25)
    bottom = GRect(20, 30, x=415, y=360)
    bottom.filled = True
    bottom.fill_color = 'grey'
    bottom.color = 'grey'
    window.add(bottom)
    bottom1 = GRect(60, 30, x=395, y=375)
    bottom1.filled = True
    bottom1.fill_color = 'grey'
    bottom1.color = 'grey'
    window.add(bottom1)
    bottom2 = GRect(52, 22, x=398, y=379)
    bottom2.filled = True
    bottom2.fill_color = 'white'
    bottom2.color = 'white'
    window.add(bottom2)
    leg1 = GRect(23, 170, x=330, y=200)
    leg1.filled = True
    leg1.fill_color = 'grey'
    leg1.color = 'grey'
    window.add(leg1)
    leg1_1 = GRect(50, 35, x=325, y=370)
    leg1_1.filled = True
    leg1_1.fill_color = 'grey'
    leg1_1.color = 'grey'
    window.add(leg1_1)
    leg2 = GRect(15, 170, x=333, y=202)
    leg2.filled = True
    leg2.fill_color = 'white'
    leg2.color = 'white'
    window.add(leg2)
    leg3 = GRect(15, 60, x=333, y=290)
    leg3.filled = True
    leg3.fill_color = 'navy'
    leg3.color = 'navy'
    window.add(leg3)
    leg1_2 = GRect(38, 25, x=330, y=373)
    leg1_2.filled = True
    leg1_2.fill_color = 'white'
    leg1_2.color = 'white'
    window.add(leg1_2)
    leg4 = GRect(23, 170, x=500, y=200)
    leg4.filled = True
    leg4.fill_color = 'grey'
    leg4.color = 'grey'
    window.add(leg4)
    leg4_1 = GRect(50, 35, x=495, y=370)
    leg4_1.filled = True
    leg4_1.fill_color = 'grey'
    leg4_1.color = 'grey'
    window.add(leg4_1)
    leg5 = GRect(15, 170, x=504, y=202)
    leg5.filled = True
    leg5.fill_color = 'white'
    leg5.color = 'white'
    window.add(leg5)
    leg6 = GRect(15, 60, x=504, y=290)
    leg6.filled = True
    leg6.fill_color = 'navy'
    leg6.color = 'navy'
    window.add(leg6)
    leg4_2 = GRect(39, 25, x=500, y=373)
    leg4_2.filled = True
    leg4_2.fill_color = 'white'
    leg4_2.color = 'white'
    window.add(leg4_2)









if __name__ == '__main__':
    main()
