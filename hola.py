import sys
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

'''from uuid import uuid4
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