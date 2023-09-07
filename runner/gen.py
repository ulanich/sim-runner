# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/runsim.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class Ui_MainWindow(QDialog):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(int(368*1.5), int(194*1.5))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.l_open = QtWidgets.QLineEdit(self.centralwidget)
        self.l_open.setObjectName("l_open")
        self.horizontalLayout_2.addWidget(self.l_open)
        self.b_open = QtWidgets.QPushButton(self.centralwidget)
        self.b_open.setObjectName("b_open")
        self.horizontalLayout_2.addWidget(self.b_open)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.ch_ignore_blind = QtWidgets.QCheckBox(self.centralwidget)
        self.ch_ignore_blind.setEnabled(False)
        self.ch_ignore_blind.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ch_ignore_blind.setAutoFillBackground(False)
        self.ch_ignore_blind.setObjectName("ch_ignore_blind")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ch_ignore_blind)
        self.ch_perfect_device = QtWidgets.QCheckBox(self.centralwidget)
        self.ch_perfect_device.setEnabled(False)
        self.ch_perfect_device.setObjectName("ch_perfect_device")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ch_perfect_device)
        self.gridLayout.addLayout(self.formLayout_2, 1, 1, 1, 1)
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setEnabled(False)
        self.run_button.setObjectName("run_button")
        self.gridLayout.addWidget(self.run_button, 2, 0, 1, 2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.formLayout.setObjectName("formLayout")
        self.l_duration = QtWidgets.QLabel(self.centralwidget)
        self.l_duration.setObjectName("l_duration")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.l_duration)
        self.l_duration_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.l_duration_2.setEnabled(False)
        self.l_duration_2.setClearButtonEnabled(False)
        self.l_duration_2.setObjectName("l_duration_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.l_duration_2)
        self.l_init_cond = QtWidgets.QLabel(self.centralwidget)
        self.l_init_cond.setObjectName("l_init_cond")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.l_init_cond)
        self.cb_init_cond = QtWidgets.QComboBox(self.centralwidget)
        self.cb_init_cond.setObjectName("comboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cb_init_cond)
        self.t_models = QtWidgets.QLabel(self.centralwidget)
        self.t_models.setObjectName("t_models")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.t_models)
        self.cb_models = QtWidgets.QComboBox(self.centralwidget)
        self.cb_models.setObjectName("comboBox_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cb_models)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LeoSimRunner"))
        self.b_open.setText(_translate("MainWindow", "Open"))
        self.ch_ignore_blind.setText(_translate("MainWindow", "Ignore blind"))
        self.ch_perfect_device.setText(_translate("MainWindow", "Perfect devices"))
        self.run_button.setText(_translate("MainWindow", "RUN"))
        self.l_duration.setText(_translate("MainWindow", "Durations"))
        self.l_init_cond.setText(_translate("MainWindow", "Init conditions"))
        self.t_models.setText(_translate("MainWindow", "Models"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
