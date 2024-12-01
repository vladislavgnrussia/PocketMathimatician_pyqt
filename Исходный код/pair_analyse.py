from PyQt6 import QtCore, QtGui, QtWidgets
from for_pair_analyse import Pair
import sys


class PairAnalyse(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.base_texts()
        self.connecting()
        self.last_pair = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(404, 550)
        self.get_result_btn = QtWidgets.QPushButton(parent=Form)
        self.get_result_btn.setGeometry(QtCore.QRect(140, 60, 141, 23))
        self.get_result_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.get_result_btn.setObjectName("get_result_btn")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 381, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(12, 100, 381, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 129, 391, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lcm_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.lcm_label.setObjectName("lcm_label")
        self.verticalLayout.addWidget(self.lcm_label)
        self.gcd_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.gcd_label.setObjectName("scm_label")
        self.verticalLayout.addWidget(self.gcd_label)
        self.common_dividers_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.common_dividers_label.setObjectName("common_dividers_label")
        self.verticalLayout.addWidget(self.common_dividers_label)
        self.amount_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.amount_label.setObjectName("amount_label")
        self.verticalLayout.addWidget(self.amount_label)
        self.product_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.product_label.setObjectName("product_label")
        self.verticalLayout.addWidget(self.product_label)
        self.divide_label_1 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.divide_label_1.setObjectName("divide_label_1")
        self.verticalLayout.addWidget(self.divide_label_1)
        self.divide_label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.divide_label_2.setObjectName("divide_label_2")
        self.verticalLayout.addWidget(self.divide_label_2)
        self.difference_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.difference_label.setObjectName("difference_label")
        self.verticalLayout.addWidget(self.difference_label)
        self.arithmetic_mean_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.arithmetic_mean_label.setObjectName("arithmetic_mean_label")
        self.verticalLayout.addWidget(self.arithmetic_mean_label)
        self.geometric_mean_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.geometric_mean_label.setObjectName("geometric_mean_label")
        self.verticalLayout.addWidget(self.geometric_mean_label)
        self.harmonic_mean_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.harmonic_mean_label.setObjectName("harmonic_mean_label")
        self.verticalLayout.addWidget(self.harmonic_mean_label)
        self.common_numbers_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.common_numbers_label.setObjectName("common_numbers_label")
        self.verticalLayout.addWidget(self.common_numbers_label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.get_result_btn.setText(_translate("Form", "Рассчитать"))
        self.lcm_label.setText(_translate("Form", "НОК: "))
        self.gcd_label.setText(_translate("Form", "НОД: "))
        self.common_dividers_label.setText(_translate("Form", "Общие делители: "))
        self.amount_label.setText(_translate("Form", "Сумма: "))
        self.product_label.setText(_translate("Form", "Произведение: "))
        self.divide_label_1.setText(_translate("Form", "Частное (1 на 2) : "))
        self.divide_label_2.setText(_translate("Form", "Частное (2 на 1): "))
        self.difference_label.setText(_translate("Form", "Модуль разности: "))
        self.arithmetic_mean_label.setText(_translate("Form", "Среднее арифметическое: "))
        self.geometric_mean_label.setText(_translate("Form", "Среднее геометрическое: "))
        self.harmonic_mean_label.setText(_translate("Form", "Среднее гармоническое: "))
        self.common_numbers_label.setText(_translate("Form", "Общие цифры: "))

    def base_texts(self):
        self.lcm_label_text = self.lcm_label.text()
        self.gcd_label_text = self.gcd_label.text()
        self.common_numbers_label_text = self.common_numbers_label.text()
        self.common_dividers_label_text = self.common_dividers_label.text()
        self.amount_label_text = self.amount_label.text()
        self.product_label_text = self.product_label.text()
        self.divide_label_2_text = self.divide_label_2.text()
        self.divide_label_1_text = self.divide_label_1.text()
        self.arithmetic_mean_label_text = self.arithmetic_mean_label.text()
        self.geometric_mean_label_text = self.geometric_mean_label.text()
        self.harmonic_mean_label_text = self.harmonic_mean_label.text()
        self.difference_label_text = self.difference_label.text()

    def connecting(self):
        self.get_result_btn.clicked.connect(self.write_pair)

    def write_pair(self):
        try:
            self.number1 = int(self.lineEdit.text())
            self.number2 = int(self.lineEdit_2.text())
            self.calculate_result()
        except ValueError:
            button = QtWidgets.QMessageBox.critical(self, 'Ошибка!', 'Одно из введенных чисел не натурально'
                                                                     ' или вообще не является числом!',
                                                    buttons=QtWidgets.QMessageBox.StandardButton.Close,
                                                    defaultButton=QtWidgets.QMessageBox.StandardButton.Close)

    def calculate_result(self):
        try:
            if self.number1 <= 0 or self.number2 <= 0:
                button = QtWidgets.QMessageBox.critical(self, 'Ошибка!', 'Одно из введенных чисел не натурально!',
                                                        buttons=QtWidgets.QMessageBox.StandardButton.Close,
                                                        defaultButton=QtWidgets.QMessageBox.StandardButton.Close)
            else:
                pair = Pair(self.number1, self.number2)
                if pair != self.last_pair:
                    self.last_pair = pair
                    self.lcm_label.setText(self.lcm_label_text + pair.lcm())
                    self.gcd_label.setText(self.gcd_label_text + pair.gcd())
                    self.common_dividers_label.setText(self.common_dividers_label_text + pair.common_dividers())
                    self.amount_label.setText(self.amount_label_text + pair.amount())
                    self.product_label.setText(self.product_label_text + pair.product())
                    self.divide_label_1.setText(self.divide_label_1_text + pair.divide_1())
                    self.divide_label_2.setText(self.divide_label_2_text + pair.divide_2())
                    self.difference_label.setText(self.difference_label_text + pair.difference())
                    self.arithmetic_mean_label.setText(self.arithmetic_mean_label_text + pair.arithmetic_mean())
                    self.geometric_mean_label.setText(self.geometric_mean_label_text + pair.geometric_mean())
                    self.harmonic_mean_label.setText(self.harmonic_mean_label_text + pair.harmonic_mean())
                    self.common_numbers_label.setText(self.common_numbers_label_text + pair.common_numbers())
        except Exception as e:
            pass
