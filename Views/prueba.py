from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCalendarWidget, QVBoxLayout, QPushButton, QDialog
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSignal
import sys


class Calendario(QDialog):
    date_selected = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.setGeometry(130, 130, 400, 300)
        self.setWindowTitle("Selecciona una fecha")
        self.setWindowIcon(QIcon('python.png'))

        vbox = QVBoxLayout()
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.selectionChanged.connect(self.calendar_date)

        self.label = QLabel("Hello")
        self.label.setFont(QFont("Sanserif", 15))
        self.label.setStyleSheet('color:green')
        self.button = QPushButton("Seleccionar")
        self.button.clicked.connect(self.close_and_emit_date)

        vbox.addWidget(self.calendar)
        vbox.addWidget(self.label)
        vbox.addWidget(self.button)

        self.setLayout(vbox)

    def calendar_date(self):
        dateselected = self.calendar.selectedDate()
        date_in_string = str(dateselected.toPyDate())

        self.label.setText("Date Is : " + date_in_string)

    def close_and_emit_date(self):
        dateselected = self.calendar.selectedDate()
        date_in_string = str(dateselected.toPyDate())
        self.date_selected.emit(date_in_string)
        self.close()