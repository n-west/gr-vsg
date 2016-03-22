# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vsg.ui'
#
# Created: Mon Mar 21 20:01:55 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(710, 520, 83, 24))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.timeDomainFrame = QtGui.QFrame(self.centralwidget)
        self.timeDomainFrame.setGeometry(QtCore.QRect(0, 0, 441, 271))
        self.timeDomainFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.timeDomainFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.timeDomainFrame.setObjectName(_fromUtf8("timeDomainFrame"))
        self.freqDomainFrame = QtGui.QFrame(self.centralwidget)
        self.freqDomainFrame.setGeometry(QtCore.QRect(0, 280, 441, 281))
        self.freqDomainFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.freqDomainFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.freqDomainFrame.setObjectName(_fromUtf8("freqDomainFrame"))
        self.pulseShapeBox = QtGui.QComboBox(self.centralwidget)
        self.pulseShapeBox.setGeometry(QtCore.QRect(460, 130, 161, 20))
        self.pulseShapeBox.setObjectName(_fromUtf8("pulseShapeBox"))
        self.modTypeBox = QtGui.QComboBox(self.centralwidget)
        self.modTypeBox.setGeometry(QtCore.QRect(460, 180, 161, 22))
        self.modTypeBox.setObjectName(_fromUtf8("modTypeBox"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.startButton.setText(_translate("MainWindow", "Start", None))

