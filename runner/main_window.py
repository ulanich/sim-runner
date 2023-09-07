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
        self.leosim_path = Path()

    def configure_buttons(self):
        self.b_open.clicked.connect(self.open_file)
        self.run_button.clicked.connect(self.run_simulation)

    def open_file(self):
        self.leosim_path = QFileDialog.getExistingDirectory(self, 'Open file')
        self.l_open.setText(self.leosim_path)
        try:
            for init_cond in os.listdir(self.leosim_path / CONFIG_INIT_CONDITIONS):
                if init_cond != '__init__.py' and init_cond.endswith('.py'):
                    self.cb_init_cond.addItem(init_cond[:-3])
            for init_cond in os.listdir(self.leosim_path / CONFIG_MODELS):
                if init_cond != '__init__.py' and init_cond.endswith('.py'):
                    self.cb_models.addItem(init_cond[:-3])

            self.run_button.setEnabled(True)
            self.ch_ignore_blind.setEnabled(True)
            self.ch_perfect_device.setEnabled(True)
            self.l_duration_2.setEnabled(True)
            self.l_duration_2.setText('100000')
        except FileNotFoundError:
            QMessageBox.about(self, 'Ошибка', 'Некорректный репозиторий stw-sim-scripts')
            self.run_button.setEnabled(False)
            self.ch_ignore_blind.setEnabled(False)
            self.ch_perfect_device.setEnabled(False)
            self.l_duration_2.setEnabled(False)
            self.cb_init_cond.clear()
            self.cb_models.clear()

    def run_simulation(self):
        duration = self.l_duration_2.text()
        initial_conditions = self.cb_init_cond.currentText()
        models = self.cb_models.currentText()
        ignore_blind = '--ignore-blind' if self.ch_ignore_blind.isChecked() else ''
        perfect_devices = self.ch_perfect_device.isChecked()

        full_path = os.path.realpath(__file__)
        os.system(f'start {os.path.dirname(full_path)}/run-sim.cmd '
                  f'{self.leosim_path} {models} {initial_conditions} '
                  f'{duration} {ignore_blind}')
