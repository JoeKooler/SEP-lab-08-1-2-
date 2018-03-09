from turtle import *

class Disk(object):
    def __init__(self, dname, xpos, ypos, dh, dw, col):
        self.name = dname
        self.x = xpos
        self.y = ypos
        self.h = dh
        self.w = dw
        self.color = col

    def showdisk(self):
        Turtle.pu()
        Turtle.goto(x,y)
        Turtle.pd()
        Turtle.fillcolor(color)
        Turtle.begin_fill()
        Turtle.seth(0)
        Turtle.fd(w / 2)
        Turtle.lt(90)
        Turtle.fd(h)
        Turtle.lt(90)
        Turtle.fd(w)
        Turtle.lt(90)
        Turtle.fd(h)
        Turtle.lt(90)
        Turtle.fd(w / 2)
        Turtle.end_fill()

    def newpos(self,x,y):
        self.x = x
        self.y = y

    def cleardisk(self):
        Turtle.pu()
        Turtle.goto(x,y)
        Turtle.pd()
        Turtle.fillcolor("white")
        Turtle.pencolor("white")
        Turtle.begin_fill()
        Turtle.seth(0)
        Turtle.fd(w / 2)
        Turtle.lt(90)
        Turtle.fd(h)
        Turtle.lt(90)
        Turtle.fd(w)
        Turtle.lt(90)
        Turtle.fd(h)
        Turtle.lt(90)
        Turtle.fd(w / 2)
        Turtle.end_fill()
        Turtle.pencolor("black")
        Turtle.fillcolor(color)

