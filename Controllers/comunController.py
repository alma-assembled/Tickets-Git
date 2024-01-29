from Models.departamentosModel import BaseDepartamentos, ModelDepartamento
from Models.categoriasTicketsModel import BaseCategorias, ModelCategoria
from Models.userModel import ModelUser
from Models.ticketsModel import ModelTickets
from Models.folioModel import ModelFolio
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QStyledItemDelegate
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter

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
        combo_box.addItem("ASIGNADo", "ASIGNADO")
        combo_box.addItem("EN PROCESO", "PROCESO")
        combo_box.addItem("TERMINADO", "TEMINADO")
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

    @staticmethod
    def llenar_tb_dasboar(md_tabla, tb_dasboar, bandera):
        #tb_dasboar.clear()
        #md_tabla.clear()
        model_ticket = ModelTickets()
        model_folio = ModelFolio()
        if bandera == True:
            tickets_all = model_ticket.select_mis_tickets_solicitante(117)
        else:
            tickets_all = model_ticket.select_mis_tickets_responsable(117)
        for ticket in tickets_all:
            nombre_completo = str(ticket[6]).split()
            nombres = " ".join([str(nombre_completo[0]), str(nombre_completo[1])])
            folio_contruido = model_folio.obtener_folio_byid(str(ticket[1]))
            n_folio = QStandardItem(folio_contruido)
            fecha = QStandardItem(str(ticket[2]))
            titulo = QStandardItem(str(ticket[3]))
            departamento = QStandardItem(str(ticket[4]))
            categoria = QStandardItem(str(ticket[5]))
            responsable = QStandardItem(nombres)
            prioridad = QStandardItem(str(ticket[7]))
            status = QStandardItem(str(ticket[8]))
            md_tabla.appendRow([n_folio, fecha, titulo, departamento, categoria, responsable, prioridad, status])
            tb_dasboar.setModel(md_tabla)

            # Asignar el delegado personalizado a la primera columna
            delegate = ColorDelegate()
            tb_dasboar.setItemDelegateForColumn(7, delegate)


class ColorDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        value = index.data(Qt.DisplayRole)  # Obtener el valor de la celda

        painter = QPainter()

        # Cambiar el color de fondo basado en el valor
        if value == "ASIGNADO":
            option.backgroundBrush = QColor("#D8863B")
            #option. =  painter.setPen(QColor(Qt.white))
        elif value == "PROCESO":
            option.backgroundBrush = QColor("#063456")
        elif value == "TERMINADO":
            option.backgroundBrush = QColor("#2B8544")
        elif value == "CERRADO":
            option.backgroundBrush = QColor("#3B96D8")
        elif value == "CANCELADO":
            option.backgroundBrush = QColor("#CE2323")
