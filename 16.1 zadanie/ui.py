# ui.py - файл интерфейса
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Заголовок
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 350, 50))
        self.label.setStyleSheet("font-size: 24px; font-weight: bold; color: #fb5b5d;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("Конвертер валют")

        #Поле "Из валюты"
        self.input_cur = QtWidgets.QLineEdit(self.centralwidget)
        self.input_cur.setGeometry(QtCore.QRect(50, 90, 350, 40))
        self.input_cur.setStyleSheet("font-size: 14px; padding: 5px; border-radius: 5px;")
        self.input_cur.setPlaceholderText("Из валюты")

        #Поле "Сумма"
        self.input_sum = QtWidgets.QLineEdit(self.centralwidget)
        self.input_sum.setGeometry(QtCore.QRect(50, 140, 350, 40))
        self.input_sum.setStyleSheet("font-size: 14px; padding: 5px; border-radius: 5px;")
        self.input_sum.setPlaceholderText("Сколько")

        #Поле "В валюту"
        self.output_cur = QtWidgets.QLineEdit(self.centralwidget)
        self.output_cur.setGeometry(QtCore.QRect(50, 190, 350, 40))
        self.output_cur.setStyleSheet("font-size: 14px; padding: 5px; border-radius: 5px;")
        self.output_cur.setPlaceholderText("В валюту")

        #Кнопка
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 240, 350, 50))
        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: #fb5b5d;
                border-radius: 10px;
                color: white;
                font-size: 16px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #fa4244;
            }
        """)
        self.pushButton.setText("Конвертировать")

        #Поле результата
        self.output_sum = QtWidgets.QLineEdit(self.centralwidget)
        self.output_sum.setGeometry(QtCore.QRect(50, 300, 350, 40))
        self.output_sum.setStyleSheet("""
            font-size: 16px; 
            font-weight: bold; 
            padding: 5px; 
            border-radius: 5px; 
            background-color: #f0f0f0;
        """)
        self.output_sum.setReadOnly(True)
        self.output_sum.setPlaceholderText("Итог")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Конвертер валют")