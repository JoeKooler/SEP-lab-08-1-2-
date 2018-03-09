import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Drawing")
        self.cat = QPixmap("images/cat.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        p.drawPolygon(
            QPoint(70,100), QPoint(100,110),
            QPoint(130,100), QPoint(100,150)
        )

        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(255,127,0))
        p.drawPie(50,150,100,100,0,180*16)

        p.drawPolygon(
            QPoint(50,200), QPoint(150,200), QPoint(100,400),
        )

        p.drawPixmap(QRect(200,100,336,203),self.cat)
        p.end()

# tawan modification
class Simple_drawing_window(Simple_drawing_window) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window 1")
        self.cat = QPixmap("images/cat1.jpg")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(20,255,0))
        p.drawPolygon(
            QPoint(70,100), QPoint(100,110),
            QPoint(130,100), QPoint(100,150)
        )

        p.setPen(QColor(100,127,0))
        p.setBrush(QColor(100,127,0))
        p.drawPie(50,150,100,100,0,180*16)

        p.drawPolygon(
            QPoint(50,200), QPoint(150,200), QPoint(100,400),
        )

        p.drawPixmap(QRect(200,100,336,203),self.cat)
        p.end()
# end tawan modification


def main():
    app = QApplication(sys.argv)

    try:
        w = Simple_drawing_window1()
        w.show()
    except:
        print("no win 1 implementer")

    try:
        w = Simple_drawing_window2()
        w.show()
    except:
        print("no win 2 implementer")

    try:
        w = Simple_drawing_window3()
        w.show()
    except:
        print("no win 3 implementer")

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())

