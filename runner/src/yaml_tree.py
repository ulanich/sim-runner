from pathlib import Path

import yaml
from PyQt5 import QtCore, QtGui

from runner.ui import Ui_MainWindow


class YamlTree:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui

    def display_yaml(self, yaml_path: Path):
        model = QtGui.QStandardItemModel()
        self.populateTree(
            parse_yaml(yaml_path),
            model.invisibleRootItem(),
        )
        model.setHeaderData(0, QtCore.Qt.Horizontal, 'sim_config.yml')
        self.ui.tree_yaml.setModel(model)
        self.ui.tree_yaml.selectionModel().selectionChanged.connect(lambda: 10)

    def populateTree(self, children, parent):
        for child_key, child_value in children.items():
            child_item = QtGui.QStandardItem(child_key)
            if isinstance(child_value, dict):
                parent.appendRow(child_item)
            else:
                parent.appendRow(QtGui.QStandardItem(f'{child_key} = {child_value}'))
            if isinstance(child_value, dict):
                self.populateTree(child_value, child_item)


def parse_yaml(yaml_path: Path) -> dict:
    with open(yaml_path, 'r') as f:
        return yaml.safe_load(f)
