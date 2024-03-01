from Models.ticketsModel import ModelTickets
from Models.global_variables import Datos , BdUsurio
from Models.folioModel import ModelFolio
import Views.calendarioView 
from PyQt5.QtCore import QDate
import datetime
from PyQt5 import QtWidgets
from Controllers.ticketDetalles import ticketsDetalles
from PyQt5.QtCore import QTimer

class ticketsResumen():
    def __init__(self, vista):
        #self.ruta = "U:\\Desarrollo\\Chat-Tickes\\"
        self.ruta =  "C:\\ARP\\Chat-Tickes\\"
        self.modelo_ticket =  ModelTickets()
        self.vista = vista
        self.modelo_folio_ticket = ModelFolio()
        self.controller_detalles =  ticketsDetalles(self.vista)
        self.vista.btn_calendario.clicked.connect(lambda: self.abrir_calendario())
        self.vista.btn_guardar_asg_4.clicked.connect(self.guardarFecha_solucion)
        self.vista.btn_sigEstado.clicked.connect(self.cambiar_estado)
        self.vista.btn_reasignar.clicked.connect(self.reasignar_ticket)
        self.vista.btn_verDetalles.clicked.connect(lambda: self.cambiar_pagina(3))
        self.vista.btn_cancelarTicket.clicked.connect(self.cerrar_ticket)
        self.vista.btn_enviar_add_3.clicked.connect(self.guardar_convesacion)
        self.vista.pt_comentarios_3.setReadOnly(True)
        # INICIALIZAR MENSAJES
        self.mensaje = QtWidgets.QMessageBox()
        self.mensaje.setIcon(QtWidgets.QMessageBox.Information)
        self.mensaje.setWindowTitle(". . : : Informacion : : . .")

    def condiciones(self):
        estado_actual = self.vista.lbl_estado_2.text()
        estado_sigiente = self.devuelve_estado_sigiente(estado_actual)
        self.vista.btn_sigEstado.setText(estado_sigiente)

        if Datos.rol == 'RESPONSABLE':
            self.vista.btn_cancelarTicket.setVisible(False)
            if estado_actual == 'ASIGNADO':
                self.vista.btn_guardar_asg_4.setVisible(True)
                self.vista.btn_calendario.setVisible(True)
            else:
                self.vista.btn_guardar_asg_4.setVisible(False)
                self.vista.btn_calendario.setVisible(False)

            if  estado_actual == 'TERMINADO' or estado_actual ==  'CERRADO' or estado_actual == 'CANCELADO':
                self.vista.btn_sigEstado.setVisible(False)
                self.vista.btn_cancelarTicket.setVisible(False)
            elif estado_actual == 'ASIGNADO' or estado_actual == 'PROCESO' :
                self.vista.btn_sigEstado.setVisible(True)


        elif Datos.rol == 'SOLICITANTE':
            if estado_actual == 'ASIGNADO' or estado_actual == 'PROCESO': 
                self.vista.btn_cancelarTicket.setVisible(True)
                self.vista.btn_sigEstado.setVisible(False)
            elif estado_actual == 'TERMINADO':
                self.vista.btn_sigEstado.setVisible(True)
                self.vista.btn_cancelarTicket.setVisible(False)
            elif estado_actual == 'CERRADO' or estado_actual == 'CANCELADO':
                self.vista.btn_sigEstado.setVisible(False)
                self.vista.btn_cancelarTicket.setVisible(False)

            self.vista.btn_guardar_asg_4.setVisible(False)
            self.vista.btn_calendario.setVisible(False)
            self.vista.btn_reasignar.setVisible(False)
            self.vista.cb_empleado_asg.setEnabled(False)

    def ticket_resumen(self, id_ticket):
        Datos.id_ticket = id_ticket
        resumen_ticket = self.modelo_ticket.select_ticket_resumen_by_id(id_ticket)

        if resumen_ticket :
            #Datos.id_ticket = resumen_ticket[0]
            folio = self.modelo_folio_ticket.obtener_folio_byid(resumen_ticket[1])
            Datos.folio_ticket_chat = folio
            self.vista.txt_n_ticket.setText(str(folio))
            self.vista.ptext_asunto_asg.setPlainText(str(resumen_ticket[3]))
            self.vista.cb_departamento_asg.setCurrentText(str(resumen_ticket[4]))
            self.vista.cb_empleado_asg.setCurrentText(str(resumen_ticket[5]))
            self.vista.lbl_estado_2.setText(str(resumen_ticket[7]))
            self.vista.lbl_fecha.setText(str(resumen_ticket[8]))

            if  self.vista.lbl_estado_2.text() == 'ASIGNADO' :
                self.ticket_asigando_campos()
            else:
                self.ticket_enProceso_campos()
        self.vista.cb_departamento_asg.setEnabled(False)
        self.vista.ptext_asunto_asg.setEnabled(False)
        self.condiciones()
        self.cargar_convesacion()
        # Configurar un temporizador para verificar el texto del QLabel periódicamente
        self.timer = QTimer()
        self.timer.timeout.connect(self.cargar_convesacion)
        self.timer.start(1000)  # Verificar cada 100 milisegundos
        self.botones_comentarios_visibles(True)
                
    def abrir_calendario(self):
        self.calendario = Views.calendarioView.Calendario()
        self.calendario.date_selected.connect(self.on_date_selected)
        self.calendario.show()

    def on_date_selected(self, date):
        self.vista.lbl_fecha.setText(str(date))

    def guardarFecha_solucion(self):
        if self.vista.lbl_estado_2.text() == 'ASIGNADO' and self.vista.lbl_fecha.text() != 'ASIGNA UNA FECHA':
            fecha_hoy = self.fecha()
            self.modelo_ticket.asignarFechaSolucion(self.vista.lbl_fecha.text(), Datos.id_ticket )
            self.modelo_ticket.guardar_lineatiempo('PROCESO', fecha_hoy, Datos.id_ticket, BdUsurio.idEmpleado)
            self.ticket_resumen(Datos.id_ticket)
            self.ticket_enProceso_campos()
            Datos.cambio_estado = True
            self.mensaje.setText("FECHA SOLUCION ASIGNADA")
            self.mensaje.exec_()
        else:
            self.mensaje.setText("DEBES ELEGIR  FECHA PARA SOLUCION")
            self.mensaje.exec_()

    def fecha(self):
        """ Definir hora que se guardara """
        self.hora_inicial = datetime.datetime.now().time()
        fecha = QDate.currentDate()
        fecha_text = fecha.toString('yyyy-MM-dd')
        fecha_creacion = (str(fecha_text) + " " + str(self.hora_inicial))
        return fecha_creacion

    def ticket_enProceso_campos(self):
        self.vista.btn_guardar_asg_4.setVisible(False)
        self.vista.btn_calendario.setEnabled(False)
        self.vista.btn_reasignar.setVisible(False)
        self.vista.cb_empleado_asg.setEnabled(False)
        self.vista.lbl_nombre_15.setText("RESPONSABLE")

    def ticket_asigando_campos(self):
        self.vista.btn_guardar_asg_4.setVisible(True)
        self.vista.btn_calendario.setEnabled(True)
        self.vista.btn_reasignar.setVisible(True)
        self.vista.cb_empleado_asg.setEnabled(True)
        self.vista.lbl_nombre_15.setText("ASIGNAR*")

    def devuelve_estado_sigiente(self, estadoActual):
        #if Datos.rol == 'SOLICITANTE':
        #    return 'CERRADO'
        #elif Datos.rol == 'RESPONSABLE':
            estados = ['ASIGNADO', 'PROCESO','TERMINADO', 'CERRADO', 'CANCELADO']
            indice = estados.index(estadoActual)
            siguiente_indice = (indice + 1) % len(estados)
            return estados[siguiente_indice]

    def cambiar_estado(self):
        estado_actual = self.vista.lbl_estado_2.text()
        estado_sigiente = self.devuelve_estado_sigiente(estado_actual)
        if  Datos.rol == 'RESPONSABLE' and estado_sigiente == 'PROCESO' and self.vista.lbl_fecha.text() == 'ASIGNA UNA FECHA':
            self.mensaje.setText("INGRESA FECHA DE SOLUCION: ")
            self.mensaje.exec_()
            return
        
        self.modelo_ticket.guardar_lineatiempo(estado_sigiente,self.fecha(),Datos.id_ticket,BdUsurio.idEmpleado)
        self.ticket_resumen(Datos.id_ticket)
        Datos.cambio_estado = True
        self.mensaje.setText("TICKET EN ESTADO: " + str(estado_sigiente))
        self.mensaje.exec_()
    
    def cerrar_ticket(self):     
        self.modelo_ticket.guardar_lineatiempo('CANCELADO',self.fecha(),Datos.id_ticket,BdUsurio.idEmpleado)
        self.ticket_resumen(Datos.id_ticket)
        Datos.cambio_estado = True
        self.vista.btn_cancelarTicket.setVisible(False)
        self.mensaje.setText("TICKET EN ESTADO: CANCELADO")
        self.mensaje.exec_()
    
    def reasignar_ticket(self):
        if self.vista.lbl_estado_2.text() == 'ASIGNADO':
            id_asignar = self.vista.cb_empleado_asg.currentData()
            self.modelo_ticket.guardar_lineatiempo('ASIGNADO',self.fecha(),Datos.id_ticket,id_asignar)
            self.ticket_resumen(Datos.id_ticket)
            Datos.cambio_estado = True
            self.mensaje.setText("TICKET REACIGNADO A : " + str(self.vista.cb_empleado_asg.currentText()))
            self.mensaje.exec_()
    
    def cambiar_pagina(self, index):
        # Cambiar a la página indicada
        self.vista.multiWidget.setCurrentIndex(index)
        self.controller_detalles.ticket_detalles(Datos.id_ticket)

    def guardar_convesacion(self):
        if self.vista.ptext_comentarios_add_3.toPlainText() != "":
            message = self.vista.ptext_comentarios_add_3.toPlainText().upper()
            self.vista.pt_comentarios_3.appendPlainText(BdUsurio.nombres+": " + message)

            with open(self.ruta+Datos.folio_ticket_chat+".txt", "a") as file:
                file.write(BdUsurio.nombres+": " + message + "\n")

            self.vista.ptext_comentarios_add_3.clear()
        else:
            self.mensaje.setText("Escribe un comentario")
            self.mensaje.exec_()

    def cargar_convesacion(self):
        self.vista.pt_comentarios_3.clear()
        try:
            with open(self.ruta+Datos.folio_ticket_chat+".txt", "r") as file:
                chat_history = file.read()
                self.vista.pt_comentarios_3.setPlainText(chat_history)
        except FileNotFoundError:
            pass
    def botones_comentarios_visibles(self, bool):
        self.vista.btn_enviar_add.setVisible(bool)
        self.vista.btn_enviar_add_3.setVisible(bool)