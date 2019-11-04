# 环境使用 PyQt5-5.4-gpl-Py3.4-Qt5.4.0-x32.exe
# python3.4.3

# ui转py命令:  pyuic5.bat -o qt_test.py qt_test1.ui
# 运行 python main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from qt_test import *


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())