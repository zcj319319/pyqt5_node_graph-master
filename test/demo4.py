#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/04/11 18:00
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : demo4.py
Software: PyCharm
'''
# _*_ coding:utf-8 _*_
# @File  : 拖拽表格.py
# @Time  : 2021-05-10 15:42
# @Author: zizle
import random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QBrush, QColor, QPalette
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QAbstractItemView, QPushButton, QHeaderView, \
    QListWidget, QWidget, QHBoxLayout, QLabel, QFrame


class TableWidget(QTableWidget):

    # class Label(QWidget,QPainter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(800, 400)

        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.viewport().setAcceptDrops(True)
        self.setDragDropOverwriteMode(False)
        self.setDropIndicatorShown(True)

        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setDragDropMode(QAbstractItemView.InternalMove)

        self.drag_data = dict()  # 记录被拖拽出行的数据
        self.drag_row = -2  # 记录被拖拽的行
        self.drop_row = -2  # 记录被放下的行
        self.is_dragging = False

    def mouseReleaseEvent(self, event) -> None:
        print('songkai')
        if self.is_leave:
            self.is_dragging = False

    def dragEnterEvent(self, event) -> None:  # 开始拖动
        if self.is_dragging:
            return
        row, col = self.indexAt(event.pos()).row(), self.indexAt(event.pos()).column()
        drag_item = self.item(row, 0)
        if col != 0 or not drag_item:
            return
        self.drag_data = drag_item.data(Qt.UserRole)
        if not self.drag_data:
            return
        # 记录拖动行
        self.drag_row = row
        super(TableWidget, self).dragEnterEvent(event)  # 拖动
        self.is_dragging = True
        self.removeRow(self.drag_row)  # 删除行

    def dragMoveEvent(self, event) -> None:  # 在控件内部拖动
        row, col = self.indexAt(event.pos()).row(), self.indexAt(event.pos()).column()
        print('目标row', row, col)
        if row < 0 or col < 0:  # 移除表格有数据的区域
            # 放回原位置还原状态
            self.reset_old_row()
            return
        super(TableWidget, self).dragMoveEvent(event)
        # 还原上下行颜色
        self.set_row_bg_color(row - 1, QColor(255, 255, 255))
        self.set_row_bg_color(row + 1, QColor(255, 255, 255))
        # 设置当前行高亮
        self.set_row_bg_color(row, QColor(254, 163, 86))
        self.drop_row = row  # 目标行

    def set_row_bg_color(self, row, color):
        if row < 0:
            return
        for col in range(self.columnCount()):
            item = self.item(row, col)
            if item:
                item.setBackground(QBrush(color))

    def dragLeaveEvent(self, event) -> None:
        print('拖出行:', self.drag_row)
        print('目标行:', self.drop_row)
        print(help(event))
        # 放回数据,清空记录数据
        self.reset_old_row()

    def reset_old_row(self):
        self.insert_row_data(self.drag_row, self.drag_data)
        self.set_row_bg_color(self.drop_row + 1, QColor(255, 255, 255))
        self.reset_drag_items()

    def reset_drag_items(self):
        self.drag_data.clear()
        self.drag_row = -2
        self.drop_row = -2
        self.is_dragging = False

    def dropEvent(self, event) -> None:
        if self.drop_row < 0:
            return
        self.insert_row_data(self.drop_row, self.drag_data)
        self.set_row_bg_color(self.drop_row + 1, QColor(255, 255, 255))
        print('拖出行:', self.drag_row)
        print('目标行:', self.drop_row)
        self.selectRow(self.drop_row)
        self.reset_drag_items()

    def get_table_data(self):
        data = []
        s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(2101, 2120):
            data.append({'id': i, 'name': s[i - 2100], 'value': random.randint(1, 200)})
        return data

    def set_data(self):
        self.setColumnCount(4)
        self.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        for row, row_item in enumerate(self.get_table_data()):
            self.insert_row_data(row, row_item)

    def insert_row_data(self, row, row_data):
        if not row_data:
            return
        self.insertRow(row)
        for col, key in enumerate(['id', 'name', 'value', '']):
            if col == 3:
                item = QTableWidgetItem()
                item.setIcon(QIcon('Model.png'))
            else:
                item = QTableWidgetItem(str(row_data[key]))
            if col == 0:
                item.setData(Qt.UserRole, row_data)
            self.setItem(row, col, item)


class DraggableTableWidget(QTableWidget):
    def __init__(self, *args, **kwargs):
        super(DraggableTableWidget, self).__init__(*args, **kwargs)
        self.resize(400, 450)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.data_keys = ['id', 'name', 'value']

        self.drag_row = -1
        self.drop_row = None

        self.drag_widget = None
        self.init_drag_widget()

    def set_drag_data_on_widget(self, row_data):
        drag_layout = QHBoxLayout(self.drag_widget)
        drag_layout.setContentsMargins(10, 0, 0, 0)
        for col, key in enumerate(self.data_keys):
            text_label = QLabel(str(row_data[key]), self.drag_widget)
            text_label.setFixedWidth(self.columnWidth(col))
            text_label.setAlignment(Qt.AlignCenter)
            drag_layout.addWidget(text_label)
            button = QPushButton(self)
            button.setFocusPolicy(Qt.NoFocus)
            button.setFixedWidth(1)
            drag_layout.addWidget(button)
        drag_layout.addStretch()
        self.drag_widget.setLayout(drag_layout)
        setattr(self.drag_widget, 'row_data', row_data)

    def init_drag_widget(self):
        if self.drag_widget is not None and isinstance(self.drag_widget, QWidget):
            self.drag_widget.deleteLater()
            self.drag_widget = None
        self.drag_widget = QWidget(self)
        p = self.drag_widget.palette()
        p.setColor(QPalette.Background, QColor(0, 200, 100))
        self.drag_widget.setPalette(p)
        self.drag_widget.setAutoFillBackground(True)

        self.drag_widget.resize(self.width(), 30)
        self.drag_widget.hide()

    def mouseMoveEvent(self, event) -> None:
        self.drag_widget.move(event.pos())
        self.drag_widget.show()
        row, col = self.indexAt(event.pos()).row(), self.indexAt(event.pos()).column()
        # 设置当前行的背景色
        self.set_row_bg_color(row, QColor(254, 163, 86))
        # 还原上下行的背景色
        self.set_row_bg_color(row + 1, QColor(255, 255, 255))
        self.set_row_bg_color(row - 1, QColor(255, 255, 255))

    def set_row_bg_color(self, row, color):
        if row < 0:
            return
        for col in range(self.columnCount()):
            item = self.item(row, col)
            if item:
                item.setBackground(QBrush(color))

    def mousePressEvent(self, event) -> None:
        row, col = self.indexAt(event.pos()).row(), self.indexAt(event.pos()).column()
        cur_item = self.item(row, col)
        if col == 0 and cur_item:
            drag_row_data = cur_item.data(Qt.UserRole)  # 获取数据
            self.set_drag_data_on_widget(drag_row_data)
            # 记录老数据行号
            self.drag_row = row

        super(DraggableTableWidget, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event) -> None:
        row, col = self.indexAt(event.pos()).row(), self.indexAt(event.pos()).column()

        # 还原当前行背景色
        self.set_row_bg_color(row, QColor(255, 255, 255))
        # 删除原行
        self.removeRow(self.drag_row)
        # 插入目标位置
        row_data = getattr(self.drag_widget, 'row_data', None)
        print(row_data)
        if row_data:
            self.insert_row_data(row, row_data)
            self.selectRow(row)
        self.init_drag_widget()
        super(DraggableTableWidget, self).mouseReleaseEvent(event)

    def get_table_data(self):
        data = []
        s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(2101, 2120):
            data.append({'id': i, 'name': s[i - 2100], 'value': random.randint(1, 200)})
        return data

    def set_data(self):
        self.setColumnCount(4)
        self.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        for row, row_item in enumerate(self.get_table_data()):
            self.insert_row_data(row, row_item)

    def insert_row_data(self, row, row_item):
        self.insertRow(row)
        for col, key in enumerate(self.data_keys + ['']):
            if col == 3:
                item = QTableWidgetItem()
                item.setIcon(QIcon('media/icons/delete.png'))
            else:
                item = QTableWidgetItem(str(row_item[key]))

            if col == 0:
                item.setData(Qt.UserRole, row_item)
            self.setItem(row, col, item)


# QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 高分辨率DPI屏幕自动缩放

app = QApplication([])
t = DraggableTableWidget()
t.get_table_data()

t.set_data()
t.show()
sys.exit(app.exec_())