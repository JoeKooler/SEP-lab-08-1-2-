import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from DrawCanvas import *

class PaintProgramWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        layout = QVBoxLayout()

        self.canvas = CanvasWidget()
        layout.addWidget(self.canvas)

        self.infoLbl = QLabel(self)
        self.infoLbl.setText("Drag the mouse to draw")
        layout.addWidget(self.infoLbl)

        self.clearBtn = QPushButton("Clear", self)
        layout.addWidget(self.clearBtn)

        self.setLayout(layout)
        self.setMinimumSize(530,600)

def main():
    app = QApplication(sys.argv)

    w = PaintProgramWindow()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())