
from PyQt4 import QtGui
from PyQt4.QtCore import QThread, QWaitCondition,QMutex,QObject,SIGNAL,pyqtSignal,Qt
from PyQt4.QtCore import QByteArray,QBuffer,QIODevice
from PyQt4.QtGui import QPicture, QPixmap,QListWidgetItem
import utils
from utils.tasks import *
from qt import tx, mainw, listing

class ListingDialog(QObject, listing.Ui_ListingDialog):

    def __init__(self):
        QObject.__init__(self)
        listing.Ui_ListingDialog.__init__(self)

    def onReject(self):
        self.task.addResponse({
            "approved" : False,
        })
        # Then close the window
        self.window.close()

    def onApprove(self):
        accounts = self.parseFromFields()
        self.task.addResponse({
            'accounts': accounts
            })
        # Then close the window
        self.window.close()


    def setupUi(self, dialog):
        super().setupUi(dialog)
        self.window = dialog
        # Connect edit-checkboxes
        self.pushButton_reject.clicked.connect(self.onReject)
        self.pushButton_approve.clicked.connect(self.onApprove)
        self.window.closeEvent = self.closeEvent



    def parseFromFields(self):
        approvedAddrs = {}
        for i in range(0, self.accountListWidget.count()):
            item = self.accountListWidget.item(i)
            if item.checkState() != Qt.Checked:
                continue
            
            approvedAddrs[str(item.text())] = 1

            print("%s approved"%  item.text())

        print("Approved %s" % ",".join(approvedAddrs))

        req = self.task.getRequest()
        accounts = req['accounts']
        approvedAccounts = []
        for a in accounts:
            addr  = a['address']
            if addr in approvedAddrs:
                approvedAccounts.append(a)

        return approvedAccounts

    def showRequest(self, task):
        req = task.getRequest()
        self.task = task

        self.label_remote.setText(req['meta']['remote'])
        self.label_transport.setText(req['meta']['scheme'])
        self.label_local.setText(req['meta']['local'])

        accounts = req['accounts']
        for a in accounts:
            addr  = a['address']
            typ = a['type']
            url = a['url']
            item = QListWidgetItem(addr)
            item.setCheckState(Qt.Checked)
            item.setData(Qt.StatusTipRole, "{} {}".format(typ, url))
            self.accountListWidget.addItem(item)

        self.window.show()

    def closeEvent(self, event):
        if self.task:
            self.task.addResponse({
                "approved" : False,
            })
        event.accept()

    def displayError(self,text):
        #TODO implement a proper UI thingy here
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Error");
        msgBox.setInformativeText(text);
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok);
        msgBox.setDefaultButton(QtGui.QMessageBox.Ok);
        msgBox.exec_()