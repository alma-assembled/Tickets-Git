from Models.ticketsModel import ModelTickets
from Models.global_variables import Datos , BdUsurio
from Models.folioModel import ModelFolio
import Views.calendarioView 
from PyQt5.QtCore import QDate
import datetime
from PyQt5 import QtWidgets

class ticketsDetalles():
    def __init__(self, vista):
        self.modelo_ticket =  ModelTickets()
        self.vista = vista
        self.modelo_folio_ticket = ModelFolio()
        self.vista.btn_guardar_asg_6.clicked.connect(self.guardarFecha_solucion)
        self.vista.btn_calendario_2.clicked.connect(lambda: self.abrir_calendario())
        # INICIALIZAR MENSAJES
        self.mensaje = QtWidgets.QMessageBox()
        self.mensaje.setIcon(QtWidgets.QMessageBox.Information)
        self.mensaje.setWindowTitle(". . : : Informacion : : . .")

    def ticket_detalles(self, id_ticket):
        Datos.id_ticket = id_ticket
        ticket_detalle = self.modelo_ticket.select_ticket_detalles_by_id(id_ticket)
        
        if ticket_detalle :
            #Datos.id_ticket = resumen_ticket[0]
            if  self.vista.lbl_estado_2.text() == 'ASIGNADO' :
                self.ticket_asigando_campos()
            else:
                self.ticket_enProceso_campos()
            folio = self.modelo_folio_ticket.obtener_folio_byid(ticket_detalle[1])
            self.vista.lbl_nombres.setText(str(ticket_detalle[8]))
            self.vista.cb_departamento_add.setCurrentText(str(ticket_detalle[5]))
            self.vista.cb_prioridad_add.setCurrentText(str(ticket_detalle[9]))
            self.vista.cb_categoria_add.setCurrentText(str(ticket_detalle[6]))
            self.vista.lbl_fecha_2.setText(str(ticket_detalle[10]))
            self.vista.ptext_asunto_add.setPlainText(str(ticket_detalle[3]))
            self.vista.ptext_descripcion_add.setPlainText(str(ticket_detalle[4]))
            self.vista.cb_empleado_add.setCurrentText(str(ticket_detalle[7]))
            self.vista.lbl_n_ticket.setText(str(folio))
            self.vista.lbl_fecha_creacion.setText(str(ticket_detalle[2]))
            self.vista.lbl_estado.setText(str(ticket_detalle[11]))
            self.vista.cb_departamento_add.setEnabled(False)
            self.vista.cb_prioridad_add.setEnabled(False)
            self.vista.cb_categoria_add.setEnabled(False)
            self.vista.ptext_asunto_add.setEnabled(False)
            self.vista.cb_empleado_add.setEnabled(False)
            self.vista.ptext_descripcion_add.setEnabled(False)
            self.vista.btn_gurdar_add.setVisible(False)

    def abrir_calendario(self):
        self.calendario = Views.calendarioView.Calendario()
        self.calendario.date_selected.connect(self.on_date_selected)
        self.calendario.show()

    def on_date_selected(self, date):
        self.vista.lbl_fecha_2.setText(str(date))

    def guardarFecha_solucion(self):
        if self.vista.lbl_estado.text() == 'ASIGNADO' and self.vista.lbl_fecha_2.text() != 'ASIGNA UNA FECHA':
            fecha_hoy = self.fecha()
            self.modelo_ticket.asignarFechaSolucion(self.vista.lbl_fecha_2.text(), Datos.id_ticket )
            self.modelo_ticket.guardar_lineatiempo('PROCESO', fecha_hoy, Datos.id_ticket, BdUsurio.idEmpleado)
            self.ticket_detalles(Datos.id_ticket)
            self.ticket_enProceso_campos()
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
        self.vista.btn_guardar_asg_6.setVisible(False)
        self.vista.btn_calendario_2.setEnabled(False)
        self.vista.cb_empleado_asg.setEnabled(False)
        self.vista.lbl_agregar_ticket.setText("TICKET")

    def ticket_asigando_campos(self):
        self.vista.btn_guardar_asg_6.setVisible(True)
        self.vista.btn_calendario_2.setEnabled(True)
        self.vista.cb_empleado_asg.setEnabled(True)
        self.vista.lbl_agregar_ticket.setText("TICKET")

    def devuelve_estado_sigiente(self, estadoActual):
        estados = ['ASIGNADO', 'PROCESO','TERMINADO','CERRADO','CANCELADO']
        indice = estados.index(estadoActual)
        siguiente_indice = (indice + 1) % len(estados)
        return estados[siguiente_indice]

    def cambiar_estado(self):
        estado_actual = self.vista.lbl_estado_2.text()
        estado_sigiente = self.devuelve_estado_sigiente(estado_actual)
        if estado_sigiente == 'PROCESO':
            self.mensaje.setText("INGRESA FECHA DE SOLUCION: ")
            self.mensaje.exec_()
            return
        self.modelo_ticket.guardar_lineatiempo(estado_sigiente,self.fecha(),Datos.id_ticket,BdUsurio.idEmpleado)
        self.ticket_resumen(Datos.id_ticket)
        self.mensaje.setText("TICKET EN ESTADO: " + estado_sigiente)
        self.mensaje.exec_()
    
    def reasignar_ticket(self):
        if self.vista.lbl_estado_2.text() == 'ASIGNADO':
            id_asignar = self.vista.cb_empleado_asg.currentData()
            self.modelo_ticket.guardar_lineatiempo('ASIGNADO',self.fecha(),Datos.id_ticket,id_asignar)
            self.ticket_resumen(Datos.id_ticket)
            self.mensaje.setText("TICKET REACIGNADO A : " + str(self.vista.cb_empleado_asg.currentText()))
            self.mensaje.exec_()
    
    def cambiar_pagina(self, index, vista):
        # Cambiar a la página indicada
        vista.multiWidget.setCurrentIndex(index)

    