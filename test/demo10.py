#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/04/14 21:12
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : demo10.py
Software: PyCharm
'''
# coding=utf-8
import os.path
import sys
import typing

from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QColor, QBrush, QDrag, QFont
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QMenu, QComboBox, QPushButton, QTreeWidgetItemIterator, \
    QApplication
from PyQt5.QtCore import Qt, QMimeData, QVariant, QPoint


class TreeItemMimeData(QMimeData):
    def __init__(self):
        self._format = []
        self._item: QTreeWidgetItem = None
        super().__init__()

    def set_drag_data(self, fmt: str, item: QTreeWidgetItem):
        self._format.append(fmt)
        self._item = item

    def get_drag_data(self):
        return self._item

    def formats(self):
        return self._format

    def retrieveData(self, mimetype: str, preferredType: 'QVariant.Type'):
        if mimetype == 'ItemMimeData':
            return self._item
        else:
            return QMimeData.retrieveData(mimetype, preferredType)


class CDragTreeWidget(QTreeWidget):
    def __init__(self, parent):
        super(CDragTreeWidget, self).__init__(parent)

        self._cut_item: QTreeWidgetItem = None
        self._vertical_scroll_value = 0

        # 允许内部元素拖动
        self.setDragEnabled(True)

        # 允许接受外部拖进
        self.setAcceptDrops(True)

        self._last_bg_colord_item: QTreeWidgetItem = None
        self._start_drag_pnt: QPoint = None

        self.itemChanged.connect(self._slot_item_changed)
        self.itemDoubleClicked.connect(self._slot_item_double_clicked)

        # 右键菜单
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self._right_click_menu)

        self._add_top_level_item()
        self.setHeaderLabels(['1', '2', '3'])
        self.setColumnWidth(0, 200)
        self._index_cmb = 1
        self._index_btn = 2
        self._cut_item = None

    def startDrag(self, supportedActions: typing.Union[QtCore.Qt.DropActions, QtCore.Qt.DropAction]) -> None:
        item = self.currentItem()

        mime_data: TreeItemMimeData = TreeItemMimeData()
        mime_data.set_drag_data('ItemMimeData', item)

        drag: QDrag = QDrag(self)

        # 定义drag事件，自定义的Mimedata传递到dragEnterEvent, dragMoveEvent, dropEvent
        drag.setMimeData(mime_data)

        # 记录下垂直滚动条的值，如果拖动没有改变滚动条，则用这个值，否则用改变之后的
        self._vertical_scroll_value = self.verticalScrollBar().value()

        if drag.exec(Qt.MoveAction) == Qt.MoveAction:
            # 新的item已经克隆并添加之后，移除拖动之前的item
            self._remove_item(item)

            self._update_custom_control()

            # 垂直滚动条设置新的值
            self.verticalScrollBar().setValue(self._vertical_scroll_value)
            self._clear_bg_color()

    # 拖动开始时Event
    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        # 内部item移动
        if event.source() == self:
            if event.mimeData().hasFormat('ItemMimeData'):
                event.setDropAction(Qt.MoveAction)
                event.accept()
            else:
                event.ignore()

        # 外部item移动进TreeWidget
        else:
            if event.mimeData().hasText():
                event.accept()
            else:
                event.ignore()

    # 拖动时移动鼠标Event
    def dragMoveEvent(self, event: QtGui.QDragMoveEvent) -> None:
        try:
            # 拖动到边界，自动滚动
            y = event.pos().y()
            height = self.height()
            if y <= 20:
                self._vertical_scroll_value = self.verticalScrollBar().value() - 1
                self.verticalScrollBar().setValue(self._vertical_scroll_value)
            elif y >= height - 50:
                self._vertical_scroll_value = self.verticalScrollBar().value() + 1
                self.verticalScrollBar().setValue(self._vertical_scroll_value)

            item: QTreeWidgetItem = self.itemAt(event.pos())
            # 如果拖动目的item为空
            if item is None:
                event.ignore()
                return

            # 如果拖动目的item不允许drop
            des_flags = self.itemAt(event.pos()).flags().__int__()
            if des_flags & Qt.ItemIsDropEnabled == 0:
                event.ignore()
                return

            # 内部拖拽item
            if event.source() == self:
                if event.mimeData().hasFormat('ItemMimeData'):
                    mime_data: TreeItemMimeData = event.mimeData()
                    item = mime_data.get_drag_data()

                    current_item: QTreeWidgetItem = self.itemAt(event.pos())
                    is_ok: bool = True
                    while current_item is not None:
                        if current_item == item:
                            is_ok = False
                            break
                        current_item = current_item.parent()
                    if is_ok:
                        item: QTreeWidgetItem = self.itemAt(event.pos())
                        self._set_item_bg(item)

                        event.setDropAction(Qt.CopyAction)
                        event.accept()
                    else:
                        event.ignore()
                else:
                    event.ignore()

            # 外部拖拽进来
            elif event.mimeData().hasText():
                item: QTreeWidgetItem = self.itemAt(event.pos())
                if item is not None:
                    self._set_item_bg(item)

                    event.setDropAction(Qt.MoveAction)
                    event.accept()
                else:
                    event.ignore()
            else:
                event.ignore()
        except Exception as e:
            print(e)

    # 释放鼠标时Event
    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        try:
            # 内部拖拽item
            if event.source() == self:
                if event.mimeData().hasFormat('ItemMimeData'):
                    mime_data: TreeItemMimeData = event.mimeData()
                    item = mime_data.get_drag_data()
                    new_item = item.clone()
                    current_item: QTreeWidgetItem = self.itemAt(event.pos())

                    if current_item is None:
                        event.ignore()
                    else:
                        current_item.addChild(new_item)
                        current_item.setExpanded(True)
                        event.setDropAction(Qt.MoveAction)
                        event.accept()
                else:
                    event.ignore()

            # 外部拖拽进来
            else:
                multi_file_path = event.mimeData().text()
                file_path_list = multi_file_path.split('\n')

                parent_item: QTreeWidgetItem = self.itemAt(event.pos())
                if parent_item is None:
                    return
                else:
                    for file_path in file_path_list:
                        if file_path == '':
                            continue

                        file_path = file_path.replace('file:///', '', 1)
                        _, file_name = os.path.split(file_path)

                        child = QTreeWidgetItem(parent_item)
                        self._set_testcase_def_param(child, file_name)
                        child.setCheckState(0, Qt.Unchecked)
                        new_flags = Qt.ItemIsEnabled | Qt.ItemIsUserCheckable | \
                                    Qt.ItemIsEditable | Qt.ItemIsDragEnabled | Qt.ItemIsSelectable
                        child.setFlags(new_flags)

                        combobox = self._add_combobox(child)
                        self.setItemWidget(child, self._index_cmb, combobox)
                        self.setItemWidget(child, self._index_btn, self._add_btn(child, combobox))
                        parent_item.setExpanded(True)

        except Exception as e:
            print(e)

    def _clear_bg_color(self):
        # 清除之前的背景色
        if self._last_bg_colord_item is not None:
            col_cnt = self.columnCount()
            for ci in range(col_cnt):
                self._last_bg_colord_item.setBackground(ci, QBrush(QColor(255, 255, 255)))
            self._last_bg_colord_item = None

    def _set_item_bg(self, item: QTreeWidgetItem):
        if item is not None and item != self._last_bg_colord_item:
            self._clear_bg_color()

            col_cnt = self.columnCount()
            for ci in range(col_cnt):
                item.setBackground(ci, QBrush(QColor(130, 130, 225)))
            self._last_bg_colord_item = item

    def _remove_item(self, item: QTreeWidgetItem):
        item_parent = item.parent()
        if item_parent is not None:
            item_parent.removeChild(item)
        else:
            index = self.indexOfTopLevelItem(item)
            self.takeTopLevelItem(index)

    def _slot_item_changed(self, item: QTreeWidgetItem, column: int):
        try:
            count = item.childCount()

            if item.checkState(column) == Qt.Checked:
                for f in range(count):
                    if item.child(f).checkState(0) != Qt.Checked:
                        item.child(f).setCheckState(0, Qt.Checked)

            if item.checkState(column) == Qt.Unchecked:
                for f in range(count):
                    if item.child(f).checkState(0) != Qt.Unchecked:
                        item.child(f).setCheckState(0, Qt.Unchecked)
        except Exception as e:
            print(e)

    def _slot_item_double_clicked(self, item: QTreeWidgetItem, column: int):
        if item.childCount() == 0 and item.parent() is not None:
            self.editItem(item, column)
        elif column == 0:
            self.editItem(item, column)

    def _right_click_menu(self, pos):
        try:
            item: QTreeWidgetItem = self.itemAt(pos)
            self._context_menu = QMenu()

            # 没有选中节点
            if item is None:
                self._action_add_top_level = self._context_menu.addAction(u'Add top level group')
                self._action_add_top_level.triggered.connect(self._action_add_top_level_handler)
            else:
                # 增加子Group
                self._action_add_group = self._context_menu.addAction(u'Add child group')
                self._action_add_group.triggered.connect(self._action_add_group_handler)

                self._context_menu.addSeparator()

                # 删除子节点
                self._action_child_del = self._context_menu.addAction(u'Delete children')
                self._action_child_del.triggered.connect(self._action_del_child_handler)

                # 删除节点包括子节点
                if item.parent() is not None:
                    self._action_del = self._context_menu.addAction(u'Delete item and children')
                    self._action_del.triggered.connect(self._action_del_handler)

                self._context_menu.addSeparator()

                # 剪切item
                self._action_cut = self._context_menu.addAction(u'Cut item')
                self._action_cut.triggered.connect(self._action_cut_handler)

                # 粘贴item
                self._action_paste = self._context_menu.addAction(u'Paste item at here')
                self._action_paste.triggered.connect(self._action_paste_handler)

            self._context_menu.exec_(self.mapToGlobal(pos))
        except Exception as e:
            print(e)

    def _action_add_group_handler(self, checked: bool):
        try:
            item = self.currentItem()
            group_item: QTreeWidgetItem = QTreeWidgetItem()
            group_item.setText(0, 'New group')
            group_item.setFont(0, QFont("Microsoft YaHei UI", 9, QFont.Bold))
            group_item.setForeground(0, QColor(Qt.blue))
            group_item.setCheckState(0, Qt.Unchecked)
            group_item.setFlags(group_item.flags() | Qt.ItemFlag.ItemIsEditable)
            item.addChild(group_item)
            item.setExpanded(True)
        except Exception as e:
            print(e)

    def _action_del_child_handler(self, checked: bool):
        try:
            item = self.currentItem()
            for i in range(0, item.childCount()):
                item.removeChild(item.child(item.childCount() - 1))
        except Exception as e:
            print(e)

    def _action_del_handler(self, checked: bool):
        try:
            self._action_del_child_handler()
            item = self.currentItem()
            if item.parent() is not None:
                item.parent().removeChild(item)
        except Exception as e:
            print(e)

    def _add_top_level_item(self, text='Top Level Group'):
        try:
            group_item = QTreeWidgetItem()
            group_item.setText(0, text)
            group_item.setFont(0, QFont("Microsoft YaHei UI", 9, QFont.Bold))
            group_item.setForeground(0, QColor(Qt.blue))
            group_item.setCheckState(0, Qt.Unchecked)
            group_item.setFlags(group_item.flags() | Qt.ItemFlag.ItemIsEditable)
            self.addTopLevelItem(group_item)
        except Exception as e:
            print(e)

    def _action_add_top_level_handler(self, checked: bool):
        try:
            self._add_top_level_item()
        except Exception as e:
            print(e)

    def _action_cut_handler(self, checked: bool):
        try:
            self._cut_item = self.currentItem()
        except Exception as e:
            print(e)

    def _action_paste_handler(self, checked: bool):
        try:
            if self._cut_item is None:
                return

            cur_item = self.currentItem()

            # 粘贴item为空
            if cur_item is None:
                return

            # 粘贴item不允许drop
            flags = cur_item.flags().__int__()
            if flags & Qt.ItemIsDropEnabled == 0:
                return

            new_item = self._cut_item.clone()
            cur_item.addChild(new_item)
            cur_item.setExpanded(True)
            self._remove_item(self._cut_item)
            self._cut_item = None
            self._update_custom_control()
        except Exception as e:
            print(e)

    def _set_testcase_def_param(self, item: QTreeWidgetItem, text: str):
        item.setText(0, text)

    def _add_combobox(self, item: QTreeWidgetItem):
        combobox = QComboBox()
        combobox.addItems(['item1', 'item2'])
        return combobox

    def _add_btn(self, item: QTreeWidgetItem, cmbbox:QComboBox):
        btn = QPushButton('Btn')
        btn.clicked.connect(lambda: self._btn_clicked(item, cmbbox))
        return btn

    def _btn_clicked(self, item: QTreeWidgetItem, cmbbox: QComboBox):
        print(item.text(0))
        print(cmbbox.currentText())

    def _update_custom_control(self):
        try:
            it = QTreeWidgetItemIterator(self)
            while True:
                it_item = it.value()
                if it_item is None:
                    break

                if it_item.childCount() > 0 or it_item.parent() is None:
                    if self.itemWidget(it_item, self._index_cmb) is not None:
                        self.removeItemWidget(it_item, self._index_cmb)
                        self.removeItemWidget(it_item, self._index_btn)
                else:
                    if self.itemWidget(it_item, self._index_cmb) is None:
                        combobox = self._add_combobox(it_item)
                        self.setItemWidget(it_item, self._index_cmb, combobox)
                        self.setItemWidget(it_item, self._index_btn, self._add_btn(it_item, combobox))
                it = it.__iadd__(1)
        except Exception as e:
            print(e)



if __name__=="__main__":
    app = QApplication(sys.argv)
    tr=QTreeWidget()
    Ctree=CDragTreeWidget(tr)
    Ctree.show()
    sys.exit(app.exec_())