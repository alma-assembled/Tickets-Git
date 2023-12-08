from Models.global_variables import BdUsurio
from PyQt5 import  QtWidgets

class CrontrollerTicket:
    def __init__(self, vista, ventana):
        self.vista = vista
        self.ventana = ventana

        #INICIAL
        self.llenarInfoInicial()
        self.modo_solicitante()
        
        #INICIALIZAR MENSAJES
        self.mensaje = QtWidgets.QMessageBox()
        self.mensaje.setIcon(QtWidgets.QMessageBox.Information)
        self.mensaje.setWindowTitle(". . : : Informacion : : . .")

        #EVENTOS
        self.vista.rb_solicitante.clicked.connect(self.evtRadio_button_toggled)
        self.vista.rb_responsable.clicked.connect(self.evtRadio_button_toggled)
        self.vista.btn_addTicket.clicked.connect(self.cambiarPagina(3))
        self.vista.btn_crearTicket.clicked.connect(self.cambiarPagina(3))
        self.vista.btn_ticket.clicked.connect(self.cambiarPagina(2))
        self.vista.btn_myTickets.clicked.connect(self.cambiarPagina(2))

    def llenarInfoInicial(self):
        ''' 
            Descripcion: llenar la informacion inicial apartir que el usuario logeando
        '''
        nombreCompleto = BdUsurio.nombre.split()
        nombres = " ".join([str(nombreCompleto[0]), str(nombreCompleto[1])])
        self.vista.lb_nombre.setText(nombres)
        self.vista.rb_solicitante.setChecked(True)


    #EVENTOS
    def evtRadio_button_toggled(self, state):
        ''' 
            Descripcion:
                Evento disparado al cambiar el  estado del radio button
                Limpiar el campo txt_tiempo despues de cambiar el estado
            Args:
                state:estado del radio button
        '''
        if  self.vista.rb_responsable.isChecked() == True:
            self.modo_responsable()
        elif self.vista.rb_solicitante.isChecked() == True:
            self.modo_solicitante()


    def cambiarPagina(self, index):
        # Cambiar a la página indicada
        self.vista.multiWidget.setCurrentIndex(index)

    def modo_solicitante(self):
        self.vista.btn_dashboard.setVisible(True)
        self.vista.fr_dashboard.setVisible(True)

        self.vista.btn_addTicket.setVisible(True)
        self.vista.fr_addTicket.setVisible(True)

        self.vista.btn_ticket.setVisible(False)
        self.vista.fr_ticket.setVisible(False)

        self.vista.btn_myTickets.setVisible(True)
        self.vista.fr_myTickets.setVisible(True)

    def modo_responsable(self):
        self.vista.btn_dashboard.setVisible(True)
        self.vista.fr_dashboard.setVisible(True)

        self.vista.btn_addTicket.setVisible(False)
        self.vista.fr_addTicket.setVisible(False)

        self.vista.btn_ticket.setVisible(True)
        self.vista.fr_ticket.setVisible(True)

        self.vista.btn_myTickets.setVisible(False)
        self.vista.fr_myTickets.setVisible(False)