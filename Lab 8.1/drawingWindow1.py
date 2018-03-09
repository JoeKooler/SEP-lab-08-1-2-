from drawingWindow import Simple_drawing_window
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Simple_drawing_window1(Simple_drawing_window):
    def __init__(self):
        return super().__init__()

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(102,68,53))
        p.drawPie(80,150,100,100,0,180*16)
        p.drawPie(20,150,100,100,0,180*16)

        p.setPen(QColor(127,127,0))
        p.setBrush(QColor(236,159,242))
        p.drawPolygon(
            QPoint(20,200), QPoint(180,200), QPoint(100,400),
        )

        p.drawPixmap(QRect(200,100,336,203),self.cat)
        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window1()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())