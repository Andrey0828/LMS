import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from random import randint


class Circle:
    def __init__(self, star_x, star_y, x, y, r):
        self.star_x = star_x
        self.star_y = star_y
        self.x = x
        self.y = y
        self.r = r

    def draw(self, paint):
        pen = QPen(QColor(255, 255, 0), 3, Qt.SolidLine)
        paint.setPen(pen)
        paint.setBrush(QColor(255, 255, 0))
        radius = int(self.r)
        paint.drawEllipse(self.star_x - radius, self.star_y - radius, 2 * radius, 2 * radius)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.object = None
        self.to_repaint = False
        self.pushButton.clicked.connect(self.dr)

    def paintEvent(self, event):
        if self.to_repaint:
            paint = QPainter()
            paint.begin(self)
            self.object.draw(paint)
            paint.end()

    def dr(self):
        self.x = randint(1, 551)
        self.y = randint(1, 705)
        r = randint(1, 200)
        self.object = Circle(self.x, self.y, self.x, self.y, r)
        self.to_repaint = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())