from PyQt6 import QtCore, QtGui, QtWidgets
import os
from for_statistico import Table, StatisticalAnalysis, NoSelectedTable


class Statistic(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.connecting()
        self.making_labels_text()
        self.filetype = ''
        self.filename = ''
        self.last_table = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(404, 550)
        self.choice_file_btn = QtWidgets.QPushButton(parent=Form)
        self.choice_file_btn.setGeometry(QtCore.QRect(146, 60, 111, 23))
        self.choice_file_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.choice_file_btn.setObjectName("choice_file_btn")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 199, 411, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.len_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.len_label.setObjectName("len_label")
        self.verticalLayout.addWidget(self.len_label)
        self.sum_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.sum_label.setObjectName("sum_label")
        self.verticalLayout.addWidget(self.sum_label)
        self.median_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.median_label.setObjectName("median_label")
        self.verticalLayout.addWidget(self.median_label)
        self.fashion_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.fashion_label.setObjectName("moda_label")
        self.verticalLayout.addWidget(self.fashion_label)
        self.arithmetic_mean_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.arithmetic_mean_label.setObjectName("arithmetic_mean_label")
        self.verticalLayout.addWidget(self.arithmetic_mean_label)
        self.spread_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.spread_label.setObjectName("spread_label")
        self.verticalLayout.addWidget(self.spread_label)
        self.max_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.max_label.setObjectName("max_label")
        self.verticalLayout.addWidget(self.max_label)
        self.min_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.min_label.setObjectName("min_label")
        self.verticalLayout.addWidget(self.min_label)
        self.dispersion_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.dispersion_label.setObjectName("dispersion_label")
        self.verticalLayout.addWidget(self.dispersion_label)
        self.standard_deviation_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.standard_deviation_label.setObjectName("standart_deviation")
        self.verticalLayout.addWidget(self.standard_deviation_label)
        self.Input = QtWidgets.QLineEdit(parent=Form)
        self.Input.setGeometry(QtCore.QRect(0, 100, 400, 20))
        self.Input.setText("")
        self.Input.setObjectName("Input")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(20, 130, 230, 16))
        self.label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label.setObjectName("label")
        self.get_result_btn = QtWidgets.QPushButton(parent=Form)
        self.get_result_btn.setGeometry(QtCore.QRect(146, 160, 111, 23))
        self.get_result_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.get_result_btn.setObjectName("get_result_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.choice_file_btn.setText(_translate("Form", "Выберете файл"))
        self.len_label.setText(_translate("Form", "  Количество чисел: "))
        self.sum_label.setText(_translate("Form", "  Сумма чисел: "))
        self.median_label.setText(_translate("Form", "  Медиана ряда: "))
        self.fashion_label.setText(_translate("Form", "  Мода ряда(самое частое число): "))
        self.arithmetic_mean_label.setText(_translate("Form", "  Среднее арифметическое: "))
        self.spread_label.setText(_translate("Form", "  Разброс: "))
        self.max_label.setText(_translate("Form", "  Наибольшее значение: "))
        self.min_label.setText(_translate("Form", "  Наименьшее значение: "))
        self.dispersion_label.setText(_translate("Form", "  Дисперсия: "))
        self.standard_deviation_label.setText(_translate("Form", "  Стандартное отклонение: "))
        self.label.setText(_translate("Form", "Введите индексы столбцов"))
        self.get_result_btn.setText(_translate("Form", "Рассчитать"))

    def connecting(self):
        self.choice_file_btn.clicked.connect(self.choice_file)
        self.get_result_btn.clicked.connect(self.get_result)

    def making_labels_text(self):
        self.len_label_text = self.len_label.text()
        self.sum_label_text = self.sum_label.text()
        self.arithmetic_mean_label_text = self.arithmetic_mean_label.text()
        self.median_label_text = self.median_label.text()
        self.fashion_label_text = self.fashion_label.text()
        self.spread_label_text = self.spread_label.text()
        self.max_label_text = self.max_label.text()
        self.min_label_text = self.min_label.text()
        self.dispersion_label_text = self.dispersion_label.text()
        self.standard_deviation_label_text = self.standard_deviation_label.text()

    def choice_file(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор таблицы', '')[0]
        self.filetype = os.path.splitext(self.filename)[1]
        if self.filetype != '' and self.filetype not in ('.xlsx', '.csv', '.sqlite'):
            button = QtWidgets.QMessageBox.critical(self, 'Ошибка!', '''Формат выбранного файла неверен!
Допустимые форматы: .xlsx; .csv; .sqlite.''',
                                                    buttons=QtWidgets.QMessageBox.StandardButton.Close,
                                                    defaultButton=QtWidgets.QMessageBox.StandardButton.Close)

    def get_result(self):
        try:
            columns = self.Input.text().split()
            if self.filetype != '.sqlite':
                columns = list(map(int, columns))
            table = Table(self.filename, *columns, format=self.filetype)
            if table != self.last_table:
                self.last_table = table
                analysis = StatisticalAnalysis(table.get_table())
                self.len_label.setText(self.len_label_text + str(analysis.length()))
                self.sum_label.setText(self.sum_label_text + str(analysis.amount()))
                self.arithmetic_mean_label.setText(self.arithmetic_mean_label_text + str(analysis.arithmetic_mean()))
                self.median_label.setText(self.median_label_text + str(analysis.median()))
                self.fashion_label.setText(self.fashion_label_text + str(analysis.fashion()))
                self.spread_label.setText(self.spread_label_text + str(analysis.spread()))
                self.max_label.setText(self.max_label_text + str(analysis.max()))
                self.min_label.setText(self.min_label_text + str(analysis.min()))
                self.dispersion_label.setText(self.dispersion_label_text + str(analysis.dispersion()))
                self.standard_deviation_label.setText(self.standard_deviation_label_text +
                                                      str(analysis.standard_deviation()))

        except Exception as e:
            if isinstance(e, NoSelectedTable):
                error(self, 'Вы не выбрали файл!')
            elif 'tuple index out of range' in str(e):
                error(self, 'Вы не ввели название таблицы!')

            elif 'no such table:' in str(e) or 'near' in str(e):
                error(self, 'Вы ввели неправильное имя таблицы!')

            elif 'no such column:' in str(e):
                incorrect_name = str(e).split(':')[1][1:]
                error(self, 'Такого столбца нет в таблице: ', incorrect_name)

            elif 'invalid literal for int() with base 10:' in str(e):
                incorrect_name = str(e).split(':')[1][1:]
                error(self, 'Вы ввели не индекс столбца, а слово ', incorrect_name)

            elif 'list index out of range' in str(e):
                error(self, 'Столбца с введенным Вами индексом не существует')

            elif 'division by zero' in str(e):
                error(self, 'Выбранный массив пустой!')

            else:
                print(e)


def error(parent, description, also=''):
    message = QtWidgets.QMessageBox.critical(parent, 'Ошибка!', description + str(also),
                                             buttons=QtWidgets.QMessageBox.StandardButton.Close,
                                             defaultButton=QtWidgets.QMessageBox.StandardButton.Close)
