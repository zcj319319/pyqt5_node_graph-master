import math

from PyQt5.QtWidgets import QGraphicsPathItem, QGraphicsItem
from PyQt5.QtGui import QColor, QPen, QBrush, QPainterPath
from PyQt5.QtCore import Qt, QPointF


class Edge(object):
    """
    中间计算雷，用来记录连线的输入场景，起始item，结束item坐标
    """
    def __init__(self, scene, start_item, end_item):
        super().__init__()
        self.scene = scene
        self.start_item = start_item
        self.end_item = end_item

        self.gr_edge = GraphicEdge(self)
        # add edge on graphic scene
        self.scene.add_edge(self.gr_edge)

        if self.start_item is not None:
            self.update_positions()

    def store(self):
        """
        场景添加线
        :return:
        """
        self.scene.add_edge(self.gr_edge)

    def update_positions(self):
        """
        更新位置
        :return:
        """
        patch = self.start_item.width / 2  #起始节点的中心宽度
        src_pos = self.start_item.pos()    #起始节点坐标
        self.gr_edge.set_src(src_pos.x()+patch, src_pos.y()+patch)
        if self.end_item is not None:  #当存在结束节点时，就连接到目标节点的中心
            end_pos = self.end_item.pos()
            self.gr_edge.set_dst(end_pos.x()+patch, end_pos.y()+patch)
        else:   #当不存在结束节点时，那么连线跟着平移
            self.gr_edge.set_dst(src_pos.x()+patch, src_pos.y()+patch)
        self.gr_edge.update()

    def remove_from_current_items(self):
        """
        清空当前起始结束节点
        :return:
        """
        self.end_item = None
        self.start_item = None

    def remove(self):
        """
        清空起始、结束item同时删除连线
        :return:
        """
        self.remove_from_current_items()
        self.scene.remove_edge(self.gr_edge)
        self.gr_edge = None



class GraphicEdge(QGraphicsPathItem):
    """
    自定义节点连线item，这里主要使用自定义的笔刷来绘制线。
    然后使用drawPath来绘制路径，只需要保证绘制路径的实时计算，那么就可以让连线实时的跟着节点走
    """
    def __init__(self, edge_wrap, parent=None):
        super().__init__(parent)
        self.edge_wrap = edge_wrap  #edge_wrap是graphic_edge的包装类，对代码逻辑重构出现的
        self.width = 3.0       #默认宽度
        self.pos_src = [0, 0]  #连线起始坐标
        self.pos_dst = [0, 0]  #连线结束坐标

        self._pen = QPen(QColor("#000"))
        self._pen.setWidthF(self.width)

        self._pen_dragging = QPen(QColor("#000"))
        self._pen_dragging.setStyle(Qt.DashDotLine)
        self._pen_dragging.setWidthF(self.width)

        self._mark_pen = QPen(Qt.green)
        self._mark_pen.setWidthF(self.width)
        self._mark_brush = QBrush()
        self._mark_brush.setColor(Qt.green)
        self._mark_brush.setStyle(Qt.SolidPattern)

        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setZValue(-1)  #置于底层 别挡在其它节点上面

    def set_src(self, x, y):   #设置连线起始坐标
        self.pos_src = [x, y]

    def set_dst(self, x, y):   #设置连线结束坐标
        self.pos_dst = [x, y]

    def calc_path(self):   #使用QPainterPath生成路径连线
        path = QPainterPath(QPointF(self.pos_src[0], self.pos_src[1]))
        path.lineTo(self.pos_dst[0], self.pos_dst[1])  #
        return path

    def boundingRect(self):  #矩形区域，以供选择
        return self.shape().boundingRect()

    def shape(self):  #形状
        return self.calc_path()

    def paint(self, painter, graphics_item, widget=None):
        """
        绘制图形
        :param painter:
        :param graphics_item:
        :param widget:
        :return:
        """
        self.setPath(self.calc_path())   #设置路径
        path = self.path()
        if self.edge_wrap.end_item is None:  #如果连接不存在结束节点，那么绘制一个点
            painter.setPen(self._pen_dragging)
            painter.drawPath(path)
        else:   #如果有结束，那么绘制带一个圆形标记的路径
            x1, y1 = self.pos_src
            x2, y2 = self.pos_dst
            radius = 5    # marker radius
            length = 70   # marker length
            k = math.atan2(y2 - y1, x2 - x1)  #通过坐标求斜边长度，即连线长度
            new_x = x2 - length * math.cos(k) - self.width
            new_y = y2 - length * math.sin(k) - self.width

            painter.setPen(self._pen)
            painter.drawPath(path)

            painter.setPen(self._mark_pen)
            painter.setBrush(self._mark_brush)
            painter.drawEllipse(new_x, new_y, radius, radius)  #？绘制椭圆，因为半径斗杓5，所以绘制的是圆
