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
        self.run_button.clicked.connect(self.run_simulation)

    def open_file(self):
        dir_name = QFileDialog.getExistingDirectory(self, 'Open file')
        self.l_open.setText(dir_name)
        try:
            for init_cond in os.listdir(dir_name / CONFIG_INIT_CONDITIONS):
                if init_cond != '__init__.py' and init_cond.endswith('.py'):
                    self.comboBox.addItem(init_cond[:-3])
            for init_cond in os.listdir(dir_name / CONFIG_MODELS):
                if init_cond != '__init__.py' and init_cond.endswith('.py'):
                    self.comboBox_2.addItem(init_cond[:-3])

            self.run_button.setEnabled(True)
            self.ch_ignore_blind.setEnabled(True)
            self.ch_perfect_device.setEnabled(True)
            self.l_duration_2.setEnabled(True)
            self.l_duration_2.setText('100000')
        except FileNotFoundError:
            QMessageBox.about(self, 'Ошибка', 'Некорректный репозиторий stw-sim-scripts')

    def run_simulation(self):
        pass