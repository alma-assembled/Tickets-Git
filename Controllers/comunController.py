from Models.departamentosModel import BaseDepartamentos, ModelDepartamento
from Models.categoriasTicketsModel import BaseCategorias, ModelCategoria
from Models.userModel import ModelUser, Usuario


class ControllerComun:
    def __init__(self):
     pass   

    def llenarCbDepartameto(self, comboBox):
        '''
        Llenar el combo box: departamentos
        '''
        comboBox.clear() 
        model =ModelDepartamento()
        departamentos_list =  model.baseDepartamentosAll()
        comboBox.addItem("-------",0)
        for fila in departamentos_list:
            departamento = BaseDepartamentos(fila[0],fila[1])
            comboBox.addItem(departamento.departemanto, departamento.idDepartamento) 


    def llenarCbCategorias(self, comboBox):
        '''
            Llenar el combo box: Tipo de documento
        '''
        comboBox.clear() 
        model = ModelCategoria()
        categorias_list =  model.baseCategoriasAll()
        comboBox.addItem("-------",0)
        for fila in categorias_list:
            categoria = BaseCategorias(fila[0],fila[1])
            comboBox.addItem(categoria.categoria, categoria.idCategoria)
   

    def llenarCbEmpleados(self, comboBox):
        '''
            Llenar el combo box: Tipo de documento
        '''
        comboBox.clear() 
        model = ModelUser()
        usuarios_list =  model.usuariosASolicitar()
        comboBox.addItem("-------",0)
        for usuario in usuarios_list:
            comboBox.addItem(usuario[1], usuario[0])

    def llenarCbEstado(self, comboBox):
        '''
            Llenar el combo box: Tipo de documento
        '''
        comboBox.clear() 
        comboBox.addItem("-------",0)
        comboBox.addItem("ASIGNADo","ASIGNADO")
        comboBox.addItem("EN PROCESO","PROCESO")
        comboBox.addItem("TERMINADO","TEMINADO")
        comboBox.addItem("CERRADO","CERRADO")
        comboBox.addItem("CANCELDO","CANCELADO")

    def llenarCbPrioridad(self, comboBox):
        '''
            Llenar el combo box: Tipo de documento
        '''
        comboBox.clear() 
        comboBox.addItem("-------",0)
        comboBox.addItem("ALTA","ALTA")
        comboBox.addItem("MEDIA","MEDIA")
        comboBox.addItem("BAJA","BAJA")