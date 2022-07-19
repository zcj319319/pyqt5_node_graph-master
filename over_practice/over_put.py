#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/06/22 11:30
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : over_put.py
Software: PyCharm
'''
from PyQt5 import QtCore
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QDialog
from ui_loading_widget import Ui_LoadingWidget
import math


class LoadingWidget(QDialog, Ui_LoadingWidget):
    def __init__(self):
        super(LoadingWidget, self).__init__()
        self.setupUi(self)
        self.offset = 0
        # 定时器
        self.startTimer(50)
        self.setFixedSize(150, 150)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | Qt.Tool | Qt.WindowCloseButtonHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

    def timerEvent(self, evt):
        self.offset += 1
        if self.offset > 11:
            self.offset = 0
        self.update()

    def paintEvent(self, evt):
        painter = QPainter(self)
        # 动反锯齿
        painter.setRenderHint(QPainter.Antialiasing, True)
        width = self.width()
        height = self.height()
        painter.translate(width >> 1, height >> 1)

        offset_dest = (width - 30) / 2
        painter.setPen(QPen(Qt.NoPen))
        # 计算小圆坐标
        for i in range(3):
            point = QPoint(0, 0)
            painter.setBrush(QColor(50 + i * 50, 20 + i * 90, 40 + i * 5, 80 + i * 80))
            point.setX(offset_dest * math.sin((-self.offset + i) * math.pi / 6))
            point.setY(offset_dest * math.cos((-self.offset + i) * math.pi / 6))
            painter.drawEllipse(point.x() - 10, point.y() - 10, 20, 20)

        for i in range(9):
            point = QPoint(0, 0)
            painter.setBrush(QColor(255, 190 - i * 20, i * 15, 255 - i * 32))
            point.setX(offset_dest * math.sin((-self.offset + i + 3) * math.pi / 6))
            point.setY(offset_dest * math.cos((-self.offset + i + 3) * math.pi / 6))
            painter.drawEllipse(point.x() - 10, point.y() - 10, 20, 20)

