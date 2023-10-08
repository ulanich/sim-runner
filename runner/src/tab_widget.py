import os
from dataclasses import dataclass
from pathlib import Path

from PyQt5.QtWidgets import QFileDialog, QMessageBox

from runner.ui import Ui_MainWindow

CONFIG_MODELS = Path('config/models')
CONFIG_INIT_CONDITIONS = Path('config/init_conditions')
CHECK_ORBIT_VIEWER_DIR = 'yarn.lock'


@dataclass
class TabBase:
    ui: Ui_MainWindow


@dataclass
class Leosim(TabBase):
    leosim_path = Path()

    def __post_init__(self):
        self._configure_buttons()

    def _configure_buttons(self):
        self.ui.b_open_sim.clicked.connect(self._open_sim_scripts)
        self.ui.b_start_sim.clicked.connect(self._run_simulation)

    def _open_sim_scripts(self, get_dir):
        self.leosim_path = QFileDialog.getExistingDirectory(
            self.ui.tabWidget,
            'Open file',
        )
        self.ui.l_open_sim.setText(self.leosim_path)
        if self.leosim_path == '':
            return None
        try:
            for init_cond in os.listdir(self.leosim_path / CONFIG_INIT_CONDITIONS):
                if init_cond != '__init__.py' and init_cond.endswith('.py'):
                    self.ui.cb_init_cond.addItem(init_cond[:-3])
            for init_cond in os.listdir(self.leosim_path / CONFIG_MODELS):
                if init_cond != '__init__.py' and init_cond.endswith('.py'):
                    self.ui.cb_models.addItem(init_cond[:-3])
            self._enable_all_sim()
        except FileNotFoundError:
            QMessageBox.about(
                self.ui.tabWidget,
                'Ошибка',
                'Некорректный репозиторий stw-sim-scripts',
            )
            self._disable_all_sim()

    def _run_simulation(self):
        duration = self.ui.l_duration.text()
        initial_conditions = self.ui.cb_init_cond.currentText()
        models = self.ui.cb_models.currentText()
        ignore_blind = (
            '--ignore-blind'
            if self.ui.chb_blind.isChecked()
            else ''
        )
        perfect_devices = (
            '--perfect-devices'
            if self.ui.chb_pref_dev.isChecked()
            else ''
        )
        os.system(f'start {Path(__file__).parents[1]}/cmd/run-sim.cmd '
                  f'{self.leosim_path} {models} {initial_conditions} '
                  f'{duration} {ignore_blind} {perfect_devices}')

    def _enable_all_sim(self):
        self.ui.b_start_sim.setEnabled(True)
        self.ui.cb_init_cond.setEnabled(True)
        self.ui.cb_models.setEnabled(True)
        self.ui.le_durations.setEnabled(True)
        self.ui.le_durations.setText('100000')

    def _disable_all_sim(self):
        self.ui.b_start_sim.setEnabled(False)
        self.ui.chb_blind.setEnabled(False)
        self.ui.chb_pref_dev.setEnabled(False)
        self.ui.le_durations.setEnabled(False)
        self.ui.le_durations.setText('')
        self.ui.cb_init_cond.clear()
        self.ui.cb_models.clear()


@dataclass
class OrbitViewer(TabBase):
    orbit_viewer_path = Path

    def __post_init__(self):
        self._configure_buttons()
        self._set_main_text()

    def _configure_buttons(self):
        self.ui.b_open_viewer.clicked.connect(self._open_orbit_viewer)
        self.ui.b_start_viewer.clicked.connect(self._run_orbit_viewer)

    def _open_orbit_viewer(self):
        self.orbit_viewer_path = QFileDialog.getExistingDirectory(
            self.ui.tabWidget,
            'Open file',
        )
        self.ui.le_open_viewer.setText(self.orbit_viewer_path)
        if self.orbit_viewer_path == '':
            return None
        if CHECK_ORBIT_VIEWER_DIR in os.listdir(self.orbit_viewer_path):
            self.ui.b_start_viewer.setEnabled(True)
        else:
            self.ui.b_start_viewer.setEnabled(False)

    def _run_orbit_viewer(self):
        os.system(f'start '
                  f'{Path(__file__).parents[1]}/cmd/run-orbit-viewer.cmd'
                  f' {self.orbit_viewer_path}')

    def _set_main_text(self):
        path = Path(__file__).parents[1] / 'data/walking_to_the_river.txt'
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.read()
            self.ui.textBrowser.setText(lines)
