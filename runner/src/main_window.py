import sys
import traceback
from pathlib import Path

from PyQt5.QtWidgets import QApplication, QMainWindow
from tomli import load

from runner.src.tab_widget import Leosim, OrbitViewer
from runner.ui.ui_gen import Ui_MainWindow


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print(tb)
    QApplication.quit()


class MainWindowBaseGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class SimRunner(MainWindowBaseGUI):

    def __init__(self):
        super().__init__()
        self._tab_sim = Leosim(self.ui)
        self._tab_orbit_viewer = OrbitViewer(self.ui)
        self._set_version()

    @classmethod
    def start(cls):
        sys.excepthook = excepthook
        app = QApplication([])
        appl = cls()
        appl.show()
        sys.exit(app.exec_())

    def _set_version(self):
        toml_path = Path(__file__).parents[2] / 'pyproject.toml'
        with open(toml_path, 'rb') as toml:
            data = load(toml)
        self.ui.version.setText(
            f'v{data["tool"]["poetry"]["version"]}'
        )
