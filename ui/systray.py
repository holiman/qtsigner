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
        self.active = False
        #We need to keep a reference to the app, 
        # to signal when to close down
        self.app = app

    def setupUi(self,w):
        
        # See 
        #https://stackoverflow.com/questions/43657890/pyqt5-qsystemtrayicon-activated-signal-not-working
        menu = QtGui.QMenu("Signer menu")
        #menu.aboutToShow.connect(self.activated)
        w.setContextMenu(menu)
        self.menu = menu
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
        #w.setContextMenu(menu)
        self.window = w
        #self.menu = menu

        #When the user activates the systray
        #self.window.activated.connect(self.activated)

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
        
    def setActive(self,text):
        """ Call this to make the signer prompt the user that there are actions to perfrom"""
        self.active = True
        self.window.setIcon(QtGui.QIcon(":/images/red-eth-48x48.png"))
        self.showMessage("Signing Request", text)
        openAction = self.menu.addAction("Open Signer main window")
        openAction.triggered.connect(self.activated)

    def setPassive(self):
        self.active = False
        self.menu.clear()
        self.window.setIcon(QtGui.QIcon(":/images/blu-eth-48x48.png"))

    def activated(self):

        print("Systray activated")
        if self.active:
            self.setPassive()
            self.receiver.onSystrayActivated()
        #event.ignore()

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
