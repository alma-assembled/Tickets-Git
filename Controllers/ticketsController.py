from Models.global_variables import BdUsurio
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
import datetime
from Controllers.comunController import ControllerComun
from Models.ticketsModel import ModelTickets
from Models.folioModel import ModelFolio


class CrontrollerTicket:
    def __init__(self, vista, ventana):
        self.hora_inicial = None
        self.vista = vista
        self.ventana = ventana
        # CONTROLADORES
        self.controllerComon = ControllerComun()  

        # MODELOS
        self.modelo_ticket = ModelTickets()
        self.modelo_folio_ticket = ModelFolio()

        # INICIAL
        self.llenar_info_inicial()
        self.modo_solicitante()
        
        # INICIALIZAR MENSAJES
        self.mensaje = QtWidgets.QMessageBox()
        self.mensaje.setIcon(QtWidgets.QMessageBox.Information)
        self.mensaje.setWindowTitle(". . : : Informacion : : . .")

        # EVENTOS
        self.vista.rb_solicitante.clicked.connect(self.evtradio_button_toggled)
        self.vista.rb_responsable.clicked.connect(self.evtradio_button_toggled)
        self.vista.btn_addTicket.clicked.connect(lambda: self.cambiar_pagina(3))
        self.vista.btn_dashboard.clicked.connect(lambda: self.cambiar_pagina(0))
        self.vista.btn_ticket.clicked.connect(lambda: self.cambiar_pagina(2))
        self.vista.btn_myTickets.clicked.connect(lambda: self.cambiar_pagina(2))
        self.vista.btn_gurdar_add.clicked.connect(self.evtguardar_ticket)

    def llenar_info_inicial(self):
        """
            Descripcion: llenar la informacion inicial apartir que el usuario logeando
        """
        self.cambiar_pagina(0)
        nombre_completo = BdUsurio.nombre.split()
        nombres = " ".join([str(nombre_completo[0]), str(nombre_completo[1])])
        self.vista.lb_nombre.setText(nombres)
        self.vista.rb_solicitante.setChecked(True)
        self.controllerComon.llenar_cbdepartameto(self.vista.cb_departamento_d)
        self.controllerComon.llenar_cbdepartameto(self.vista.cb_departamento_t)
        self.controllerComon.llenar_cbdepartameto(self.vista.cb_departamento_add)
        self.controllerComon.llenar_cbdepartameto(self.vista.cb_departamento_asg)

        self.controllerComon.llenar_cbcategorias(self.vista.cb_categoria_d)
        self.controllerComon.llenar_cbcategorias(self.vista.cb_categoria_t)
        self.controllerComon.llenar_cbcategorias(self.vista.cb_categoria_add)

        self.controllerComon.llenar_cbempleados(self.vista.cb_empleado_d)
        self.controllerComon.llenar_cbempleados(self.vista.cb_empleado_t)
        self.controllerComon.llenar_cbempleados(self.vista.cb_empleado_add)
        self.controllerComon.llenar_cbempleados(self.vista.cb_empleado_asg)

        self.controllerComon.llenar_cbestado(self.vista.cb_status_d)
        self.controllerComon.llenar_cbestado(self.vista.cb_status_t)
        self.controllerComon.llenar_cbprioridad(self.vista.cb_prioridad_add)

    # EVENTOS
    def evtradio_button_toggled(self):
        """
        Descripcion:
            Evento disparado al cambiar el  estado del radio button
            Limpiar el campo txt_tiempo despues de cambiar el estado
        """
        self.cambiar_pagina(0)
        if self.vista.rb_responsable.isChecked():
            self.modo_responsable()
        elif self.vista.rb_solicitante.isChecked():
            self.modo_solicitante()

    def evtguardar_ticket(self):
        id_departamento = self.vista.cb_departamento_add.currentData()
        id_categoria = self.vista.cb_categoria_add.currentData()
        prioridad = self.vista.cb_prioridad_add.currentData()
        id_empleado = self.vista.cb_empleado_add.currentData()
        asunto = self.vista.ptext_asunto_add.toPlainText()
        descripcion = self.vista.ptext_descripcion_add.toPlainText()
        fecha = self.fecha()
        status = "ASIGNADO"
        if (id_departamento == 0 or id_categoria == 0 or id_empleado == 0 or prioridad == 0 or asunto == ""
                or descripcion == ""):
            self.mensaje.setText("Debes llenar todos los campos")
            self.mensaje.exec_()
            return
        numero_consecutivo_folio = self.modelo_folio_ticket.generar_numero_foliodepartamento(id_departamento)
        id_folio = self.modelo_folio_ticket.create_folio(numero_consecutivo_folio, id_departamento)
        folio_generado = self.modelo_folio_ticket.obtener_folio_byid(id_folio)
        id_ticket = self.modelo_ticket.guardar_ticket(asunto, descripcion, prioridad, fecha, id_categoria,
                                                      id_departamento, BdUsurio.idEmpleado, id_folio)
        self.modelo_ticket.guardar_lineatiempo(status, fecha, id_ticket, id_empleado)
        self.mensaje.setText("Ticket " + str(folio_generado) + " generado correctamente")
        self.mensaje.exec_()
        return

    def cambiar_pagina(self, index):
        # Cambiar a la página indicada
        self.vista.multiWidget.setCurrentIndex(index)

    def modo_solicitante(self):
        self.setwidgetsvisibility(True, True, True, True, True, True, False, False)

    def modo_responsable(self):
        self.setwidgetsvisibility(True, True, False, False, True, True, False, False)

    def setwidgetsvisibility(self, btn_dashboard, fr_dashboard, btn_addticket, fr_addticket, btn_ticket, fr_ticket,
                             btn_mytickets, fr_mytickets):
        self.vista.btn_dashboard.setVisible(btn_dashboard)
        self.vista.fr_dashboard.setVisible(fr_dashboard)
        self.vista.btn_addTicket.setVisible(btn_addticket)
        self.vista.fr_addTicket.setVisible(fr_addticket)
        self.vista.btn_ticket.setVisible(btn_ticket)
        self.vista.fr_ticket.setVisible(fr_ticket)
        self.vista.btn_myTickets.setVisible(btn_mytickets)
        self.vista.fr_myTickets.setVisible(fr_mytickets)

    def fecha(self):
        """ Definir hora que se guardara """
        self.hora_inicial = datetime.datetime.now().time()
        fecha = QDate.currentDate()
        fecha_text = fecha.toString('yyyy-MM-dd')
        fecha_creacion = (str(fecha_text) + " " + str(self.hora_inicial))
        return fecha_creacion
