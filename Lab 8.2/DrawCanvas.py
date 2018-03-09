import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class CanvasWidget(QWidget):
    def __init__(self):
         QWidget.__init__(self, None)

    def clear(self):
         pass