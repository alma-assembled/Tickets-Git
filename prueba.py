import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit, QPushButton, QWidget

class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat")
        self.setGeometry(100, 100, 400, 300)

        # Layout principal
        layout = QVBoxLayout()

        # Área de texto para mostrar el historial del chat
        self.chat_history = QTextEdit()
        layout.addWidget(self.chat_history)

        # Campo de texto para ingresar mensajes
        self.message_input = QTextEdit()
        layout.addWidget(self.message_input)

        # Botón para enviar mensajes
        send_button = QPushButton("Enviar")
        send_button.clicked.connect(self.send_message)
        layout.addWidget(send_button)

        # Widget principal
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    

    def send_message(self):
        # Obtener el mensaje del campo de texto
        message = self.message_input.toPlainText()

        # Mostrar el mensaje en el historial del chat
        self.chat_history.append("Tú: " + message)

        # Guardar el mensaje en un archivo de texto
        with open("chat_history.txt", "a") as file:
            file.write(BdUsurio.nombres +": " + message + "\n")

        # Limpiar el campo de texto después de enviar el mensaje
        self.message_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec_())
