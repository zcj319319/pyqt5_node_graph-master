#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/06/22 11:36
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : over_demo_01.py
Software: PyCharm
'''
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie


class LoadingGifWin(QWidget):
    def init(self, parent=None):
        super(LoadingGifWin, self).init(parent)
        self.label = QLabel('', self)
        self.setFixedSize(128, 128)
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)
        self.movie = QMovie("./images/waiting.gif")
        self.label.setMovie(self.movie)
        self.movie.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loadingGitWin = LoadingGifWin()
    loadingGitWin.show()
    sys.exit(app.exec_())
