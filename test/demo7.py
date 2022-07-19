#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/04/12 20:55
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : demo7.py
Software: PyCharm
'''
from PyQt5.QtWidgets import *
import sys


class ModifyTree(QWidget):
    """
    添加、修改、删除树控件中的节点
    啊啊啊！我快疯了，父类继承了一个QMainWindow,怎么就是不显示 QWidget，注意！！！
    """

    def __init__(self):
        super(ModifyTree, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('TreeWidget 例子')
        self.resize(400, 300)

        # 添加按钮
        operatorLayout = QHBoxLayout()
        addBtn = QPushButton('添加节点')
        updateBtn = QPushButton('修改节点')
        deleteBtn = QPushButton('删除节点')

        operatorLayout.addWidget(addBtn)
        operatorLayout.addWidget(updateBtn)
        operatorLayout.addWidget(deleteBtn)

        # 按钮绑定槽
        addBtn.clicked.connect(self.addNode)
        updateBtn.clicked.connect(self.updateNode)
        deleteBtn.clicked.connect(self.deleteNode)

        # 利用上节树事件中的树结构
        self.tree = QTreeWidget()

        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['Key', 'Value'])

        root = QTreeWidgetItem(self.tree)
        root.setText(0, 'root')
        root.setText(1, '0')

        # 添加子节点1
        child1 = QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        child1.setText(1, '1')

        # 添加子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, '2')
        #
        child3 = QTreeWidgetItem(child2)
        child3.setText(0, 'child3')
        child3.setText(1, '3')

        # 打开所有节点
        # self.tree.expandAll()

        self.tree.clicked.connect(self.onTreeClicked)

        mainLayout = QVBoxLayout(self)
        mainLayout.addLayout(operatorLayout)
        mainLayout.addWidget(self.tree)
        self.setLayout(operatorLayout)


    # 添加节点
    def addNode(self):
        print('添加节点')
        item = self.tree.currentItem()
        print(item)
        node = QTreeWidgetItem(item)
        node.setText(0, '新节点')
        node.setText(1, '新值')


    # 修改节点
    def updateNode(self):
        print('修改节点')
        item = self.tree.currentItem()
        item.setText(0, '修改节点')
        item.setText(1, '值已经被修改')


    # 删除节点
    def deleteNode(self):
        print('删除节点')
        root = self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            (item.parent() or root).removeChild(item)


    def onTreeClicked(self, index):
        item = self.tree.currentItem()
        print(index.row())
        print('key=%s,value=%s' % (item.text(0), item.text(1)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ModifyTree()
    print(main.__doc__)
    main.show()
    sys.exit(app.exec_())

