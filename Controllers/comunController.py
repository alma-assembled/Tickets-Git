from Models.departamentosModel import BaseDepartamentos, ModelDepartamento
from Models.categoriasTicketsModel import BaseCategorias, ModelCategoria
from Models.userModel import ModelUser
from Models.ticketsModel import ModelTickets
from Models.folioModel import ModelFolio
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QStyledItemDelegate, QPushButton 
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette
from Models.global_variables import BdUsurio, Datos
from Controllers.ticketsResumen import ticketsResumen

class ControllerComun:

    @staticmethod
    def llenar_cbdepartameto(combo_box):
        """
             Llenar el combo box: departamentos
        """
        combo_box.clear()
        model = ModelDepartamento()
        departamentos_list = model.base_departamentosall()
        combo_box.addItem("-------", 0)
        for fila in departamentos_list:
            departamento = BaseDepartamentos(fila[0], fila[1])
            combo_box.addItem(departamento.departemanto, departamento.id_departamento)

    @staticmethod
    def llenar_cbcategorias(combo_box):
        """
            Llenar el combo box: Tipo de documento
        """
        combo_box.clear()
        model = ModelCategoria()
        categorias_list = model.base_categoriasall()
        combo_box.addItem("-------", 0)
        for fila in categorias_list:
            categoria = BaseCategorias(fila[0], fila[1])
            combo_box.addItem(categoria.categoria, categoria.idcategoria)

    @staticmethod
    def llenar_cbempleados(combo_box):
        """
            Llenar el combo box: Tipo de documento
        """
        combo_box.clear()
        model = ModelUser()
        usuarios_list = model.usuariosASolicitar()
        combo_box.addItem("-------", 0)
        for usuario in usuarios_list:
            combo_box.addItem(usuario[1], usuario[0])

    @staticmethod
    def llenar_cbestado(combo_box):
        """

            Llenar el combo box: Tipo de documento
        """
        combo_box.clear()
        combo_box.addItem("-------", 0)
        combo_box.addItem("ASIGNADO", "ASIGNADO")
        combo_box.addItem("EN PROCESO", "PROCESO")
        combo_box.addItem("TERMINADO", "TERMINADO")
        combo_box.addItem("CERRADO", "CERRADO")
        combo_box.addItem("CANCELDO", "CANCELADO")

    @staticmethod
    def llenar_cbprioridad(combo_box):
        """
            Llenar el combo box: Tipo de documento
        """
        combo_box.clear()
        combo_box.addItem("-------", 0)
        combo_box.addItem("ALTA", "ALTA")
        combo_box.addItem("MEDIA", "MEDIA")
        combo_box.addItem("BAJA", "BAJA")

    def llenar_tb_dasboar(self, md_tabla, tb_dasboar, vista):
        # Limpiar el modelo de datos
        md_tabla.clear()

        model_ticket = ModelTickets()
        model_folio = ModelFolio()
        if Datos.rol == 'SOLICITANTE':
            md_tabla.setHorizontalHeaderLabels(["N FOLIO", "FECHA", "TITULO", "DEPARTAMENTO",
                                                "RESPONSABLE", "PRIORIDAD", "STATUS","VER"])
            if Datos.filtro == True:
                fecha = vista.lbl_fecha_4.text()
                codigo = vista.text_buscar_d.text()
                status = vista.cb_status_d.currentData()
                id_responsable = vista.cb_empleado_d.currentData()
                id_departamento = vista.cb_departamento_d.currentData()
                id_ticket_categoria = vista.cb_categoria_d.currentData()
                id_solicitante = BdUsurio.idEmpleado
                tickets_all = model_ticket.select_tickets_dashboard_solicitante_filtro(codigo, id_solicitante, status,id_responsable,id_departamento,id_ticket_categoria, fecha)
                Datos.filtro = False
            else:
                tickets_all = model_ticket.select_tickets_dashboard_solicitante(BdUsurio.idEmpleado)

        elif  Datos.rol == 'RESPONSABLE':
            md_tabla.setHorizontalHeaderLabels(["N FOLIO", "FECHA", "TITULO", "DEPARTAMENTO",
                                                "AUTOR", "PRIORIDAD", "STATUS", "VER"])
            if Datos.filtro == True:
                fecha = vista.lbl_fecha_4.text()
                codigo = vista.text_buscar_d.text()
                status = vista.cb_status_d.currentData()
                id_solicitante = vista.cb_empleado_d.currentData()
                id_departamento = vista.cb_departamento_d.currentData()
                id_ticket_categoria = vista.cb_categoria_d.currentData()
                id_responsable = BdUsurio.idEmpleado
                tickets_all = model_ticket.select_tickets_dashboard_responsable_filtro(codigo, id_solicitante, status,id_responsable,id_departamento,id_ticket_categoria,fecha)
                Datos.filtro = False
            else:
                tickets_all = model_ticket.select_tickets_dashboard_responsable(BdUsurio.idEmpleado)

        # Iterar sobre los tickets y agregarlos al modelo de datos
        for  row, ticket in enumerate(tickets_all):
            # Obtener el nombre completo del responsable
            nombre_completo = str(ticket[5]).split()
            nombres = " ".join(nombre_completo[:2]) if len(nombre_completo) >= 2 else ticket[5]

            # Construir el número de folio
            folio_contruido = model_folio.obtener_folio_byid(str(ticket[1]))

            # Crear los ítems de la fila
            n_folio = QStandardItem(folio_contruido)
            fecha = QStandardItem(str(ticket[2]))
            titulo = QStandardItem(str(ticket[3]))
            departamento = QStandardItem(str(ticket[4]))
            responsable = QStandardItem(nombres)
            prioridad = QStandardItem(str(ticket[6]))
            status = QStandardItem(str(ticket[7]))

            # Agregar la fila al modelo de datos
            md_tabla.appendRow([n_folio, fecha, titulo, departamento, responsable, prioridad, status])

            # Establecer el identificador único en el rol UserRole para la fila actual
            index = md_tabla.index(row, 0)
            md_tabla.setData(index, ticket[0], Qt.UserRole)

            # Agregar un botón
            button = QPushButton("VER")
            button.clicked.connect(lambda: self.on_button_clicked_dashboard(md_tabla,tb_dasboar, vista))
            tb_dasboar.setIndexWidget(md_tabla.index(row, 7), button)

        # Asignar el modelo de datos a la tabla
        tb_dasboar.setModel(md_tabla)

        # Asignar el delegado personalizado a la columna de STATUS
        delegate = ColorDelegate()
        tb_dasboar.setItemDelegateForColumn(6, delegate)

        # Estilizar el encabezado de la tabla
        header = tb_dasboar.horizontalHeader()
        header.setStyleSheet("background-color: #3c4145;color: #3c4145;")
    
    def llenar_tb_mis_tickets(self, md_tabla, tb_tickets, vista):
        # Limpiar el modelo de datos
        md_tabla.clear()

        model_ticket = ModelTickets()
        model_folio = ModelFolio()

        if Datos.rol == 'SOLICITANTE':
            md_tabla.setHorizontalHeaderLabels(["N FOLIO", "FECHA", "TITULO", "DEPARTAMENTO",
                                                "RESPONSABLE", "PRIORIDAD", "STATUS","VER"])
            if Datos.filtro == True:
                fecha = vista.lbl_fecha_3.text()
                codigo = vista.text_buscar_t.text()
                status = vista.cb_status_t.currentData()
                id_responsable = vista.cb_empleado_t.currentData()
                id_departamento = vista.cb_departamento_t.currentData()
                id_ticket_categoria = vista.cb_categoria_t.currentData()
                id_solicitante = BdUsurio.idEmpleado
                tickets_all = model_ticket.filtro_select_tickets_mis_tickets_solicitante(codigo, id_solicitante, status,id_responsable,id_departamento,id_ticket_categoria,fecha)
                Datos.filtro = False
            else:
                tickets_all = model_ticket.select_tickets_mis_tickets_solicitante(BdUsurio.idEmpleado)
        elif  Datos.rol == 'RESPONSABLE':
            md_tabla.setHorizontalHeaderLabels(["N FOLIO", "FECHA", "TITULO", "DEPARTAMENTO",
                                                "AUTOR", "PRIORIDAD", "STATUS","VER"])
            if Datos.filtro == True:
                fecha = vista.lbl_fecha_3.text()
                codigo = vista.text_buscar_t.text()
                status = vista.cb_status_t.currentData()
                id_solicitante = vista.cb_empleado_t.currentData()
                id_departamento = vista.cb_departamento_t.currentData()
                id_ticket_categoria = vista.cb_categoria_t.currentData()
                id_responsable = BdUsurio.idEmpleado
                tickets_all = model_ticket.filtro_select_tickets_mis_tickets_reponsable(codigo, id_solicitante, status,id_responsable,id_departamento,id_ticket_categoria, fecha)
                Datos.filtro = False
            else:
                tickets_all = model_ticket.select_tickets_mis_tickets_responsable(BdUsurio.idEmpleado)

        # Iterar sobre los tickets y agregarlos al modelo de datos
        for row, ticket in enumerate(tickets_all):
            # Obtener el nombre completo del responsable
            nombre_completo = str(ticket[5]).split()
            nombres = " ".join(nombre_completo[:2]) if len(nombre_completo) >= 2 else ticket[5]

            # Construir el número de folio
            folio_contruido = model_folio.obtener_folio_byid(str(ticket[1]))

            # Crear los ítems de la fila
            n_folio = QStandardItem(folio_contruido)
            fecha = QStandardItem(str(ticket[2]))
            titulo = QStandardItem(str(ticket[3]))
            departamento = QStandardItem(str(ticket[4]))
            responsable = QStandardItem(nombres)
            prioridad = QStandardItem(str(ticket[6]))
            status = QStandardItem(str(ticket[7]))

            # Agregar la fila al modelo de datos
            md_tabla.appendRow([n_folio, fecha, titulo, departamento, responsable, prioridad, status])

            # Establecer el identificador único en el rol UserRole para la fila actual
            index = md_tabla.index(row, 0)
            md_tabla.setData(index, ticket[0], Qt.UserRole)

            # Agregar un botón
            button = QPushButton("VER")
            button.clicked.connect(lambda: self.on_button_clicked_mis_tickets(md_tabla, tb_tickets, vista))
            tb_tickets.setIndexWidget(md_tabla.index(row, 7), button)

        # Asignar el modelo de datos a la tabla
        tb_tickets.setModel(md_tabla)

        # Asignar el delegado personalizado a la columna de STATUS
        delegate = ColorDelegate()
        tb_tickets.setItemDelegateForColumn(6, delegate)

        # Estilizar el encabezado de la tabla
        header = tb_tickets.horizontalHeader()
        header.setStyleSheet("background-color: #3c4145;color: #3c4145;")
    
    def on_button_clicked_mis_tickets(self, md_tabla, tb_ticket, vista):
        ticket_resumen =  ticketsResumen(vista)
        # Obtener los índices de las filas seleccionadas 
        selected_indexes = tb_ticket.selectionModel().selectedRows()
        for index in sorted(selected_indexes, reverse=True):
            # Obtener el identificador único de la fila seleccionada
            id_unique = md_tabla.data(index, Qt.UserRole)
            #print("Id:", id_unique)
            self.cambiar_pagina(4, vista)
            ticket_resumen.ticket_resumen(id_unique)
            
    def on_button_clicked_dashboard(self, md_tabla, tb_dasboar, vista):
        ticket_resumen =  ticketsResumen(vista)
        # Obtener los índices de las filas seleccionadas 
        selected_indexes = tb_dasboar.selectionModel().selectedRows()
        for index in sorted(selected_indexes, reverse=True):
            # Obtener el identificador único de la fila seleccionada
            id_unique = md_tabla.data(index, Qt.UserRole)
            #print("Id:", id_unique)
            self.cambiar_pagina(4, vista)
            ticket_resumen.ticket_resumen(id_unique)

    def cambiar_pagina(self, index, vista):
        # Cambiar a la página indicada
        vista.multiWidget.setCurrentIndex(index)
        
class ColorDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        value = index.data(Qt.DisplayRole)  # Obtener el valor de la celda

        # Cambiar el color de fondo basado en el valor
        if value == "ASIGNADO":
            option.backgroundBrush = QColor("#D8863B")
            option.palette.setColor(QPalette.Text, QColor(Qt.white))
        elif value == "PROCESO":
            option.backgroundBrush = QColor("#063456")
            option.palette.setColor(QPalette.Text, QColor(Qt.white))
        elif value == "TERMINADO":
            option.backgroundBrush = QColor("#2B8544")
            option.palette.setColor(QPalette.Text, QColor(Qt.white))
        elif value == "CERRADO":
            option.backgroundBrush = QColor("#3B96D8")
            option.palette.setColor(QPalette.Text, QColor(Qt.white))
        elif value == "CANCELADO":
            option.backgroundBrush = QColor("#CE2323")
            option.palette.setColor(QPalette.Text, QColor(Qt.white))

class ButtonDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(ButtonDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        if index.column() == 3 and index.row() == 0:  # Columna 3, fila
            pass