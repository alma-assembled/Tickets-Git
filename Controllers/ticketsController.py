from Models.global_variables import BdUsurio
from PyQt5 import  QtWidgets
from PyQt5.QtCore import QDate, QTime
import datetime
from Controllers.comunController import ControllerComun
from Models.ticketsModel import ModelTickets


class CrontrollerTicket:
    def __init__(self, vista, ventana):
        self.vista = vista
        self.ventana = ventana
        #CONTROLADORES
        self.controllerComon = ControllerComun()  

        #MODELOS
        self.modelo_ticket = ModelTickets()

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
        self.vista.btn_gurdar_add.clicked.connect(self.evtGuardarTicket)
        

    def llenarInfoInicial(self):
        ''' 
            Descripcion: llenar la informacion inicial apartir que el usuario logeando
        '''
        self.cambiarPagina(0)
        nombreCompleto = BdUsurio.nombre.split()
        nombres = " ".join([str(nombreCompleto[0]), str(nombreCompleto[1])])
        self.vista.lb_nombre.setText(nombres)
        self.vista.rb_solicitante.setChecked(True)
        self.controllerComon.llenarCbDepartameto(self.vista.cb_departamento_d)
        self.controllerComon.llenarCbDepartameto(self.vista.cb_departamento_t)
        self.controllerComon.llenarCbDepartameto(self.vista.cb_departamento_add)
        self.controllerComon.llenarCbDepartameto(self.vista.cb_departamento_asg)

        self.controllerComon.llenarCbCategorias(self.vista.cb_categoria_d)
        self.controllerComon.llenarCbCategorias(self.vista.cb_categoria_t)
        self.controllerComon.llenarCbCategorias(self.vista.cb_categoria_add)

        self.controllerComon.llenarCbEmpleados(self.vista.cb_empleado_d)
        self.controllerComon.llenarCbEmpleados(self.vista.cb_empleado_t)
        self.controllerComon.llenarCbEmpleados(self.vista.cb_empleado_add)
        self.controllerComon.llenarCbEmpleados(self.vista.cb_empleado_asg)

        self.controllerComon.llenarCbEstado(self.vista.cb_status_d)
        self.controllerComon.llenarCbEstado(self.vista.cb_status_t)
        self.controllerComon.llenarCbPrioridad(self.vista.cb_prioridad_add)



    #EVENTOS
    def evtRadio_button_toggled(self, state):
        ''' 
            Descripcion:
                Evento disparado al cambiar el  estado del radio button
                Limpiar el campo txt_tiempo despues de cambiar el estado
            Args:
                state:estado del radio button
        '''
        self.cambiarPagina(0)
        if  self.vista.rb_responsable.isChecked() == True:
            self.modo_responsable()
        elif self.vista.rb_solicitante.isChecked() == True:
            self.modo_solicitante()

    def evtGuardarTicket(self):
        id_departamento = self.vista.cb_departamento_add.currentData()
        id_categoria = self.vista.cb_categoria_add.currentData()
        prioridad = self.vista.cb_prioridad_add.currentData()
        id_empleado = self.vista.cb_empleado_add.currentData()
        asunto = self.vista.ptext_asunto_add.toPlainText()
        descripcion = self.vista.ptext_descripcion_add.toPlainText()
        folio= "000"
        fecha = self.fecha()
        status = "ASIGNADO"

        print(id_empleado)
        if id_departamento ==  0 or id_categoria == 0 or id_empleado == 0 or prioridad == 0 or asunto == "" or  descripcion == "" :
            self.mensaje.setText( "Debes llenar todos los campos")
            self.mensaje.exec_()
            return
        id_ticket = self.modelo_ticket.guardarTicket(asunto, descripcion, folio, prioridad , fecha ,id_categoria,id_departamento, BdUsurio.idEmpleado)
        print(id_departamento)
        self.modelo_ticket.guardarLineaTiempo(status ,fecha,id_ticket,id_empleado)
        self.mensaje.setText( "Guardado")
        self.mensaje.exec_()
        return
    
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

    def fecha(self):
        '''Definir hora que se guardara '''
        self.hora_inicial = datetime.datetime.now().time()
        fecha = QDate.currentDate()
        fecha_text = fecha.toString('yyyy-MM-dd')
        fecha_creacion  = (str(fecha_text) +" "+ str(self.hora_inicial))
        return fecha_creacion
