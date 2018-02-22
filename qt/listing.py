# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listing.ui'
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

class Ui_ListingDialog(object):
    def setupUi(self, ListingDialog):
        ListingDialog.setObjectName(_fromUtf8("ListingDialog"))
        ListingDialog.resize(546, 628)
        self.verticalLayout_3 = QtGui.QVBoxLayout(ListingDialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(ListingDialog)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_remote = QtGui.QLabel(self.groupBox)
        self.label_remote.setObjectName(_fromUtf8("label_remote"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_remote)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_transport = QtGui.QLabel(self.groupBox)
        self.label_transport.setObjectName(_fromUtf8("label_transport"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.label_transport)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_local = QtGui.QLabel(self.groupBox)
        self.label_local.setObjectName(_fromUtf8("label_local"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.label_local)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(ListingDialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.accountListWidget = QtGui.QListWidget(self.groupBox_2)
        self.accountListWidget.setObjectName(_fromUtf8("accountListWidget"))
        self.verticalLayout.addWidget(self.accountListWidget)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalGroupBox_8 = QtGui.QGroupBox(ListingDialog)
        self.horizontalGroupBox_8.setObjectName(_fromUtf8("horizontalGroupBox_8"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.horizontalGroupBox_8)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.pushButton_reject = QtGui.QPushButton(self.horizontalGroupBox_8)
        self.pushButton_reject.setObjectName(_fromUtf8("pushButton_reject"))
        self.horizontalLayout_8.addWidget(self.pushButton_reject)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.pushButton_approve = QtGui.QPushButton(self.horizontalGroupBox_8)
        self.pushButton_approve.setObjectName(_fromUtf8("pushButton_approve"))
        self.horizontalLayout_8.addWidget(self.pushButton_approve)
        self.verticalLayout_3.addWidget(self.horizontalGroupBox_8)

        self.retranslateUi(ListingDialog)
        QtCore.QMetaObject.connectSlotsByName(ListingDialog)

    def retranslateUi(self, ListingDialog):
        ListingDialog.setWindowTitle(_translate("ListingDialog", "List accounts", None))
        self.groupBox.setTitle(_translate("ListingDialog", "Request Info", None))
        self.label.setText(_translate("ListingDialog", "Remote", None))
        self.label_remote.setText(_translate("ListingDialog", "TextLabel", None))
        self.label_3.setText(_translate("ListingDialog", "Transport", None))
        self.label_transport.setText(_translate("ListingDialog", "TextLabel", None))
        self.label_4.setText(_translate("ListingDialog", "Local endpoint", None))
        self.label_local.setText(_translate("ListingDialog", "TextLabel", None))
        self.groupBox_2.setTitle(_translate("ListingDialog", "Accounts available for listing", None))
        self.pushButton_reject.setText(_translate("ListingDialog", "Reject", None))
        self.pushButton_approve.setText(_translate("ListingDialog", "Approve", None))

