class WindowUtils():
    windows = {}
    @staticmethod
    def display(window, ui):
        """ 
        This method displays and stores a window and a form. 
        
        Utility method to display a window containing a certain form. Due to some Qt -peculiarities, both of these
        variables must be kept in memory, otherwise it is gc:ed by Qt. If the window (widget/dialog etc) is gc:ed, 
        the window disappears. If the ui (Form object) is gc:ed, all signals and slots stop working. 
        This utility method keeps them both, and makes sure they are removed properly when the window is closed
        """
        ui.setupUi(window)
        window.show()
        WindowUtils.store(ui, window)
        
    @staticmethod
    def store(window,ui):
        """This method stpres a window and a form
         
        Due to some Qt -peculiarities, both of these
        variables must be kept in memory, otherwise it is gc:ed by Qt. If the window (widget/dialog etc) is gc:ed, 
        the window disappears. If the ui (Form object) is gc:ed, all signals and slots stop working. 
        This utility method keeps them both, and makes sure they are removed properly when the window is closed
        
        Actually, the above is not really true. Not only the form object must be stored, but any receiver of signals. So, 
        if you have connected the click of a button to a handler-class other than the form itself, that object which 
        receives the signals must be stored somewhere. See objectinspectorhandler for example. 
        """

        WindowUtils.windows[window] = ui
        #Reference to window need to be kept, otherwise window disappears
        #Refernce to ui-form need to be kept, otherwise signal/slots stop working
        def newClose(x):
            print("Newclose")
            del WindowUtils.windows[window]
        window.closeEvent = newClose
        
        
#    @staticmethod
#    def alert(text=None, html=None):
#        ui = help.Ui_HelpDialog()
#        window = QtGui.QDialog()
#        WindowUtils.display(window,ui)
#        if text is not None : 
#            print("-> "+text)
#            ui.textBrowser_help.setText(text)
#        elif html is not None:
#            ui.textBrowser_help.setHtml(html)
#        return ui
#   
#    @staticmethod
#    def showHelp(html = None):
#        WindowUtils.alert(html = html)
#    