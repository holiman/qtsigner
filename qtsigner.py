#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

"""

import sys, json
from PyQt4 import QtGui
from PyQt4.QtCore import QThread, QWaitCondition,QMutex,QObject,SIGNAL,pyqtSignal,Qt
from qt import tx, mainw

import utils,re
from tinyrpc.dispatch import public
from utils.tasks import *
from ui.transaction import TransactionDialog
from ui.systray import SystrayUI

class MainwindowHandler(QObject,mainw.Ui_mainwindow):

    logSignal = pyqtSignal(str)
    taskSignal = pyqtSignal(Task)

    def __init__(self, signer_hash):
        QObject.__init__(self)
        mainw.Ui_mainwindow.__init__(self)
        self.shutdowntasks = []
        self.signer_hash = signer_hash

    def setSystrayHandler(self, sysui):
        self.systray = sysui

    def addShutdownTask(self, func):
        self.shutdowntasks.append(func)

    def doShutdown(self):
        for func in self.shutdowntasks:
            func()

    def onOpen(self):
        print("onOpen called in MainwindowHandler")

    def setupUi(self, w):
        super().setupUi(w)
        self.label_sha256.setText(self.signer_hash)
        self.window = w
        self.logSignal.connect(self.showLog)
        self.taskSignal.connect(self.onTask)

        def closeEvent( event):
            r = QtGui.QMessageBox.question( w, "Quit?", "Are you sure you want to quit?", QtGui.QMessageBox.Yes,QtGui.QMessageBox.No )
            if r ==  QtGui.QMessageBox.Yes:
                print("Shutting down")
                try:
                    self.doShutdown()
                except Exception as e:
                    print(e)
                event.accept()

            else:
                event.ignore()
                w.setWindowState(Qt.WindowMinimized)

        w.closeEvent = closeEvent        

    def onTask(self,task):
        # Note: Do not call this method directly
        #
        # No need to use signals here, we arrived here via 
        # a signal, so should already be in the main UI thread

        # Toggle the systray
        self.systray.setActive("Signing request received")
        self.task = task

    def onSystrayActivated(self):
        task = self.task
        if task is not None:
            # Fire up the tx window
            # TODO! Discern different types of tasks, 
            # when implementing the remaining operations
            txwindow =  QtGui.QDialog()
            txui = TransactionDialog()
            txui.setupUi(txwindow)
            txui.showTransaction(task)

        #self.systray.setPassive()

    def showLog(self, text):
        self.plainTextEdit.appendPlainText(text.strip())




from comms.server import StdIOHandler, connectHandler
class ServerThread(QThread, StdIOHandler):
    """ The serverthread listens to RPC-requests"""

    def __init__(self):
        QThread.__init__(self)
        self.cond = QWaitCondition()

    def __del__(self):
        self.wait()

    def run(self):
        self.rpc_server.serve_forever()

    def configure(self,rpcserver, signal):
        self.rpc_server = rpcserver
        self.signal = signal
  
    @public
    def ApproveTx(self,**kwargs):

        task = Task(kwargs)
        self.signal.emit(task)
        return task.waitForResponse()

    @public
    def ShowInfo(self,message = ""):
        sys.stdout.write("OverloadedInfo: {}\n".format( message))
        return

class StdErrThread(QThread):
    """The StdErrThread listens to the stderr for the signer"""

    def __init__(self):
        QThread.__init__(self)
        self.ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]')


    def escape_ansi(self, line):
        return self.ansi_escape.sub('', line)

    def configure(self, pipe, signal):
        """Configure this thread with the pipe to read from, and 
        the signal to emit the results on
        """
        self.pipe = pipe
        self.signal = signal

    def run(self):
        x = self.pipe.readline()
        while x:
            self.signal.emit(self.escape_ansi(x))
            x = self.pipe.readline()   


description= """
This is a GUI for a signer, based on Qt 4. 
"""
import argparse
parser = argparse.ArgumentParser(description=description,formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument('-s','--signer', type=str, required=True,
    help="Signer binary (path)", default="/usr/bin/signer")


def main(args):
    import os
    binary = args.signer
    bindir = os.path.dirname(os.path.realpath(binary))

    cmd = ["{}".format(binary),
        "--4bytedb","{}/4byte.json".format(bindir),
        "--stdio-ui"] 
#        "--stdio-ui-test"]

    
    # Check as much as we can about the binary
    sha_hash = check_hash(binary)

    
    if not check_perms(binary):
        sys.exit(0)

    app = QtGui.QApplication(sys.argv)


    # The serverthread communicates over STDIO with the signer-process
    serverthread = ServerThread()
    stderrthread = StdErrThread()

    mainui = MainwindowHandler(sha_hash)

    # The systray
    systrayWindow = QtGui.QSystemTrayIcon()
    sysui = SystrayUI(mainui, app)
    sysui.setupUi(systrayWindow)
    systrayWindow.show()

    mainui.setSystrayHandler(sysui)

    (rpcserver, p ) = connectHandler(cmd, serverthread)

    # Configure the server thread
    serverthread.configure(rpcserver,mainui.taskSignal )
    # Connect the stderr-reader to the pipe and the right signal
    stderrthread.configure(p.stderr,mainui.logSignal)

    killproc = lambda: p.kill()
    
    mainui.addShutdownTask(killproc)

    mainwindow = QtGui.QMainWindow()
    mainui.setupUi(mainwindow)
    mainwindow.show()


    # Kick off the server
    serverthread.start()
    stderrthread.start()
    # And kick off the app
    sys.exit(app.exec_())

if __name__ == '__main__':
    options = parser.parse_args()
    main(options)

