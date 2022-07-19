#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/04/10 20:17
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : test.py
Software: PyCharm
'''
import math

"""
操作SQLite数据库
"""
from PyQt5.QtCore import Qt, QRectF, QLine
from PyQt5.QtGui import QColor, QPen, QBrush, QFont, QPixmap
from PyQt5.QtWidgets import (QGraphicsView, QGraphicsScene, QApplication, QGraphicsPixmapItem, QGraphicsItem)
class MainWindow(QGraphicsView):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # 创建场景
        self.scene = MyGraphScene(self)
        # settings
        self.grid_size = 20  # 网格尺寸
        self.grid_squares = 5  # 网格数量

        self._color_background = QColor('#393939')  # 背景颜色
        self._color_light = QColor('#2f2f2f')  # 线颜色
        self._color_dark = QColor('#292929')

        self._pen_light = QPen(self._color_light)  # 设置绘笔
        self._pen_light.setWidth(1)  # 绘笔宽度
        self._pen_dark = QPen(self._color_dark)  # 绘笔颜色
        self._pen_dark.setWidth(2)  # 深色宽度

        self.setBackgroundBrush(self._color_background)
        self.setSceneRect(0, 0, 500, 500)
        # 在场景中添加文字
        self.addPoint(0, 0, "p1")
        self.addPoint(50, 100, "p2")
        self.addPoint(100, 0, "p3")
        self.setSceneRect(QRectF(-150, -150, 400, 400))
        self.scale(2, 2)
        # 将场景加载到窗口
        self.setScene(self.scene)

    def addPoint(self, x, y, name):
        item = GraphicItem()
        item.setPos(x, y)
        self.scene.addItem(item)
        # self.scene.addRect(x, y, 16, 16, QPen(QColor(Qt.red)), QBrush(QColor(Qt.red)))


class MyGraphScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(MyGraphScene, self).__init__(parent)
    def drawBackground(self, painter, rect):
        # 在这里可以绘制底板，比如网格
        super().drawBackground(painter, rect)

        left = int(math.floor(rect.left()))  # 获取scene的最左边 x坐标
        right = int(math.ceil(rect.right()))  # 获取scene的最右边边 x坐标
        top = int(math.floor(rect.top()))  # 获取scene的最上边 y坐标
        bottom = int(math.ceil(rect.bottom()))  # 获取scene的最下边 y坐标

        first_left = left - (left % self.grid_size)
        first_top = top - (top % self.grid_size)

        lines_light, lines_dark = [], []
        for x in range(first_left, right, self.grid_size):
            if x % (self.grid_size * self.grid_squares) != 0:
                lines_light.append(QLine(x, top, x, bottom))
            else:
                lines_dark.append(QLine(x, top, x, bottom))

        for y in range(first_top, bottom, self.grid_size):
            if y % (self.grid_size * self.grid_squares) != 0:
                lines_light.append(QLine(left, y, right, y))
            else:
                lines_dark.append(QLine(left, y, right, y))

        # draw the lines
        painter.setPen(self._pen_light)
        if lines_light:
            painter.drawLines(*lines_light)  # 直接使用drawLines绘制多个线

        painter.setPen(self._pen_dark)
        if lines_dark:
            painter.drawLines(*lines_dark)

class GraphicItem(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pix = QPixmap("Model.png")
        self.width = 85
        self.height = 85
        self.setPixmap(self.pix)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setData(1, "hello woprld")


    # def mouseMoveEvent(self, event):
    #     """
    #     当移动节点时，实时更新整个场景中的所有连线，这里其实需要 关联控制比较好
    #
    #     :param event:
    #     :return:
    #     """
    #     super().mouseMoveEvent(event)
    #     # update selected node and its edge
    #     if self.isSelected():
    #         for gr_edge in self.scene().edges:
    #             gr_edge.edge_wrap.update_positions()

if __name__ == '__main__':
    import sys
    # 每个PyQt程序必须创建一个application对象，sys.argv 参数是命令行中的一组参数
    # 注意：application在 PyQt5.QtWidgets 模块中
    # 注意：application在 PyQt4.QtGui 模块中
    app = QApplication(sys.argv)
    # 创建桌面窗口
    mainWindow = MainWindow()
    # 显示桌面窗口
    mainWindow.show()
    sys.exit(app.exec_())

