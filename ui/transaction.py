
from PyQt4 import QtGui
from PyQt4.QtCore import QThread, QWaitCondition,QMutex,QObject,SIGNAL,pyqtSignal,Qt
from PyQt4.QtCore import QByteArray,QBuffer,QIODevice
from PyQt4.QtGui import QPicture, QPixmap
import utils
from utils.tasks import *
from qt import tx, mainw
from utils.blockies import getIconPNG

class TransactionDialog(QObject, tx.Ui_TxDialog):

    transactionSignal = pyqtSignal(Task)

    def __init__(self):
        QObject.__init__(self)
        tx.Ui_TxDialog.__init__(self)

    def recalculate(self, line_edit, combobox, label):
        converters = {'wei':1, 'Kwei':int(1e3),'Mwei':int(1e6),'Gwei':int(1e9),'ether':int(1e18)}
        displayval = "N/A"
        value = str(line_edit.text())
        try:
            value=int(value)
        except Exception as e:
            print("Error: ", e )
            label.setText(str(e))
            return

        denom = str(combobox.currentText())

        if denom not in converters.keys():
            print("Error: Unknown denomination {}".format(denom))
            label.setText("Error")
            return


        mult = converters[denom]
        label.setText(str(mult * value)+" wei")

    def setupUi(self, dialog):
        super().setupUi(dialog)
        self.window = dialog
        # Connect edit-checkboxes
        self.checkBox_editfrom.stateChanged.connect(    lambda x: self.lineEdit_from.setEnabled(bool(x)))
        self.checkBox_editto.stateChanged.connect(      lambda x: self.lineEdit_to.setEnabled(bool(x)))
        self.checkBox_editvalue.stateChanged.connect(   lambda x: self.lineEdit_value.setEnabled(bool(x)) or self.comboBox_value.setEnabled(bool(x)))
        self.checkBox_editgas.stateChanged.connect(     lambda x: self.lineEdit_gas.setEnabled(bool(x)))
        self.checkBox_editgasprice.stateChanged.connect(lambda x: self.lineEdit_gasprice.setEnabled(bool(x)) or self.comboBox_gasprice.setEnabled(bool(x)))
        self.checkBox_editnonce.stateChanged.connect(   lambda x: self.spinBox_nonce.setEnabled(bool(x)))
        self.checkBox_editdata.stateChanged.connect(    lambda x: self.plainTextEdit_data.setEnabled(bool(x)))

        
        recalc_value    = lambda x: self.recalculate(self.lineEdit_value,self.comboBox_value,self.label_value)        
        recalc_gasprice = lambda x: self.recalculate(self.lineEdit_gasprice,self.comboBox_gasprice,self.label_gasprice)        

        self.lineEdit_value.textChanged.connect(recalc_value)
        self.comboBox_value.currentIndexChanged.connect(recalc_value)

        self.lineEdit_gasprice.textChanged.connect(recalc_gasprice)
        self.comboBox_gasprice.currentIndexChanged.connect(recalc_gasprice)

        self.pushButton_reject.clicked.connect(self.onReject)
        self.pushButton_approve.clicked.connect(self.onApprove)

        self.transactionSignal.connect(self.showTransaction)

        self.lineEdit_to.textChanged.connect(self.toChanged)
        self.lineEdit_from.textChanged.connect(self.fromChanged)

    def toChanged(self):
        addr = self.to
        self.updateIdenticon(self.label_toaccount, addr)
        pass

    def fromChanged(self):
        addr = self.fromaccount
        self.updateIdenticon(self.label_fromaccount, addr)

    def updateIdenticon(self, label, seed):

        picdata = getIconPNG(seed.lower())
        qp = QPixmap()
        qp.loadFromData(QByteArray.fromRawData(picdata))
        label.setPixmap(qp)

    def onReject(self):
        self.task.addResponse({
            "approved" : False,
        })
        # Then close the window
        self.window.close()

    def displayError(self,text):
        #TODO implement a proper UI thingy here
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Error");
        msgBox.setInformativeText(text);
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok);
        msgBox.setDefaultButton(QtGui.QMessageBox.Ok);
        msgBox.exec_()

    def onApprove(self):

        # Construct a new transaction_info object from the fields, 
        (new_t, error)  = self.parseTxFromFields()
        if error:
            self.displayError(error)
            return

        # Compare it to the old one
        diffInfo = self.compareObjects(self.originalTx, new_t)
        if len(diffInfo) > 0:
            #Todo, get actual confirmation
            info = ["Key '{}' changed from {} to {}".format(k, o, n) for (k,o,n) in diffInfo]

            msgBox = QtGui.QMessageBox()
            msgBox.setText("Transaction modified");
            msgBox.setInformativeText("The transaction has been modified by the UI. Do you wish to proceed? ")
            msgBox.setDetailedText("\n".join(info))
            msgBox.setStandardButtons(QtGui.QMessageBox.Cancel | QtGui.QMessageBox.Ok);
            msgBox.setDefaultButton(QtGui.QMessageBox.Cancel);
            if msgBox.exec_() == QtGui.QMessageBox.Ok:
                print("Ok clicked")
            else:
                print("Cancel, returning")
                return

        new_t['approved'] = True
        new_t['password'] = str(QtGui.QInputDialog.getText (self.window, 
                "Password", 
                "Enter password for account {}".format(new_t['fromaccount']), 
                mode = QtGui.QLineEdit.Password))

        self.task.addResponse(new_t)
        # Then close the window
        self.window.close()
        
    def compareObjects(self, old,new):
        diffs = []
        if old['fromaccount'] != new['fromaccount']:
            diffs.append(("fromaccount", old['fromaccount'], new['fromaccount']))

        old_t = old['transaction']
        new_t = new['transaction']
        for key in ['to','value','gas','gasPrice','nonce','data']:
            if old_t[key] != new_t[key]:
                diffs.append((key, old_t[key], new_t[key]))

        return diffs

    @property
    def to(self):
        return self.lineEdit_to.text()

    @to.setter
    def to(self, x):
        self.lineEdit_to.setText(x)

    @property
    def fromaccount(self):
        return self.lineEdit_from.text()

    @fromaccount.setter
    def fromaccount(self, x):
        self.lineEdit_from.setText(x)

    @property
    def value(self):
        return self.lineEdit_value.text()

    @value.setter
    def value(self, x):
        if x is None:
            x = "0x00"
        self.lineEdit_value.setText(str(int(x,16)))

    @property
    def gas(self):
        return self.lineEdit_gas.text()

    @gas.setter
    def gas(self, x):
        if x is None:
            x = "0x00"
        self.lineEdit_gas.setText(str(int(x,16)))

    @property
    def gasPrice(self):
        return self.lineEdit_gasprice.text()

    @gasPrice.setter
    def gasPrice(self, x):
        if x is None:
            x = "0x00"
        self.lineEdit_gasprice.setText(str(int(x,16)))

    @property
    def nonce(self):
        return hex(self.spinBox_nonce.value())

    @nonce.setter
    def nonce(self,x):
        if x is None or len(str(x)) == 0:
            x = "0x00"
        self.spinBox_nonce.setValue(int(x,16))

    @property
    def data(self):
        return self.plainTextEdit_data.toPlainText()

    @data.setter
    def data(self,x):
        return self.plainTextEdit_data.setPlainText(x)

    def parseTxFromFields(self):
        """
        returns ( tx, err)
        """
        
        _from, error = validAddressOrEmpty(self.fromaccount,allow_empty=False)
        if error != None:
            return (None, "{} {}".format("from",error))

        tx = {}
        resp = {"fromaccount" : _from, "transaction": tx}

        checks = [
            ("to"   , self.to,     validAddressOrEmpty),
            ("value", self.value,  validInt),
            ("gas"  , self.gas,    validInt),
            ("gasPrice", self.gasPrice, validInt),
            ("data"  , self.data,  validHex),
            ("nonce"  , self.nonce,  lambda x: (x,None))
        ]

        # The tx fields
        for (key, indata ,validator) in checks:
            (value, error) = validator(indata)  
            if error != None:
                return (None, "{} {}".format(key,error))
            tx[key] = value

        # All ok
        return (resp, None)

    def showTransaction(self, task):
        txinfo = task.getRequest()
        # Request info
        self.label_remote.setText(txinfo['meta']['remote'])
        self.label_transport.setText(txinfo['meta']['scheme'])
        self.label_local.setText(txinfo['meta']['local'])

        # Tx info
        self.fromaccount = txinfo['fromaccount']
        self.to = txinfo['transaction']['to']
        self.value =  txinfo['transaction']['value']
        self.gas =  txinfo['transaction']['gas']
        self.gasPrice =  txinfo['transaction']['gasPrice']
        self.nonce = txinfo['transaction']['nonce']
        self.data = txinfo['transaction']['data']

        # Callinfo
        self.textEdit_callinfo.setText(txinfo['call_info'])
        self.originalTx = txinfo
        self.task = task

        self.window.show()
