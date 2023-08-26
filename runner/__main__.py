import sys

from PyQt5 import QtWidgets

from runner.main_window import LeoSimRunner

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LeoSimRunner()
    ui.setupUi(MainWindow)
    ui.configure_buttons()
    MainWindow.show()
    sys.exit(app.exec_())
