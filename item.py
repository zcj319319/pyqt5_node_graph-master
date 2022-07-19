from PyQt5.QtWidgets import QGraphicsItem, QGraphicsPixmapItem, QLabel
from PyQt5.QtGui import QPixmap


class GraphicItem(QGraphicsPixmapItem):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.pix = QPixmap("Model.png")
        self.width = 85
        self.height = 85
        self.setPixmap(self.pix)
        self.labIteCord = QLabel()
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setData(1, "hello woprld")

    def mouseMoveEvent(self, event):
        """
        当移动节点时，实时更新整个场景中的所有连线，这里其实需要 关联控制比较好

        :param event:
        :return:
        """
        super().mouseMoveEvent(event)
        # update selected node and its edge
        if self.isSelected():
            for gr_edge in self.scene().edges:
                gr_edge.edge_wrap.update_positions()
