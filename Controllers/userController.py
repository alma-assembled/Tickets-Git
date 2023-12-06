
from Models.userModel import Usuario 
from PyQt5 import  QtWidgets
import  sys
from Controllers.ticketsController import CrontrollerTicket
from PyQt5.QtCore import Qt, QEvent
from Views.ticketsViews import Ui_TicketWindow

class ControllerUser:
    def __init__(self, modelo, vista , ventana_principal):
        self.modelo = modelo
        self.vista = vista
        self.ventana_principal = ventana_principal
        self.vista.btn_cerrar.clicked.connect(self.cerrar)
        self.vista.btn_logear.clicked.connect(self.logear)
        self.vista.btn_mostrar.clicked.connect(self.mostrar_pass)
        self.vista.txt_password.returnPressed.connect(self.logear)
        self.vista.label_info.hide()

    def logear(self):
        '''metodo para logear usuauarios'''
        usuario = self.vista.txt_user.text()
        password = self.vista.txt_password.text()

        if usuario and password:
            user = Usuario(usuario, password)
            if self.modelo.ConsultaUsuario(user) == True:
                self.mostrar_vista_ticket()
            else : 
                self.vista.label_info.show()

    def mostrar_vista_ticket(self):
        '''mostrar la ventana de crear '''
        self.ventana_principal.close()
        self.Fo = QtWidgets.QMainWindow()
        self.ui = Ui_TicketWindow()
        self.ui.setupUi(self.Fo)
        self.controlador = CrontrollerTicket(self.ui, self.Fo)
        self.Fo.show()
        

    def cerrar(self):
        self.ventana_principal.close()

    def mostrar_pass(self):
        if self.vista.txt_password.echoMode() == QtWidgets.QLineEdit.Password:
            self.vista.txt_password.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.vista.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)

    def eventFilter(self, obj, event):
        if obj is self.btn_logear and event.type() == QEvent.KeyPress:
            key = event.key()
            if key == Qt.Key_Escape:
                self.logear()
            if key == Qt.Key_Enter or key == Qt.Key_Return:
                self.logear()
        
        return super().eventFilter(obj, event)