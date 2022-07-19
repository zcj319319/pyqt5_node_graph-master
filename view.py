"""
本脚本为主视图类
功能:
    1.添加场景scene
    2.设置UI属性
    3.添加快捷键事件
    4.添加鼠标出发事件

"""
from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import *
from item import GraphicItem
from edge import Edge


class GraphicView(QGraphicsView):

    def __init__(self, graphic_scene, parent=None):
        """
        传入自定义scene作为视图主场景
        :param graphic_scene:
        :param parent:
        """
        super().__init__(parent)

        self.gr_scene = graphic_scene
        self.parent = parent

        self.edge_enable = False
        self.drag_edge = None
        self.init_ui()

    def init_ui(self):
        self.setScene(self.gr_scene)
        self.setRenderHints(QPainter.Antialiasing |  # 开启抗锯齿
                            QPainter.HighQualityAntialiasing |  # 高质量抗锯齿
                            QPainter.TextAntialiasing |  # 文本抗锯齿
                            QPainter.SmoothPixmapTransform)  # |     #平滑像素移动
        # QPainter.LosslessImageRendering)     #渲染低损失  这版本可能没有
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)  # 任何可见部分更新时，全视口更新
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 隐藏水平滑动条
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 隐藏垂直滑动条
        self.setTransformationAnchor(self.AnchorUnderMouse)
        self.setDragMode(self.RubberBandDrag)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_N:
            item = GraphicItem()
            item.setPos(0, 0)
            self.gr_scene.add_node(item)
        if event.key() == Qt.Key_E:
            self.edge_enable = ~self.edge_enable

    def mousePressEvent(self, event):
        item = self.get_item_at_click(event)
        if event.button() == Qt.RightButton:
            if isinstance(item, GraphicItem):
                self.gr_scene.remove_node(item)
        elif self.edge_enable:
            if isinstance(item, GraphicItem):
                self.labItemCord.setText(item.data(1))
                self.edge_drag_start(item)
        else:
            super().mousePressEvent(event)

    def get_item_at_click(self, event):
        """ Return the object that clicked on. """
        pos = event.pos()
        item = self.itemAt(pos)
        return item

    def get_items_at_rubber(self):
        """ Get group select items. """
        area = self.rubberBandRect()
        return self.items(area)

    def mouseMoveEvent(self, event):
        pos = event.pos()
        if self.edge_enable and self.drag_edge is not None:
            sc_pos = self.mapToScene(pos)
            self.drag_edge.gr_edge.set_dst(sc_pos.x(), sc_pos.y())
            self.drag_edge.gr_edge.update()
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.edge_enable:
            self.edge_enable = False
            item = self.get_item_at_click(event)
            if isinstance(item, GraphicItem) and item is not self.drag_start_item:
                self.edge_drag_end(item)
            else:
                self.drag_edge.remove()
                self.drag_edge = None
        else:
            super().mouseReleaseEvent(event)

    def edge_drag_start(self, item):
        """
        开始绘制起始线  生成Edge类
        """
        self.drag_start_item = item
        self.drag_edge = Edge(self.gr_scene, self.drag_start_item, None)

    def edge_drag_end(self, item):
        new_edge = Edge(self.gr_scene, self.drag_start_item, item)
        self.drag_edge.remove()
        self.drag_edge = None
        new_edge.store()
