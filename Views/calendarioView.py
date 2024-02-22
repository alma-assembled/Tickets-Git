from PyQt5.QtWidgets import QWidget, QCalendarWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal


class Calendario(QWidget):
    date_selected = pyqtSignal(str)
    def __init__(self):
        super().__init__()

        self.setGeometry(130, 130, 400, 300)
        self.setWindowTitle("Selecciona una fecha")
        self.setWindowIcon(QIcon('python.png'))

        vbox = QVBoxLayout()
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)

        self.button = QPushButton("SELECCCIONAR")
        self.button.clicked.connect(self.close_and_emit_date)

        vbox.addWidget(self.calendar)
        vbox.addWidget(self.button)

        self.setLayout(vbox)

    def close_and_emit_date(self):
        dateselected = self.calendar.selectedDate()
        date_in_string = str(dateselected.toPyDate())
        self.date_selected.emit(date_in_string)
        self.close()