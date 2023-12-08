from Models.global_variables import BdUsurio
from PyQt5 import  QtWidgets
from Controllers.comunController import ControllerComun
class CrontrollerTicket:
    def __init__(self, vista, ventana):
        self.vista = vista
        self.ventana = ventana
        #CONTROLADORES
        self.controllerComon = ControllerComun()  

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
        self.vista.btn_addTicket.clicked.connect(lambda: self.cambiarPagina(3))
        self.vista.btn_dashboard.clicked.connect(lambda: self.cambiarPagina(0))
        self.vista.btn_ticket.clicked.connect(lambda: self.cambiarPagina(2))
        self.vista.btn_myTickets.clicked.connect(lambda: self.cambiarPagina(2))
        

    def llenarInfoInicial(self):
        ''' 
            Descripcion: llenar la informacion inicial apartir que el usuario logeando
        '''
        nombreCompleto = BdUsurio.nombre.split()
        nombres = " ".join([str(nombreCompleto[0]), str(nombreCompleto[1])])
        self.vista.lb_nombre.setText(nombres)
        self.vista.rb_solicitante.setChecked(True)
        self.controllerComon.llenarCbDepartameto(self.vista.cb_departamento)

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
        self.setWidgetsVisibility(True, True, True, True, True, True, False, False,True)

    def modo_responsable(self):
        self.setWidgetsVisibility(True, True, False, False, True, True, False, False, False)

    def setWidgetsVisibility(self, btn_dashboard, fr_dashboard, btn_addTicket, fr_addTicket, btn_ticket, fr_ticket, btn_myTickets, fr_myTickets,registrados):
        self.vista.btn_dashboard.setVisible(btn_dashboard)
        self.vista.fr_dashboard.setVisible(fr_dashboard)
        self.vista.btn_addTicket.setVisible(btn_addTicket)
        self.vista.fr_addTicket.setVisible(fr_addTicket)
        self.vista.btn_ticket.setVisible(btn_ticket)
        self.vista.fr_ticket.setVisible(fr_ticket)
        self.vista.btn_myTickets.setVisible(btn_myTickets)
        self.vista.fr_myTickets.setVisible(fr_myTickets)
        self.vista.registrados.setVisible(registrados)
