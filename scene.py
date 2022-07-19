"""
本脚本是自定义scene类，主要是用来记录当前场景已存在的节点以及连线
主要功能是添加、删除节点以及连线。

"""


import math

from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import QColor, QPen
from PyQt5.QtCore import QLine

class GraphicScene1(QGraphicsScene):
    def __init__(self):
        super(GraphicScene1, self).__init__()



class GraphicScene(QGraphicsScene):
    """
    自定义场景，设置背景颜色，添加网格
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        # settings
        self.grid_size = 20     #网格尺寸
        self.grid_squares = 5   #网格数量

        self._color_background = QColor('#393939')   #背景颜色
        self._color_light = QColor('#2f2f2f')        #线颜色
        self._color_dark = QColor('#292929')

        self._pen_light = QPen(self._color_light)     #设置绘笔
        self._pen_light.setWidth(1)                   #绘笔宽度
        self._pen_dark = QPen(self._color_dark)       #绘笔颜色
        self._pen_dark.setWidth(2)                    #深色宽度

        self.setBackgroundBrush(self._color_background)
        self.setSceneRect(0, 0, 500, 500)

        self.nodes = []           #当前场景中所有节点
        self.edges = []           #当前场景中所有连线

    def add_node(self, node):   
        """
        自定义函数，添加节点到该场景，主要调用addItem函数
        :param node:
        :return:
        """
        self.nodes.append(node)
        self.addItem(node)

    def remove_node(self, node):
        """
        自定义函数，移除节点，主要调用removeItem函数，
        在移除节点的同时，也会移除关联的节点连线
        :param node:
        :return:
        """
        self.nodes.remove(node)
        for edge in self.edges:
            if edge.edge_wrap.start_item is node or edge.edge_wrap.end_item is node:
                self.remove_edge(edge)
        self.removeItem(node)

    def add_edge(self, edge):
        """
        自定义函数，添加连线,调用addItem函数
        :param edge:
        :return:
        """
        self.edges.append(edge)
        self.addItem(edge)

    def remove_edge(self, edge):
        """
        自定义函数，移除连线，调用removeItem函数
        :param edge:
        :return:
        """
        self.edges.remove(edge)
        self.removeItem(edge)

    def drawBackground(self, painter, rect):
        """
        重写父类，自定义背景颜色，同时绘制网格
        :param painter:
        :param rect:
        :return:
        """
        super().drawBackground(painter, rect)

        left = int(math.floor(rect.left()))      #获取scene的最左边 x坐标
        right = int(math.ceil(rect.right()))     #获取scene的最右边边 x坐标
        top = int(math.floor(rect.top()))        #获取scene的最上边 y坐标
        bottom = int(math.ceil(rect.bottom()))   #获取scene的最下边 y坐标

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
            painter.drawLines(*lines_light)  #直接使用drawLines绘制多个线

        painter.setPen(self._pen_dark)
        if lines_dark:
            painter.drawLines(*lines_dark)
