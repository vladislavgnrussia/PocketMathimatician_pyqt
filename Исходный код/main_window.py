import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from calculator import Calculator
from number_characteristic import NumberAnalysis
from pair_analyse import PairAnalyse
from statistico import Statistic


class Main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connecting()
        self.open_modes = False
        self.calculator_btn.hide()
        self.number_analyse_btn.hide()
        self.pair_analyse_btn.hide()
        self.table_analyse_btn.hide()
        self.opened_widget_window = Calculator(self)
        self.opened_widget_window.move(10, 70)
        self.opened_widget_window.show()
        self.setFixedSize(414, 640)

    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(414, 640)
        self.mode_btn = QtWidgets.QPushButton(parent=Main)
        self.mode_btn.setGeometry(QtCore.QRect(10, 10, 40, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.mode_btn.setFont(font)
        self.mode_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.mode_btn.setObjectName("mode_btn")
        font = QtGui.QFont()
        font.setPointSize(8)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Main)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(53, 10, 360, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.mode_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.mode_layout.setContentsMargins(0, 0, 0, 0)
        self.mode_layout.setObjectName("mode_layout")
        self.calculator_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.calculator_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calculator_btn.setObjectName("calculator_btn")
        self.calculator_btn.setFont(font)
        self.mode_layout.addWidget(self.calculator_btn)
        self.number_analyse_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.number_analyse_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.number_analyse_btn.setObjectName("number_analyse_btn")
        self.number_analyse_btn.setFont(font)
        self.mode_layout.addWidget(self.number_analyse_btn)
        self.pair_analyse_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pair_analyse_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pair_analyse_btn.setObjectName("pair_analyse_btn")
        self.pair_analyse_btn.setFont(font)
        self.mode_layout.addWidget(self.pair_analyse_btn)
        self.table_analyse_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.table_analyse_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.table_analyse_btn.setObjectName("table_analyse_btn")
        self.table_analyse_btn.setFont(font)
        self.mode_layout.addWidget(self.table_analyse_btn)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Карманный математик"))
        self.mode_btn.setText(_translate("Main", "≡"))
        self.calculator_btn.setText(_translate("Main", "Калькулятор"))
        self.number_analyse_btn.setText(_translate("Main", "Анализ числа"))
        self.pair_analyse_btn.setText(_translate("Main", "Анализ пары"))
        self.table_analyse_btn.setText(_translate("Main", "Анализ таблицы"))

    def connecting(self):
        self.calculator_btn.clicked.connect(self.open_calculator)
        self.number_analyse_btn.clicked.connect(self.open_number_analyse)
        self.pair_analyse_btn.clicked.connect(self.open_pair_analyse)
        self.table_analyse_btn.clicked.connect(self.open_table_analyse)
        self.mode_btn.clicked.connect(self.hide_show_layout)

    def hide_show_layout(self):
        if self.open_modes:
            self.open_modes = False
            self.calculator_btn.hide()
            self.number_analyse_btn.hide()
            self.pair_analyse_btn.hide()
            self.table_analyse_btn.hide()
        else:
            self.open_modes = True
            self.calculator_btn.show()
            self.number_analyse_btn.show()
            self.pair_analyse_btn.show()
            self.table_analyse_btn.show()

    def open_calculator(self):
        self.open_widget(Calculator(self))

    def open_number_analyse(self):
        self.open_widget(NumberAnalysis(self))

    def open_pair_analyse(self):
        self.open_widget(PairAnalyse(self))

    def open_table_analyse(self):
        self.open_widget(Statistic(self))

    def open_widget(self, widget: QtWidgets.QWidget):
        self.opened_widget_window.deleteLater()
        self.opened_widget_window = widget
        self.opened_widget_window.move(10, 70)
        self.opened_widget_window.show()


if __name__ == '__main__':
    application = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(application.exec())
