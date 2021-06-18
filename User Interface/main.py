from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
import sys
import time

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('Robot_ui.ui', self)


class SplashDialog(QDialog):
    def __init__(self):
        super(SplashDialog, self).__init__()
        uic.loadUi('splash_screen.ui', self)

        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # self.timer = QtCore.QTimer()
        # self.timer.timeout.connect(self.displayWindow)
        # # self.timer.timeout
        # self.timer.startTimer(35)
        # self.show()


# timer = QtCore.QTimer()
#
# def displayWindow(self):
#     # global dlg
#     timer.stop()
#     window = MyWindow()
#     window.resize(1280, 720)
#     window.show()

if __name__ == '__main__':
    # timer.timeout.connect(displayWindow)
    # timer.startTimer(35)
    try:
        qss_file = open('Remover.qss').read()
        app = QtWidgets.QApplication(sys.argv)
        app.setStyleSheet(qss_file)
        dlg = SplashDialog()
        # dlg.show()
        # time.sleep(20)
        # timer = QtCore.QTimer()
        # timer.
        # dlg.close()
        window = MyWindow()
        window.resize(1280, 720)
        window.show()
        dlg.show()


    except Exception as e:
        print(e)

    sys.exit(app.exec_())
