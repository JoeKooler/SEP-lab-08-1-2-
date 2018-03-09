import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class CanvasWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.__isDrawing = False;

        self.__XandYPos = []

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        for point in self.__XandYPos:
            p.setPen(QColor(0, 0, 0))
            p.setBrush(QColor(0, 0, 0))
            p.drawPie(point[0], point[1], 20, 20, 0, 360 * 100)

        p.end()

    def mousePressEvent(self, event):
        self.__isDrawing = True
        self.update()

    def mouseReleaseEvent(self, event):
        self.__isDrawing = False
        self.update()

    def mouseMoveEvent(self, QMouseEvent):
        if(self.__isDrawing):
            X_Pos = QMouseEvent.x()
            Y_Pos = QMouseEvent.y()
            self.__XandYPos.append([X_Pos,Y_Pos])
        self.update()

    def clear(self):
        self.__XandYPos = []
        self.update()
