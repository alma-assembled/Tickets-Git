from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QStyledItemDelegate, QTableView, QVBoxLayout, QWidget

class ColorDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        value = index.data(Qt.DisplayRole)  # Obtener el valor de la celda

        # Cambiar el color de fondo basado en el valor
        if value == "Alto":
            option.backgroundBrush = QColor(Qt.red)
        elif value == "Medio":
            option.backgroundBrush = QColor(Qt.yellow)
        elif value == "Bajo":
            option.backgroundBrush = QColor(Qt.green)

class CustomTableModel(QStandardItemModel):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)

    def data(self, index, role=Qt.DisplayRole):
        value = super().data(index, role)

        # Cambiar el color del texto basado en el valor
        if role == Qt.TextColorRole:
            if value == "Alto":
                return QColor(Qt.white)
            elif value == "Medio":
                return QColor(Qt.black)
            elif value == "Bajo":
                return QColor(Qt.darkGreen)

        return value

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabla con Colores Personalizados")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout(self)

        self.table_view = QTableView()
        layout.addWidget(self.table_view)

        self.model = CustomTableModel(5, 3)
        self.model.setHorizontalHeaderLabels(["Prioridad", "Descripción", "Fecha"])

        data = [
            ["Alto", "Tarea crítica", "2023-11-01"],
            ["Medio", "Tarea importante", "2023-11-15"],
            ["Bajo", "Tarea rutinaria", "2023-11-30"],
            ["Alto", "Otra tarea crítica", "2023-12-05"],
            ["Medio", "Otra tarea importante", "2023-12-20"],
        ]

        for row in range(len(data)):
            for col in range(len(data[0])):
                item = QStandardItem(data[row][col])
                self.model.setItem(row, col, item)

        self.table_view.setModel(self.model)

        # Asignar el delegado personalizado a la primera columna
        delegate = ColorDelegate()
        self.table_view.setItemDelegateForColumn(0, delegate)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
