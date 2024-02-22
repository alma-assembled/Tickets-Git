'''import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton

class ChatApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Chat App')
        self.setGeometry(100, 100, 400, 400)

        self.message_display = QTextEdit(self)
        self.message_display.setReadOnly(True)

        self.message_input = QLineEdit(self)
        self.send_button = QPushButton('Send', self)
        self.send_button.clicked.connect(self.send_message)

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.message_display)
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.message_input)
        input_layout.addWidget(self.send_button)
        layout.addLayout(input_layout)

        self.show()

    def send_message(self):
        message = self.message_input.text()
        if message:
            self.message_display.append(f'You: {message}')
            # Aquí puedes agregar lógica para enviar el mensaje a través de una red o cualquier otro medio
            # Por ahora, solo lo mostramos en la ventana

            # Limpia el cuadro de entrada después de enviar el mensaje
            self.message_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_app = ChatApp()
    sys.exit(app.exec_())

    
    
from uuid import uuid4
from nicegui import ui

messages = []

@ui.refreshable
def chat_messages(own_id):
    for user_id, avatar, text in messages:
        ui.chat_message(avatar=avatar, text=text, sent=user_id==own_id)

@ui.page('/')
def index():
    def send():
        messages.append((user, avatar, text.value))
        chat_messages.refresh()
        text.value = ''

    user = str(uuid4())
    avatar = f'https://robohash.org/{user}?bgset=bg2'
    with ui.column().classes('w-full items-stretch'):
        chat_messages(user)

    with ui.footer().classes('bg-white'):
        with ui.row().classes('w-full items-center'):
            with ui.avatar():
                ui.image(avatar)
            text = ui.input(placeholder='message') \
                .props('rounded outlined').classes('flex-grow') \
                .on('keydown.enter', send)

ui.run()


import re

texto = " un texto      que  es       mas  largo"
palabras = re.sub(r'\s+', ' ', texto).strip().split(' ')

n = len(palabras)

print("Número de palabras:", n)
'''

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyledItemDelegate
from PyQt5.QtGui import QColor

class ColorDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        value = index.data(Qt.DisplayRole)  # Obtener el valor de la celda


        # Cambiar el color de fondo basado en el valor
        if value == "ASIGNADO":
            option.backgroundBrush = QColor("#D8863B")
            #option. =  painter.setPen(QColor(Qt.white))
        elif value == "PROCESO":
            option.backgroundBrush = QColor("#063456")
        elif value == "TERMINADO":
            option.backgroundBrush = QColor("#2B8544")
        elif value == "CERRADO":
            option.backgroundBrush = QColor("#3B96D8")
        elif value == "CANCELADO":
            option.backgroundBrush = QColor("#CE2323")

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Ejemplo de Botón en Tabla con ColorDelegate")
        self.setGeometry(100, 100, 600, 400)
        
        # Crear la tabla
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 500, 300)
        
        # Configurar la tabla
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(3)
        
        # Llenar la tabla con datos de ejemplo
        for i in range(3):
            for j in range(4):
                self.tableWidget.setItem(i, j, QTableWidgetItem(f"Item {i},{j}"))
        
        # Agregar un botón a la última columna de cada fila
        for i in range(3):
            button = QPushButton("Botón")
            button.clicked.connect(self.on_button_clicked)
            self.tableWidget.setCellWidget(i, 3, button)
        
        # Asignar el delegado personalizado a la columna de STATUS
        delegate = ColorDelegate()
        self.tableWidget.setItemDelegateForColumn(6, delegate)
        
    def on_button_clicked(self):
        print("¡Botón clickeado!")

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()