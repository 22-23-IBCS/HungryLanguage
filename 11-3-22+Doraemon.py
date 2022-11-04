from graphics import *
def main():
    win = GraphWin("Character", 800, 600)
    win.setBackground("white")
    #PART 1


    #Blue
    c = Oval(Point(170, 100), Point(630, 500))
    c.setFill("light blue")
    c.setOutline("black")
    c.draw(win)
    #White
    d = Oval(Point(200, 170), Point(600, 500))
    d.setFill("white")
    d.setOutline("black")
    d.draw(win)
    #Arc
    cir = Circle(Point(400, 320), 120)
    cir.draw(win)
    #rectangle for making arc
    rec = Rectangle(Point(280, 210), Point(520, 390))
    rec.setFill("white")
    rec.setOutline("white")
    rec.draw(win)

    rec1 = Polygon(Point(310, 211), Point(400, 175), Point(490, 211))
    rec1.setFill("white")
    rec1.setOutline("white")
    rec1.draw(win)

    


    #PART 2
    a1 = Oval(Point(320,130), Point(398, 230))
    a2 = Oval(Point(402,130), Point(480, 230))
    a1.setOutline("black")
    a2.setOutline("black")
    a1.setFill("white")
    a2.setFill("white")
    a1.draw(win)
    a2.draw(win)

    b = Rectangle(Point(200, 480), Point(600, 700))
    b.setOutline("white")
    b.setFill("white")
    b.draw(win)
    
    l = Rectangle(Point(270,465), Point(530, 481))
    l.setOutline("black")
    l.setFill("red")
    l.draw(win)
    

    b1 = Oval(Point(372, 195), Point(385, 215))
    b1.setFill("black")
    b1.draw(win)

    b2 = Oval(Point(415, 195), Point(428, 215))
    b2.setFill("black")
    b2.draw(win)

    c1 = Oval(Point(376, 198), Point(382, 212))
    c1.setFill("white")
    c1.draw(win)

    c2 = Oval(Point(418, 198), Point(424, 212))
    c2.setFill("white")
    c2.draw(win)

    ci = Circle(Point(400, 240), 29)
    ci.setFill("red")
    ci.draw(win)

    ci2 = Circle(Point(405, 233), 9)
    ci2.setFill("white")
    ci2.draw(win)

    l1 = Line(Point(400, 270), Point(400, 440))
    l1.draw(win)

    #PART 3
    line1 = Line(Point(240, 320),Point(340, 320))
    line1.draw(win)

    line2 = Line(Point(250, 270),Point(335, 290))
    line2.draw(win)

    line3 = Line(Point(250, 370),Point(335, 350))
    line3.draw(win)

    line4 = Line(Point(560, 320),Point(460, 320))
    line4.draw(win)

    line5 = Line(Point(550, 270),Point(465, 290))
    line5.draw(win)

    line6 = Line(Point(550, 370),Point(465, 350))
    line6.draw(win)

    p = Oval(Point(350, 30), Point(450, 70))
    p.setFill("#F3EAAF")
    p.setOutline("black")
    p.draw(win)
    
    q = Oval(Point(392, 46), Point(408, 54))
    q.setFill("yellow")
    q.setOutline("black")
    q.draw(win)

    s = Rectangle(Point(399, 100), Point(401, 54))
    s.setFill("yellow")
    s.draw(win)


    sign = Text(Point(700, 560), "TC")
    sign.setFace("courier")
    sign.setSize(16)
    sign.setStyle("italic")
    sign.draw(win)
    
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
