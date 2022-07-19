#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Time    : 2022/04/11 11:21
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : demo3.py
Software: PyCharm
'''
# 参考网上的一篇文章, 自已写的例子.
# 解决 QGraphicsItemGroup 不能向他的子 item 传递事件的问题,
# 要改的,并不是 group层的代码,而是他子类的函数:sceneEvent
# setfilterschildevents 并不是这个问题的关键,sethandleschildevents 已经 obsolete , 所以都没用.
# 本例中 有一个 proxy widget的按钮, 在此模式下,可以正常工作.

# 有三种方式可以重载 sceneEvent,
# 1. 派生一个子类, 这里就不做测试了.
# 2. 把原类的函数更改掉. 因为 pyqt 是 qt的python 包装, 并不是 built-in , 所以这种方法,可以实行.
# 3. 更改子类的方法.

# 要注意的是, 方法 2 和方法 3 在实行时, 函数的写法不同. 方法3, 实际上,就是 一个装饰器.
# 方法2 在更改时, 对原代码的影响最小, 但可能是给自己挖坑..
# 方法3 要对每一个实例进行更改, 实际上, 操作可能有些困难, 别的一些写好的函数内部调用时,可能无法实行.
# 具体 选哪种方式, 见仁见智吧.


# python 3.8 , pyqt 5.15

from typing import Callable
from PyQt5 import QtWidgets as qw, QtCore as qc, QtGui as qg
import sys
import numpy as np


# 通过改变类的函数,来重载 event
def change_type_event():
    def mouseReleaseEvent(
            self: qw.QGraphicsItem, event: "qw.QGraphicsSceneMouseEvent"
    ) -> None:
        print("mouseReleaseEvent", type(self))
        if not isinstance(self, qw.QGraphicsProxyWidget):
            self.setPen(self._base_pen)
        return self._mouseReleaseEvent(self, event)

    def mousePressEvent(
            self: qw.QGraphicsItem, event: "qw.QGraphicsSceneMouseEvent"
    ) -> None:
        event.accept()
        print("mousePressEvent", type(self))
        if not isinstance(self, qw.QGraphicsProxyWidget):
            self._base_pen = self.pen()
            p = qg.QPen()
            p.setColor(qg.QColor(255, 0, 0))
            p.setWidth(self.pen().width())
            self.setPen(p)
        return self._mousePressEvent(self, event)

    def sceneEvent(self: qw.QGraphicsItem, event: qc.QEvent):
        event.accept()
        # 有可能会漏了一部分事件的触发
        if isinstance(event, qw.QGraphicsSceneMouseEvent):
            if event.type() == 155:
                self.mouseMoveEvent(event)
            elif event.type() == 156:
                self.mousePressEvent(event)
            elif event.type() == 157:
                self.mouseReleaseEvent(event)
            elif event.type() == 158:
                self.mouseDoubleClickEvent(event)
            else:
                print("other ", event.type())
        elif isinstance(event, qw.QGraphicsSceneContextMenuEvent):
            print(type(self), type(event), event.type())
            self.contextMenuEvent(event)
        else:
            self._sceneEvent(self, event)
        return True

    types = [
        qw.QGraphicsLineItem,
        qw.QGraphicsPathItem,
        qw.QGraphicsPolygonItem,
        qw.QGraphicsRectItem,
        qw.QGraphicsProxyWidget,
        qw.QGraphicsEllipseItem,
    ]

    for tp in types:
        assert not hasattr(tp, "_mousePressEvent")
        tp._mousePressEvent = tp.mousePressEvent
        tp.mousePressEvent = mousePressEvent

        assert not hasattr(tp, "_mouseReleaseEvent")
        tp._mouseReleaseEvent = tp.mouseReleaseEvent
        tp.mouseReleaseEvent = mouseReleaseEvent

        assert not hasattr(tp, "_sceneEvent")
        tp._sceneEvent = tp.sceneEvent
        tp.sceneEvent = sceneEvent


def change_event_item(obj: qw.QGraphicsItem):
    def mouseReleaseEvent(event: "qw.QGraphicsSceneMouseEvent") -> None:
        print("mouseReleaseEvent", type(obj))
        if not isinstance(obj, qw.QGraphicsProxyWidget):
            obj.setPen(obj._base_pen)
        return obj._mouseReleaseEvent(event)

    def mousePressEvent(event: "qw.QGraphicsSceneMouseEvent") -> None:
        event.accept()
        print("mousePressEvent", type(obj))
        if not isinstance(obj, qw.QGraphicsProxyWidget):
            obj._base_pen = obj.pen()
            p = qg.QPen()
            p.setColor(qg.QColor(255, 0, 0))
            p.setWidth(obj.pen().width())
            obj.setPen(p)
        return obj._mousePressEvent(event)

    def sceneEvent(event: qc.QEvent):
        event.accept()
        # 有可能会漏了一部分事件的触发
        if isinstance(event, qw.QGraphicsSceneMouseEvent):
            if event.type() == 155:
                obj.mouseMoveEvent(event)
            elif event.type() == 156:
                obj.mousePressEvent(event)
            elif event.type() == 157:
                obj.mouseReleaseEvent(event)
            elif event.type() == 158:
                obj.mouseDoubleClickEvent(event)
            else:
                print("other ", event.type())
        elif isinstance(event, qw.QGraphicsSceneContextMenuEvent):
            print(type(obj), type(event), event.type())
            obj.contextMenuEvent(event)
        else:
            obj._sceneEvent(event)
        return True

    assert not hasattr(obj, "_mousePressEvent")
    obj._mousePressEvent = obj.mousePressEvent
    obj.mousePressEvent = mousePressEvent

    assert not hasattr(obj, "_mouseReleaseEvent")
    obj._mouseReleaseEvent = obj.mouseReleaseEvent
    obj.mouseReleaseEvent = mouseReleaseEvent

    assert not hasattr(obj, "_sceneEvent")
    obj._sceneEvent = obj.sceneEvent
    obj.sceneEvent = sceneEvent

    return obj


if __name__ == "__main__":

    def make_items(obj_wraper: Callable = None):

        flag1 = qw.QGraphicsItem.GraphicsItemFlag.ItemIsMovable
        flag2 = qw.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable

        scene = qw.QGraphicsScene()
        scene.setBackgroundBrush(qg.QColor(qg.QColor().red()))

        pen = qg.QPen()
        pen.setColor(qg.QColor(0, 160, 230))
        pen.setWidth(10)

        m_rectItem = qw.QGraphicsRectItem()
        m_rectItem.setRect(0, 0, 80, 80)
        m_rectItem.setPen(pen)
        m_rectItem.setBrush(qg.QBrush(qg.QColor(255, 0, 255)))
        m_rectItem.setFlag(flag1)
        m_rectItem.setFlag(flag2)

        bt = qw.QPushButton()
        bt_p = qw.QGraphicsProxyWidget()
        bt_p.setWidget(bt)

        def on_bt_click(event):
            print("clicked")

        bt.clicked.connect(on_bt_click)
        m_lineItem = qw.QGraphicsLineItem()
        m_lineItem.setLine(qc.QLineF(0, 0, 100, 100))
        m_lineItem.setPen(pen)
        m_lineItem.setFlag(flag1)
        m_lineItem.setFlag(flag2)

        m_pathItem = qw.QGraphicsPathItem()

        path = qg.QPainterPath()
        path.moveTo(90, 50)
        for i in range(1, 5):
            path.lineTo(
                50 + 40 * np.cos(0.8 * i * np.pi), 50 + 40 * np.sin(0.8 * i * np.pi)
            )

        path.closeSubpath()
        m_pathItem.setPath(path)
        m_pathItem.setPen(pen)
        m_pathItem.setFlag(flag1)
        m_pathItem.setFlag(flag2)

        m_polygonItem = qw.QGraphicsPolygonItem()
        polygon = qg.QPolygonF()
        polygon.append(qc.QPointF(-100.0, -150.0))
        polygon.append(qc.QPointF(-120.0, 150.0))
        polygon.append(qc.QPointF(320.0, 160.0))
        polygon.append(qc.QPointF(220.0, -140.0))

        m_polygonItem.setPolygon(polygon)
        m_polygonItem.setPen(pen)
        m_polygonItem.setFlag(flag1)
        m_polygonItem.setFlag(flag2)

        gp = qw.QGraphicsItemGroup()
        gp.setFlag(flag1)
        gp.setFlag(flag2)

        if obj_wraper:
            m_rectItem = obj_wraper(m_rectItem)
            bt_p = obj_wraper(bt_p)
            m_polygonItem = obj_wraper(m_polygonItem)
            m_lineItem = obj_wraper(m_lineItem)
            m_pathItem = obj_wraper(m_pathItem)

        gp.addToGroup(m_rectItem)
        gp.addToGroup(bt_p)
        scene.addItem(m_polygonItem)
        scene.addItem(m_lineItem)
        scene.addItem(m_pathItem)
        scene.addItem(gp)

        v = qw.QGraphicsView()
        v.setBackgroundBrush(qg.QBrush(qg.QColor(75, 225, 200)))
        v.setScene(scene)
        v.resize(1027, 768)
        return v


    def test1():
        # 直接更改类的函数来重载 event
        app = qw.QApplication(sys.argv)
        change_type_event()  # 重载
        v = make_items()
        v.show()

        r = app.exec_()
        sys.exit(r)


    def test2():
        # 更改实例的函数来重载 event
        app = qw.QApplication(sys.argv)

        v = make_items(change_event_item)
        v.show()

        r = app.exec_()
        sys.exit(r)


    # 两个 test 是两种方式, 只能按一种方式重载
    # test1()
    test2()