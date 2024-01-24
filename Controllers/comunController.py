from Models.departamentosModel import BaseDepartamentos, ModelDepartamento
from Models.categoriasTicketsModel import BaseCategorias, ModelCategoria
from Models.userModel import ModelUser


class ControllerComun:

    def llenar_cbdepartameto(self, combo_box):
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

    def llenar_cbcategorias(self, combo_box):
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

    def llenar_cbempleados(self, combo_box):
        """
            Llenar el combo box: Tipo de documento
        """
        combo_box.clear()
        model = ModelUser()
        usuarios_list = model.usuariosASolicitar()
        combo_box.addItem("-------", 0)
        for usuario in usuarios_list:
            combo_box.addItem(usuario[1], usuario[0])

    def llenar_cbestado(self, combo_box):
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

    def llenar_cbprioridad(self, combo_box):
        """
            Llenar el combo box: Tipo de documento
        """
        combo_box.clear()
        combo_box.addItem("-------", 0)
        combo_box.addItem("ALTA", "ALTA")
        combo_box.addItem("MEDIA", "MEDIA")
        combo_box.addItem("BAJA", "BAJA")
        