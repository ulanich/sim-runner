from PyQt5.QtWidgets import QFileDialog

from runner.gen import MainWindow


class LeoSimRunner(MainWindow):

    def config_buttons(self):
        self.b_open.clicked.connect(self.open_file)

    def open_file(self):
        filename = QFileDialog.getExistingDirectory(self, 'Open file')
        self.l_open.setText(filename)