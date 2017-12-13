# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName(_fromUtf8("mainwindow"))
        mainwindow.resize(848, 271)
        self.centralwidget = QtGui.QWidget(mainwindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_sha256 = QtGui.QLabel(self.centralwidget)
        self.label_sha256.setText(_fromUtf8(""))
        self.label_sha256.setObjectName(_fromUtf8("label_sha256"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_sha256)
        self.verticalLayout.addLayout(self.formLayout)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_signerlogs = QtGui.QWidget()
        self.tab_signerlogs.setObjectName(_fromUtf8("tab_signerlogs"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_signerlogs)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.tab_signerlogs)
        self.plainTextEdit.setUndoRedoEnabled(False)
        self.plainTextEdit.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlainText(_fromUtf8(""))
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        self.tabWidget.addTab(self.tab_signerlogs, _fromUtf8(""))
        self.tab_uilogs = QtGui.QWidget()
        self.tab_uilogs.setObjectName(_fromUtf8("tab_uilogs"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_uilogs)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.plainTextEdit1 = QtGui.QPlainTextEdit(self.tab_uilogs)
        self.plainTextEdit1.setObjectName(_fromUtf8("plainTextEdit1"))
        self.verticalLayout_2.addWidget(self.plainTextEdit1)
        self.tabWidget.addTab(self.tab_uilogs, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        mainwindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainwindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainwindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(mainwindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        mainwindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(mainwindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        mainwindow.setWindowTitle(_translate("mainwindow", "Ethereum QT Signer", None))
        self.label.setText(_translate("mainwindow", "Signer SHA-256", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_signerlogs), _translate("mainwindow", "Signer logs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_uilogs), _translate("mainwindow", "UI logs", None))
        self.toolBar.setWindowTitle(_translate("mainwindow", "toolBar", None))

