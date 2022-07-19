#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/04/11 11:13
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : demo2.py
Software: PyCharm
'''
"""
QGraphicsItem 的动态波纹线
By Linyoubiao
2020-03-21
"""

from PyQt5.QtWidgets import (QApplication, QGraphicsItem, QGraphicsScene, QGraphicsView)
from PyQt5.QtCore import (QLine, QLineF, QPoint, QPointF, QRect, QRectF, QTimer, QTime, Qt)
from PyQt5.QtGui import (QBrush, QPen, QImage, QPicture, QPixmap,
                         QPainter, QPainterPath, QColor,
                         QFont, QFontMetrics, QFontDatabase,
                         QLinearGradient)


class Shape(QGraphicsItem):
    shape_rect = QRectF(QPointF(0, 0), QPointF(100, 100))

    def __init__(self):
        super(Shape, self).__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(100)
        self.line_offset = 0

        self.setFlag(QGraphicsItem.ItemIsMovable)

    def timerEvent(self):
        self.line_offset += 1
        self.prepareGeometryChange()

    def boundingRect(self):
        return QRectF(QPointF(0, 0), QPointF(500, 500))

    def paint(self, painter, option, widget):
        pen = QPen(Qt.black, 2.0, Qt.SolidLine)
        pen.setCosmetic(False)
        painter.setPen(pen)
        painter.drawRect(Shape.shape_rect)

        pen.setColor(Qt.green)
        pen.setCapStyle(Qt.FlatCap)
        pen.setDashPattern((5, 5))
        pen.setDashOffset(self.line_offset)
        painter.setPen(pen)
        painter.drawRect(Shape.shape_rect)

        gradient = QLinearGradient(100, 100, 200, 200)
        gradient.setColorAt(0, Qt.red)
        gradient.setColorAt(1, Qt.green)

        font = QFont()
        # 设置字体
        font.setFamily("Webdings")
        # 设置字体大小像素
        font.setPixelSize(20)
        # 设置字体为粗体
        font.setBold(True)
        # 设置字体为斜体
        font.setItalic(False)
        # 设置字体大小
        font.setPointSize(70)
        # 设置下划线
        font.setUnderline(True)
        # 设置上划线
        font.setOverline(True)
        font_path = QPainterPath()
        font_path.addText(10, 180, font, "arar")
        painter.setPen(Qt.NoPen)
        painter.setBrush(gradient)
        painter.drawPath(font_path)


class Shape_Scene(QGraphicsScene):
    def __init__(self):
        super(Shape_Scene, self).__init__()
        self.image = QPixmap("Model.png")
        self.addPixmap(self.image)
        self.shape = Shape()
        self.addItem(self.shape)


class Shape_View(QGraphicsView):
    def __init__(self, parent=None):
        super(Shape_View, self).__init__(parent)
        self.shape_scene = Shape_Scene()
        self.setScene(self.shape_scene)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    font_database = QFontDatabase()
    for font in font_database.families():
        print(font)

    mainView = Shape_View()
    mainView.show()

    sys.exit(app.exec_())