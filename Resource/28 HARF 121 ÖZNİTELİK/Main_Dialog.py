# -*- coding: utf-8 -*-
"""
Created on Fri Oct 06 15:52:47 2017

@author: acronis_test
"""

import sys
from PyQt4 import QtGui
from Coding import MainWindow

def main():
    app=QtGui.QApplication(sys.argv)
    
    mainWindow=MainWindow()
    mainWindow.show()
    return app.exec_()
    
    

if __name__=="__main__":
    main()
    
    