#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4.QtCore import QThread, QWaitCondition,QMutex,QObject,SIGNAL
from qt import resources
from utils.windows import WindowUtils

from PyQt4 import QtGui

class SystrayUI(QObject):
    """ The SystrayUI inherits from QObject in order to be able
    to receive signals, and is the class responsible for setting up and 
    handling the actions in the systray icon. 

    """
    def __init__(self,receiver, app):
        QObject.__init__(self)
        self.receiver = receiver
        #We need to keep a reference to the app, 
        # to signal when to close down
        self.app = app

    def setupUi(self,w):
        menu = QtGui.QMenu("Signer menu")
        # Define menu options
        #openAction = menu.addAction("Open Signer main window")
        #msgAction  = menu.addAction("Show message") 
        #reqAction = menu.addAction("Trigger request") 
        #exitAction = menu.addAction("Exit") 


        #openAction.setStatusTip('Open signer window')
        #exitAction.setStatusTip("Quits the signer")

        # Define callbacks
        #openAction.triggered.connect(self.receiver.onOpen)
        #msgAction.triggered.connect(lambda x: self.showMessage("A Title", "Here's the message"))
        #exitAction.triggered.connect(lambda x: self.shutdown())
        #reqAction.triggered.connect(lambda x: self.onRequest("Sign tx"))

        w.setIcon(QtGui.QIcon(":/images/blu-eth-48x48.png"))
        w.setContextMenu(menu)
        self.window = w
        self.menu = menu

    def shutdown(self):
        """This is a signal to close shop. We could 
        try to forcibly close everything, but that may kill windows. 
        Instead, we set quitOnLastWindowClosed, and then open and close a window
        """

        print("systrayui.close()")
        self.window.hide()        
        self.app.setQuitOnLastWindowClosed(True)
        QtGui.QWidget().close()
    
    def showMessage(self,title, message):
        self.window.showMessage(title, message)
        
    def onRequest(self,text):
        """ Call this to make the signer prompt the user that there are actions to perfrom"""
        self.window.setIcon(QtGui.QIcon(":/images/red-eth-48x48.png"))
        self.showMessage("Signing Request", text)


class SystrayReceiver(QObject): 

    def onOpen(self):
        print("onOpen")

def main():
    
    receiver = SystrayReceiver()
   
    app = QtGui.QApplication(sys.argv)
    # The systray widget is not counted as a window
    app.setQuitOnLastWindowClosed(False)
    w2 = QtGui.QSystemTrayIcon()
    sysui = SystrayUI(receiver, app)
    sysui.setupUi(w2)
    w2.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
