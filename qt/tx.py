# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tx.ui'
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

class Ui_TxDialog(object):
    def setupUi(self, TxDialog):
        TxDialog.setObjectName(_fromUtf8("TxDialog"))
        TxDialog.resize(1467, 975)
        self.verticalLayout = QtGui.QVBoxLayout(TxDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(TxDialog)
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
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(TxDialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_8)
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_11)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit_value = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_value.setEnabled(False)
        self.lineEdit_value.setReadOnly(False)
        self.lineEdit_value.setObjectName(_fromUtf8("lineEdit_value"))
        self.horizontalLayout.addWidget(self.lineEdit_value)
        self.comboBox_value = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_value.setEnabled(False)
        self.comboBox_value.setObjectName(_fromUtf8("comboBox_value"))
        self.comboBox_value.addItem(_fromUtf8(""))
        self.comboBox_value.addItem(_fromUtf8(""))
        self.comboBox_value.addItem(_fromUtf8(""))
        self.comboBox_value.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboBox_value)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.checkBox_editvalue = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_editvalue.setObjectName(_fromUtf8("checkBox_editvalue"))
        self.horizontalLayout.addWidget(self.checkBox_editvalue)
        self.formLayout_2.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lineEdit_gas = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_gas.setEnabled(False)
        self.lineEdit_gas.setReadOnly(False)
        self.lineEdit_gas.setObjectName(_fromUtf8("lineEdit_gas"))
        self.horizontalLayout_5.addWidget(self.lineEdit_gas)
        self.checkBox_editgas = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_editgas.setObjectName(_fromUtf8("checkBox_editgas"))
        self.horizontalLayout_5.addWidget(self.checkBox_editgas)
        self.formLayout_2.setLayout(7, QtGui.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineEdit_from = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_from.setEnabled(False)
        self.lineEdit_from.setInputMask(_fromUtf8(""))
        self.lineEdit_from.setText(_fromUtf8(""))
        self.lineEdit_from.setReadOnly(False)
        self.lineEdit_from.setObjectName(_fromUtf8("lineEdit_from"))
        self.horizontalLayout_3.addWidget(self.lineEdit_from)
        self.checkBox_editfrom = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_editfrom.setObjectName(_fromUtf8("checkBox_editfrom"))
        self.horizontalLayout_3.addWidget(self.checkBox_editfrom)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lineEdit_to = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_to.setEnabled(False)
        self.lineEdit_to.setInputMask(_fromUtf8(""))
        self.lineEdit_to.setReadOnly(False)
        self.lineEdit_to.setObjectName(_fromUtf8("lineEdit_to"))
        self.horizontalLayout_4.addWidget(self.lineEdit_to)
        self.checkBox_editto = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_editto.setObjectName(_fromUtf8("checkBox_editto"))
        self.horizontalLayout_4.addWidget(self.checkBox_editto)
        self.formLayout_2.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_14)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit_gasprice = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_gasprice.setEnabled(False)
        self.lineEdit_gasprice.setReadOnly(False)
        self.lineEdit_gasprice.setObjectName(_fromUtf8("lineEdit_gasprice"))
        self.horizontalLayout_2.addWidget(self.lineEdit_gasprice)
        self.comboBox_gasprice = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_gasprice.setEnabled(False)
        self.comboBox_gasprice.setObjectName(_fromUtf8("comboBox_gasprice"))
        self.comboBox_gasprice.addItem(_fromUtf8(""))
        self.comboBox_gasprice.addItem(_fromUtf8(""))
        self.comboBox_gasprice.addItem(_fromUtf8(""))
        self.comboBox_gasprice.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBox_gasprice)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.checkBox_editgasprice = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_editgasprice.setObjectName(_fromUtf8("checkBox_editgasprice"))
        self.horizontalLayout_2.addWidget(self.checkBox_editgasprice)
        self.formLayout_2.setLayout(8, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.spinBox_nonce = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_nonce.setEnabled(False)
        self.spinBox_nonce.setReadOnly(False)
        self.spinBox_nonce.setMaximum(65535)
        self.spinBox_nonce.setObjectName(_fromUtf8("spinBox_nonce"))
        self.horizontalLayout_6.addWidget(self.spinBox_nonce)
        self.checkBox_editnonce = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_editnonce.setObjectName(_fromUtf8("checkBox_editnonce"))
        self.horizontalLayout_6.addWidget(self.checkBox_editnonce)
        self.formLayout_2.setLayout(10, QtGui.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout_2.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtGui.QLabel(self.groupBox_2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout_2.setWidget(11, QtGui.QFormLayout.LabelRole, self.label_16)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.plainTextEdit_data = QtGui.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_data.setEnabled(False)
        self.plainTextEdit_data.setReadOnly(False)
        self.plainTextEdit_data.setPlainText(_fromUtf8(""))
        self.plainTextEdit_data.setObjectName(_fromUtf8("plainTextEdit_data"))
        self.horizontalLayout_7.addWidget(self.plainTextEdit_data)
        self.checkBox_editdata = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_editdata.setObjectName(_fromUtf8("checkBox_editdata"))
        self.horizontalLayout_7.addWidget(self.checkBox_editdata)
        self.formLayout_2.setLayout(11, QtGui.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.label_gasprice = QtGui.QLabel(self.groupBox_2)
        self.label_gasprice.setObjectName(_fromUtf8("label_gasprice"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.FieldRole, self.label_gasprice)
        self.label_value = QtGui.QLabel(self.groupBox_2)
        self.label_value.setTextFormat(QtCore.Qt.PlainText)
        self.label_value.setObjectName(_fromUtf8("label_value"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.label_value)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(TxDialog)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.textEdit_callinfo = QtGui.QTextEdit(self.groupBox_3)
        self.textEdit_callinfo.setReadOnly(True)
        self.textEdit_callinfo.setObjectName(_fromUtf8("textEdit_callinfo"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.textEdit_callinfo)
        self.verticalLayout_4.addLayout(self.formLayout_3)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.horizontalGroupBox_8 = QtGui.QGroupBox(TxDialog)
        self.horizontalGroupBox_8.setObjectName(_fromUtf8("horizontalGroupBox_8"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.horizontalGroupBox_8)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.pushButton_reject = QtGui.QPushButton(self.horizontalGroupBox_8)
        self.pushButton_reject.setObjectName(_fromUtf8("pushButton_reject"))
        self.horizontalLayout_8.addWidget(self.pushButton_reject)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.pushButton_approve = QtGui.QPushButton(self.horizontalGroupBox_8)
        self.pushButton_approve.setObjectName(_fromUtf8("pushButton_approve"))
        self.horizontalLayout_8.addWidget(self.pushButton_approve)
        self.verticalLayout.addWidget(self.horizontalGroupBox_8)
        self.label_7.setBuddy(self.label_7)
        self.label_8.setBuddy(self.lineEdit_to)
        self.label_11.setBuddy(self.lineEdit_value)
        self.label_13.setBuddy(self.lineEdit_gas)
        self.label_14.setBuddy(self.lineEdit_gasprice)
        self.label_15.setBuddy(self.spinBox_nonce)
        self.label_16.setBuddy(self.plainTextEdit_data)
        self.label_value.setBuddy(self.checkBox_editvalue)

        self.retranslateUi(TxDialog)
        QtCore.QMetaObject.connectSlotsByName(TxDialog)

    def retranslateUi(self, TxDialog):
        TxDialog.setWindowTitle(_translate("TxDialog", "Dialog", None))
        self.groupBox.setTitle(_translate("TxDialog", "Request Info", None))
        self.label.setText(_translate("TxDialog", "Remote", None))
        self.label_remote.setText(_translate("TxDialog", "TextLabel", None))
        self.label_3.setText(_translate("TxDialog", "Transport", None))
        self.label_transport.setText(_translate("TxDialog", "TextLabel", None))
        self.label_4.setText(_translate("TxDialog", "Local endpoint", None))
        self.label_local.setText(_translate("TxDialog", "TextLabel", None))
        self.groupBox_2.setTitle(_translate("TxDialog", "Transaction Info", None))
        self.label_7.setText(_translate("TxDialog", "From", None))
        self.label_8.setText(_translate("TxDialog", "To", None))
        self.label_11.setText(_translate("TxDialog", "Value", None))
        self.comboBox_value.setItemText(0, _translate("TxDialog", "wei", None))
        self.comboBox_value.setItemText(1, _translate("TxDialog", "Mwei", None))
        self.comboBox_value.setItemText(2, _translate("TxDialog", "Gwei", None))
        self.comboBox_value.setItemText(3, _translate("TxDialog", "ether", None))
        self.checkBox_editvalue.setText(_translate("TxDialog", "Edit", None))
        self.checkBox_editgas.setText(_translate("TxDialog", "Edit", None))
        self.checkBox_editfrom.setText(_translate("TxDialog", "Edit", None))
        self.checkBox_editto.setText(_translate("TxDialog", "Edit", None))
        self.label_13.setText(_translate("TxDialog", "Gas", None))
        self.label_14.setText(_translate("TxDialog", "Gasprice", None))
        self.comboBox_gasprice.setItemText(0, _translate("TxDialog", "wei", None))
        self.comboBox_gasprice.setItemText(1, _translate("TxDialog", "Mwei", None))
        self.comboBox_gasprice.setItemText(2, _translate("TxDialog", "Gwei", None))
        self.comboBox_gasprice.setItemText(3, _translate("TxDialog", "ether", None))
        self.checkBox_editgasprice.setText(_translate("TxDialog", "Edit", None))
        self.checkBox_editnonce.setText(_translate("TxDialog", "Edit", None))
        self.label_15.setText(_translate("TxDialog", "Nonce", None))
        self.label_16.setText(_translate("TxDialog", "Data", None))
        self.checkBox_editdata.setText(_translate("TxDialog", "Edit", None))
        self.label_gasprice.setText(_translate("TxDialog", "TextLabel", None))
        self.label_value.setText(_translate("TxDialog", "TextLabel", None))
        self.groupBox_3.setTitle(_translate("TxDialog", "Data info", None))
        self.textEdit_callinfo.setHtml(_translate("TxDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">WARNING</span>: Could not decode data according to ABI</p></body></html>", None))
        self.pushButton_reject.setText(_translate("TxDialog", "Reject", None))
        self.pushButton_approve.setText(_translate("TxDialog", "Approve", None))

