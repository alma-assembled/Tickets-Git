from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
import datetime
from Controllers.comunController import ControllerComun
from Models.ticketsModel import ModelTickets
from Models.folioModel import ModelFolio
from PyQt5.QtGui import QStandardItemModel
from Models.global_variables import Datos, BdUsurio
from PyQt5.QtCore import QTimer
import Views.calendarioView 

class CrontrollerTicket:
    def __init__(self, vista, ventana):
        self.solicitante = True
        self.hora_inicial = None
        self.vista = vista
        self.ventana = ventana
        # CONTROLADORES
        self.controllerComon = ControllerComun()  

        # MODELOS
        self.modelo_ticket = ModelTickets()
        self.modelo_folio_ticket = ModelFolio()
        
        # INICIALIZAR MENSAJES
        self.mensaje = QtWidgets.QMessageBox()
        self.mensaje.setIcon(QtWidgets.QMessageBox.Information)
        self.mensaje.setWindowTitle(". . : : Informacion : : . .")

        # EVENTOS
        self.vista.rb_solicitante.clicked.connect(self.evtradio_button_toggled)
        self.vista.rb_responsable.clicked.connect(self.evtradio_button_toggled)
        self.vista.btn_addTicket.clicked.connect(self.agregar_ticket_nuevo)
        self.vista.btn_dashboard.clicked.connect(lambda: self.cambiar_pagina(0))
        self.vista.btn_ticket.clicked.connect(lambda: self.cambiar_pagina(2))
        self.vista.btn_myTickets.clicked.connect(lambda: self.cambiar_pagina(2))
        self.vista.btn_gurdar_add.clicked.connect(self.evtguardar_ticket)
        self.vista.btn_allTickets_d.clicked.connect(self.limpiar_filtros)
        self.vista.btn_buscar_d.clicked.connect(self.filtrar_ticketsdashboard)
        self.vista.btn_buscar_t.clicked.connect(self.filtar_mis_ticket)
        self.vista.btn_allTickets_t.clicked.connect(self.limpiar_filtros)
        self.vista.btn_add_ticket_t.clicked.connect(self.agregar_ticket_nuevo)
        self.vista.btn_crearTicket.clicked.connect(self.agregar_ticket_nuevo) 
        self.vista.btn_calendario_4.clicked.connect(lambda: self.abrir_calendario_dasboard())
        self.vista.btn_calendario_3.clicked.connect(lambda: self.abrir_calendario_mis_tickets())
        # Tabla dashboart
        self.tb_dashboart_modelo = QStandardItemModel()
        self.vista.tb_tickets_dashboar.setModel(self.tb_dashboart_modelo)
        self.vista.tb_tickets_dashboar.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # Tabla mis tickets
        self.tb_mis_tikets_modelo = QStandardItemModel()
        self.vista.tb_mis_tickets.setModel(self.tb_mis_tikets_modelo)
        self.vista.tb_mis_tickets.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # Crear un modelo para el QlistView
        self.model_ops = QStandardItemModel()

        # INICIAL
        self.llenar_info_inicial()
        self.modo_solicitante()
        self.dashboard_contontar()

        # Configurar un temporizador para verificar el texto del QLabel periódicamente
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_tablas)
        self.timer.start(1000)  # Verificar cada 100 milisegundos


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

        # TABLA DASBOART
        self.controllerComon.llenar_tb_dasboar(self.tb_dashboart_modelo, self.vista.tb_tickets_dashboar, self.vista)
        self.controllerComon.llenar_tb_mis_tickets(self.tb_mis_tikets_modelo, self.vista.tb_mis_tickets,  self.vista )
    
    def actualizar_tablas(self):
        if Datos.cambio_estado:
            self.controllerComon.llenar_tb_dasboar(self.tb_dashboart_modelo, self.vista.tb_tickets_dashboar, self.vista)
            self.controllerComon.llenar_tb_mis_tickets(self.tb_mis_tikets_modelo, self.vista.tb_mis_tickets,  self.vista)
            Datos.cambio_estado = False
    # EVENTOS
    def evtradio_button_toggled(self):
        """
        Descripcion:
            Evento disparado al cambiar el  estado del radio button
            Limpiar el campo txt_tiempo despues de cambiar el estado
        """
        #Self.cambiar_pagina(0)
        if self.vista.rb_responsable.isChecked():
            self.modo_responsable()
        elif self.vista.rb_solicitante.isChecked():
            self.modo_solicitante()
        self.dashboard_contontar()

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
                                                      id_departamento, BdUsurio.idEmpleado, id_folio, folio_generado)
        self.modelo_ticket.guardar_lineatiempo(status, fecha, id_ticket, id_empleado)
        
        self.campos_ticket_despues_creacrear(folio_generado,fecha)
        self.controllerComon.llenar_tb_dasboar(self.tb_dashboart_modelo, self.vista.tb_tickets_dashboar,   self.vista)
        self.controllerComon.llenar_tb_mis_tickets(self.tb_mis_tikets_modelo, self.vista.tb_mis_tickets,  self.vista )
        
        self.mensaje.setText("Ticket " + str(folio_generado) + " generado correctamente")
        self.mensaje.exec_()
        return

    def campos_ticket_despues_creacrear(self, ticket, fecha):
        self.vista.lbl_n_ticket.setText(ticket)
        self.vista.lbl_fecha_creacion.setText(fecha)
        self.vista.lbl_estado.setText('ASIGNADO')
        self.vista.lbl_fecha_creacion.setVisible(True)
        self.vista.lb_fechaCreacion.setVisible(True)
        self.vista.cb_departamento_add.setEnabled(False)
        self.vista.cb_prioridad_add.setEnabled(False)
        self.vista.cb_categoria_add.setEnabled(False)
        self.vista.ptext_asunto_add.setEnabled(False)
        self.vista.cb_empleado_add.setEnabled(False)
        self.vista.ptext_descripcion_add.setEnabled(False)
        self.vista.btn_gurdar_add.setVisible(False)

    def cambiar_pagina(self, index):
        # Cambiar a la página indicada
        self.vista.multiWidget.setCurrentIndex(index)

    def agregar_ticket_nuevo(self):
        self.cambiar_pagina(3)
        self.vista.lbl_nombres.setText("")
        self.vista.cb_departamento_add.setCurrentText("")
        self.vista.cb_prioridad_add.setCurrentText("")
        self.vista.cb_categoria_add.setCurrentText("")
        self.vista.lbl_fecha_2.setText("")
        self.vista.ptext_asunto_add.setPlainText("")
        self.vista.ptext_descripcion_add.setPlainText("")
        self.vista.cb_empleado_add.setCurrentText("")
        self.vista.lbl_n_ticket.setText("")
        self.vista.lbl_fecha_creacion.setText("")
        self.vista.lbl_estado.setText("")
        self.vista.cb_departamento_add.setEnabled(True)
        self.vista.cb_prioridad_add.setEnabled(True)
        self.vista.cb_categoria_add.setEnabled(True)
        self.vista.ptext_asunto_add.setEnabled(True)
        self.vista.cb_empleado_add.setEnabled(True)
        self.vista.ptext_descripcion_add.setEnabled(True)
        self.vista.btn_gurdar_add.setVisible(True)

        nombre_completo = BdUsurio.nombre.split()
        nombres = " ".join([str(nombre_completo[0]), str(nombre_completo[1])])
        self.vista.lbl_nombres.setText(nombres)

        #invisible
        self.vista.lb_fechaSolucion.setVisible(False)
        self.vista.lbl_fecha_2.setVisible(False)
        self.vista.btn_calendario_2.setVisible(False)
        self.vista.btn_guardar_asg_6.setVisible(False)
        self.vista.lbl_fecha_creacion.setVisible(False)
        self.vista.lb_fechaCreacion.setVisible(False)

    def modo_solicitante(self):
        self.solicitante = True
        Datos.rol ='SOLICITANTE'
        self.setwidgetsvisibility(True, True, True, True, True, True, False, False)
        
    def modo_responsable(self):
        self.solicitante = False
        Datos.rol ='RESPONSABLE'
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
        self.vista.btn_add_ticket_t.setVisible(btn_addticket)
        self.vista.btn_crearTicket.setVisible(btn_addticket)

        self.controllerComon.llenar_tb_dasboar(self.tb_dashboart_modelo, self.vista.tb_tickets_dashboar,  self.vista)
        self.controllerComon.llenar_tb_mis_tickets(self.tb_mis_tikets_modelo, self.vista.tb_mis_tickets, self.vista )
    
    def fecha(self):
        """ Definir hora que se guardara """
        self.hora_inicial = datetime.datetime.now().time()
        fecha = QDate.currentDate()
        fecha_text = fecha.toString('yyyy-MM-dd')
        fecha_creacion = (str(fecha_text) + " " + str(self.hora_inicial))
        return fecha_creacion

    def dashboard_contontar(self):
        if Datos.rol == "SOLICITANTE":
            self.vista.lb_contador_asignados.setText(str(self.modelo_ticket.count_estado_solicitante(BdUsurio.idEmpleado, "ASIGNADO")[0]))
            self.vista.lb_contadorproceso.setText(str(self.modelo_ticket.count_estado_solicitante(BdUsurio.idEmpleado, 'PROCESO')[0]))
            self.vista.lb_contador_terminados.setText(str(self.modelo_ticket.count_estado_solicitante(BdUsurio.idEmpleado, 'TERMINADO')[0]))
            self.vista.lb_contador_cerrados.setText(str(self.modelo_ticket.count_estado_solicitante(BdUsurio.idEmpleado, 'CERRADO')[0]))
            self.vista.lb_contadorCancelados.setText(str(self.modelo_ticket.count_estado_solicitante(BdUsurio.idEmpleado, 'CANCELADO')[0]))
        elif Datos.rol == "RESPONSABLE":
            pass
            self.vista.lb_contador_asignados.setText(str(self.modelo_ticket.count_estado_responsable(BdUsurio.idEmpleado, 'ASIGNADO')[0]))
            self.vista.lb_contadorproceso.setText(str(self.modelo_ticket.count_estado_responsable(BdUsurio.idEmpleado, 'PROCESO')[0]))
            self.vista.lb_contador_terminados.setText(str(self.modelo_ticket.count_estado_responsable(BdUsurio.idEmpleado, 'TERMINADO')[0]))
            self.vista.lb_contador_cerrados.setText(str(self.modelo_ticket.count_estado_responsable(BdUsurio.idEmpleado, 'CERRADO')[0]))
            self.vista.lb_contadorCancelados.setText(str(self.modelo_ticket.count_estado_responsable(BdUsurio.idEmpleado, 'CANCELADO')[0]))

    def filtrar_ticketsdashboard(self):
        Datos.filtro = True
        self.controllerComon.llenar_tb_dasboar(self.tb_dashboart_modelo, self.vista.tb_tickets_dashboar,  self.vista)
        
    def filtar_mis_ticket(self):
        Datos.filtro = True
        self.controllerComon.llenar_tb_mis_tickets(self.tb_mis_tikets_modelo, self.vista.tb_mis_tickets,  self.vista )

    def limpiar_filtros(self):
                self.vista.lbl_fecha_4.setText('XXXX-XX-XX')
                self.vista.text_buscar_d.setText("")
                self.vista.cb_status_d.setCurrentIndex(0)
                self.vista.cb_empleado_d.setCurrentIndex(0)
                self.vista.cb_departamento_d.setCurrentIndex(0)
                self.vista.cb_categoria_d.setCurrentIndex(0)
                self.controllerComon.llenar_tb_dasboar(self.tb_dashboart_modelo, self.vista.tb_tickets_dashboar,  self.vista)

                self.vista.lbl_fecha_3.setText('XXXX-XX-XX')
                self.vista.text_buscar_t.setText("")
                self.vista.cb_status_t.setCurrentIndex(0)
                self.vista.cb_empleado_t.setCurrentIndex(0)
                self.vista.cb_departamento_t.setCurrentIndex(0)
                self.vista.cb_categoria_t.setCurrentIndex(0)
                self.controllerComon.llenar_tb_mis_tickets(self.tb_mis_tikets_modelo, self.vista.tb_mis_tickets,  self.vista )

    def abrir_calendario_dasboard(self):
        self.calendario = Views.calendarioView.Calendario()
        self.calendario.date_selected.connect(self.on_date_selected_dasboard)
        self.calendario.show()
    
    def on_date_selected_dasboard(self, date):
        self.vista.lbl_fecha_4.setText(str(date))

    def abrir_calendario_mis_tickets(self):
        self.calendario = Views.calendarioView.Calendario()
        self.calendario.date_selected.connect(self.on_date_selected_mis_tickets)
        self.calendario.show()

    def on_date_selected_mis_tickets(self, date):
        self.vista.lbl_fecha_3.setText(str(date))