from PyQt6 import QtCore, QtGui, QtWidgets
from sys import exit, argv
from math import sin, cos, radians, sqrt, pow
from decimal import Decimal
from statistico import error


class Calculator(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.connecting()
        self.str_input = '0'
        self.num_input = 0
        self.delete_all_input = True
        self.is_expo = True
        self.current_operation = ''

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(404, 550)
        Form.setFixedSize(404, 550)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 159, 401, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.multiple_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.multiple_btn.setFont(font)
        self.multiple_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.multiple_btn.setObjectName("multiple_btn")
        self.gridLayout.addWidget(self.multiple_btn, 3, 3, 1, 1)
        self.degree_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.degree_btn.setFont(font)
        self.degree_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.degree_btn.setObjectName("degree_btn")
        self.gridLayout.addWidget(self.degree_btn, 0, 2, 1, 1)
        self.n9_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.n9_btn.setFont(font)
        self.n9_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.n9_btn.setObjectName("n9_btn")
        self.gridLayout.addWidget(self.n9_btn, 3, 2, 1, 1)
        self.clear_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.clear_btn.setFont(font)
        self.clear_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.clear_btn.setObjectName("clear_btn")
        self.gridLayout.addWidget(self.clear_btn, 4, 0, 1, 1)
        self.sin_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.sin_btn.setFont(font)
        self.sin_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.sin_btn.setIconSize(QtCore.QSize(16, 16))
        self.sin_btn.setObjectName("sin_btn")
        self.gridLayout.addWidget(self.sin_btn, 0, 0, 1, 1)
        self.divide_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.divide_btn.setFont(font)
        self.divide_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.divide_btn.setObjectName("divide_btn")
        self.gridLayout.addWidget(self.divide_btn, 4, 3, 1, 1)
        self.clear_entry_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.clear_entry_btn.setFont(font)
        self.clear_entry_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.clear_entry_btn.setObjectName("clear_entry_btn")
        self.gridLayout.addWidget(self.clear_entry_btn, 4, 2, 1, 1)
        self.n0_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.n0_btn.setFont(font)
        self.n0_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.n0_btn.setObjectName("n0_btn")
        self.gridLayout.addWidget(self.n0_btn, 4, 1, 1, 1)
        self.result_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.result_btn.setFont(font)
        self.result_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.result_btn.setObjectName("result_btn")
        self.gridLayout.addWidget(self.result_btn, 5, 1, 1, 2)
        self.n8_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.n8_btn.setFont(font)
        self.n8_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.n8_btn.setObjectName("n8_btn")
        self.gridLayout.addWidget(self.n8_btn, 3, 1, 1, 1)
        self.sqrt_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sqrt_btn.setFont(font)
        self.sqrt_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.sqrt_btn.setObjectName("sqrt_btn")
        self.gridLayout.addWidget(self.sqrt_btn, 0, 3, 1, 1)
        self.n6_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.n6_btn.setFont(font)
        self.n6_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.n6_btn.setObjectName("n6_btn")
        self.gridLayout.addWidget(self.n6_btn, 2, 2, 1, 1)
        self.minus_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.minus_btn.setFont(font)
        self.minus_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.minus_btn.setObjectName("minus_btn")
        self.gridLayout.addWidget(self.minus_btn, 2, 3, 1, 1)
        self.n5_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.n5_btn.setFont(font)
        self.n5_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.n5_btn.setObjectName("n5_btn")
        self.gridLayout.addWidget(self.n5_btn, 2, 1, 1, 1)
        self.n7_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.n7_btn.setFont(font)
        self.n7_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.n7_btn.setObjectName("n7_btn")
        self.gridLayout.addWidget(self.n7_btn, 3, 0, 1, 1)
        self.n1_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.n1_btn.setFont(font)
        self.n1_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.n1_btn.setObjectName("n1_btn")
        self.gridLayout.addWidget(self.n1_btn, 1, 0, 1, 1)
        self.cos_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cos_btn.setFont(font)
        self.cos_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.cos_btn.setObjectName("cos_btn")
        self.gridLayout.addWidget(self.cos_btn, 0, 1, 1, 1)
        self.n2_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.n2_btn.setFont(font)
        self.n2_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.n2_btn.setObjectName("n2_btn")
        self.gridLayout.addWidget(self.n2_btn, 1, 1, 1, 1)
        self.n3_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.n3_btn.setFont(font)
        self.n3_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.n3_btn.setObjectName("n3_btn")
        self.gridLayout.addWidget(self.n3_btn, 1, 2, 1, 1)
        self.n4_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.n4_btn.setFont(font)
        self.n4_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.n4_btn.setObjectName("n4_btn")
        self.gridLayout.addWidget(self.n4_btn, 2, 0, 1, 1)
        self.plus_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plus_btn.setFont(font)
        self.plus_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.plus_btn.setObjectName("plus_btn")
        self.gridLayout.addWidget(self.plus_btn, 1, 3, 1, 1)
        self.point_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.point_btn.setFont(font)
        self.point_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.point_btn.setObjectName("point_btn")
        self.gridLayout.addWidget(self.point_btn, 5, 0, 1, 1)
        self.change_sign_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.change_sign_btn.setFont(font)
        self.change_sign_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.change_sign_btn.setObjectName("change_sign_btn")
        self.gridLayout.addWidget(self.change_sign_btn, 5, 3, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 291, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.second_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.second_label.setFont(font)
        self.second_label.setText("")
        self.second_label.setObjectName("second_label")
        self.verticalLayout.addWidget(self.second_label)
        self.main_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.main_label.setFont(font)
        self.main_label.setObjectName("main_label")
        self.verticalLayout.addWidget(self.main_label)
        self.delete_btn = QtWidgets.QPushButton(parent=Form)
        self.delete_btn.setGeometry(QtCore.QRect(305, 110, 95, 44))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.delete_btn.setFont(font)
        self.delete_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delete_btn.setObjectName("delete_btn")
        self.expo_btn = QtWidgets.QPushButton(parent=Form)
        self.expo_btn.setGeometry(QtCore.QRect(305, 60, 95, 44))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.expo_btn.setFont(font)
        self.expo_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.expo_btn.setObjectName("expo_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.multiple_btn.setText(_translate("Form", "×"))
        self.degree_btn.setText(_translate("Form", "^"))
        self.n9_btn.setText(_translate("Form", "9"))
        self.clear_btn.setText(_translate("Form", "C"))
        self.sin_btn.setText(_translate("Form", "sin"))
        self.divide_btn.setText(_translate("Form", "÷"))
        self.clear_entry_btn.setText(_translate("Form", "СE"))
        self.n0_btn.setText(_translate("Form", "0"))
        self.result_btn.setText(_translate("Form", "="))
        self.n8_btn.setText(_translate("Form", "8"))
        self.sqrt_btn.setText(_translate("Form", "√"))
        self.n6_btn.setText(_translate("Form", "6"))
        self.minus_btn.setText(_translate("Form", "-"))
        self.n5_btn.setText(_translate("Form", "5"))
        self.n7_btn.setText(_translate("Form", "7"))
        self.n1_btn.setText(_translate("Form", "1"))
        self.cos_btn.setText(_translate("Form", "cos"))
        self.n2_btn.setText(_translate("Form", "2"))
        self.n3_btn.setText(_translate("Form", "3"))
        self.n4_btn.setText(_translate("Form", "4"))
        self.plus_btn.setText(_translate("Form", "+"))
        self.point_btn.setText(_translate("Form", "."))
        self.change_sign_btn.setText(_translate("Form", "±"))
        self.main_label.setText(_translate("Form", "0"))
        self.delete_btn.setText(_translate("Form", "⌫"))
        self.expo_btn.setText(_translate("Form", "E"))

    def connecting(self):
        self.n1_btn.clicked.connect(self.add_text)
        self.n2_btn.clicked.connect(self.add_text)
        self.n3_btn.clicked.connect(self.add_text)
        self.n4_btn.clicked.connect(self.add_text)
        self.n5_btn.clicked.connect(self.add_text)
        self.n6_btn.clicked.connect(self.add_text)
        self.n7_btn.clicked.connect(self.add_text)
        self.n8_btn.clicked.connect(self.add_text)
        self.n9_btn.clicked.connect(self.add_text)
        self.n0_btn.clicked.connect(self.add_text)
        self.point_btn.clicked.connect(self.add_text)

        self.plus_btn.clicked.connect(self.action)
        self.minus_btn.clicked.connect(self.action)
        self.multiple_btn.clicked.connect(self.action)
        self.divide_btn.clicked.connect(self.action)
        self.degree_btn.clicked.connect(self.action)

        self.sin_btn.clicked.connect(self.function)
        self.cos_btn.clicked.connect(self.function)

        self.sqrt_btn.clicked.connect(self.sqrt)

        self.clear_btn.clicked.connect(self.clear)
        self.clear_entry_btn.clicked.connect(self.clear)
        self.delete_btn.clicked.connect(self.clear)

        self.result_btn.clicked.connect(self.result)

        self.expo_btn.clicked.connect(self.is_exponential)

        self.change_sign_btn.clicked.connect(self.change_sign_func)

    def is_exponential(self):
        answer, is_ok = QtWidgets.QInputDialog.getItem(self, 'Выбор', 'Применять эксп. запись?', (
            'Да', 'Нет'), 0, False)
        if is_ok and answer == 'Да':
            self.is_expo = True
            self.main_label.setText(f'{Decimal(self.str_input):.2e}')
        elif is_ok:
            self.is_expo = False
            self.main_label.setText(self.str_input)

    def add_text(self):
        send = self.sender()

        if send is not self.point_btn:
            num = send.text()
            num: str

            if self.delete_all_input or self.str_input == '0':
                self.str_input = num
                self.main_label.setText(num)
                self.num_input = int(num)
                self.delete_all_input = False
            else:
                self.str_input += num
                if int(float(self.str_input)) == float(self.str_input):
                    self.num_input = int(float(self.str_input))
                else:
                    self.num_input = float(self.str_input)
                if len(self.str_input) > 18 and self.is_expo:
                    self.main_label.setText(f'{Decimal(self.str_input):.2e}')
                else:
                    self.main_label.setText(self.str_input)

        elif '.' not in self.str_input and self.main_label.text() != 'Ошибка':
            self.str_input += '.'
            if len(self.str_input) > 18 and self.is_expo:
                self.main_label.setText(f'{Decimal(self.str_input):.2e}')
            else:
                self.main_label.setText(self.str_input)
            self.delete_all_input = False

    def function(self):
        if self.main_label.text() != 'Ошибка':
            system, is_ok = QtWidgets.QInputDialog.getItem(self, 'Выбор', 'Выберите единицу измерения угла',
                                                           ('Градусы', 'Радианы'), 1, False)

            send = self.sender()
            if send is self.sin_btn and is_ok:
                if system == 'Градусы':
                    self.num_input = sin(radians(self.num_input))
                else:
                    self.num_input = sin(self.num_input)
                if int(self.num_input) == self.num_input:
                    self.num_input = int(self.num_input)
                self.str_input = str(self.num_input)
                self.main_label.setText(self.str_input)
                self.delete_all_input = True
            elif is_ok:
                if system == 'Градусы':
                    self.num_input = cos(radians(self.num_input))
                else:
                    self.num_input = cos(self.num_input)
                if int(self.num_input) == self.num_input:
                    self.num_input = int(self.num_input)
                self.str_input = str(self.num_input)
                self.str_input = str(self.num_input)
                self.main_label.setText(self.str_input)
                self.delete_all_input = True

    def sqrt(self):
        if self.main_label.text() != 'Ошибка':
            try:
                self.num_input = sqrt(self.num_input)
                if int(self.num_input) == self.num_input:
                    self.num_input = int(self.num_input)
                self.str_input = str(self.num_input)
                self.main_label.setText(self.str_input)
                self.delete_all_input = True
            except ValueError:
                self.main_label.setText('Ошибка')
                self.second_label.setText('')
                self.delete_all_input = True

    def change_sign_func(self):
        if self.main_label.text() != 'Ошибка':
            if self.str_input and self.num_input:
                self.num_input *= -1
                if self.num_input == int(self.num_input):
                    self.num_input = int(self.num_input)
                self.str_input = str(self.num_input)
                self.main_label.setText(self.str_input)

    def action(self):
        if self.main_label.text() != 'Ошибка':
            send = self.sender()
            if send is self.plus_btn:
                sign_of_operation = '+'
            elif send is self.minus_btn:
                sign_of_operation = '-'
            elif send is self.multiple_btn:
                sign_of_operation = '*'
            elif send is self.divide_btn:
                sign_of_operation = '/'
            else:
                sign_of_operation = '**'
            if self.second_label.text() and sign_of_operation == self.current_operation:
                self.result()
            if len(self.str_input) > 18 and self.is_expo:
                self.second_label.setText(f'{Decimal(self.str_input):.2e}' + ' ' + send.text())
            else:
                self.second_label.setText(self.str_input + ' ' + send.text())
            self.delete_all_input = True
            self.current_operation = sign_of_operation
            self.second_label_num = self.num_input

    def clear(self):
        send = self.sender()
        if send is self.clear_btn:
            self.num_input = 0
            self.str_input = '0'
            self.second_label.setText('')
            self.main_label.setText('0')
            self.delete_all_input = True
        elif send is self.clear_entry_btn:
            self.num_input = 0
            self.str_input = '0'
            self.main_label.setText('0')
            self.delete_all_input = True
        else:
            if len(self.str_input) == 1:
                self.str_input = '0'
            else:
                self.str_input = self.str_input[:-1]
            if int(float(self.str_input)) == float(self.str_input):
                self.num_input = int(float(self.str_input))
            else:
                self.num_input = float(self.str_input)
            self.main_label.setText(self.str_input)

    def result(self):
        if self.main_label.text() != 'Ошибка':
            try:

                res = str(self.equally())
                if int(float(res)) == float(res):
                    self.str_input = str(int(float(res)))
                    self.num_input = int(self.str_input)
                else:
                    self.str_input = res
                    self.num_input = float(self.str_input)
                self.second_label.setText('')
                self.delete_all_input = True
                if len(self.str_input) > 18 and self.is_expo:
                    self.main_label.setText(f'{Decimal(self.str_input):.2e}')
                else:
                    self.main_label.setText(self.str_input)
            except ZeroDivisionError:
                self.main_label.setText('Ошибка')
                self.second_label.setText('')
                self.delete_all_input = True
            except ValueError:
                self.main_label.setText('Ошибка')
                self.second_label.setText('')
                self.delete_all_input = True
            except OverflowError:
                error(self, 'Слишком большие числа!')
            except Exception as e:
                print(e)

    def equally(self):
        if self.current_operation == '+':
            return self.second_label_num + self.num_input
        elif self.current_operation == '-':
            return self.second_label_num - self.num_input
        elif self.current_operation == '*':
            return self.second_label_num * self.num_input
        elif self.current_operation == '/':
            return self.second_label_num / self.num_input
        elif self.current_operation == '**':
            return pow(self.second_label_num, self.num_input)
