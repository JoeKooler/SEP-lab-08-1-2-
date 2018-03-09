from turtle import *

class Disk(object):
    def __init__(self, dname, xpos, ypos, dh, dw, col = "red"):
        self.name = dname
        self.x = xpos
        self.y = ypos
        self.h = dh
        self.w = dw
        self.color = col

    def showdisk(self):
        pu()
        goto(x,y)
        pd()
        fillcolor(color)
        begin_fill()
        seth(0)
        fd(w / 2)
        lt(90)
        fd(h)
        lt(90)
        fd(w)
        lt(90)
        fd(h)
        lt(90)
        fd(w / 2)
        end_fill()

    def newpos(self,x,y):
        self.x = x
        self.y = y

    def cleardisk(self):
        pu()
        goto(x,y)
        pd()
        fillcolor("white")
        pencolor("white")
        begin_fill()
        seth(0)
        fd(w / 2)
        lt(90)
        fd(h)
        lt(90)
        fd(w)
        lt(90)
        fd(h)
        lt(90)
        fd(w / 2)
        end_fill()
        pencolor("black")
        fillcolor(color)

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getname(self):
        return self.name

    def geth(self):
        return self.h

    def getw(self):
        return self.w