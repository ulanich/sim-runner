from PyQt5 import QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox

from runner.gen import Ui_MainWindow
from pathlib import Path
import os

CONFIG_MODELS = Path('config/models')
CONFIG_INIT_CONDITIONS = Path('config/init_conditions')


class LeoSimRunner(Ui_MainWindow):

    def __init__(self):
        super().__init__()

    def configure_buttons(self):
        self.b_open.clicked.connect(self.open_file)

    def open_file(self):
        dir_name = QFileDialog.getExistingDirectory(self, 'Open file')
        self.l_open.setText(dir_name)
        try:
            for init_cond in os.listdir(dir_name / CONFIG_INIT_CONDITIONS):
                if init_cond != '__init__.py' and init_cond.endswith('.py'):
                    self.comboBox.addItem(init_cond[:-3])
        except FileNotFoundError:
            QMessageBox.about(self, 'Ошибка', 'Некорректный репозиторий stw-sim-scripts')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LeoSimRunner"))
        self.ch_ignore_blind.setText(_translate("MainWindow", "CheckBox"))
        self.l_ignore_blind.setText(_translate("MainWindow", "Ignore blind"))
        self.l_perfect_device.setText(_translate("MainWindow", "Perfect devices"))
        self.run_button.setText(_translate("MainWindow", "RUN"))
        self.ch_perfect_device.setText(_translate("MainWindow", "CheckBox"))
        self.l_init_cond.setText(_translate("MainWindow", "Initial conditions"))
        self.l_duration.setText(_translate("MainWindow", "Durations"))
        self.b_open.setText(_translate("MainWindow", "Open"))