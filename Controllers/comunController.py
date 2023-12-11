from Models.departamentosModel import BaseDepartamentos, ModelDepartamento
from Models.categoriasTicketsModel import BaseCategorias, ModelCategoria


class ControllerComun:
    def __init__(self):
     pass   

    def llenarCbDepartameto(self, comboBox):
        '''
        Llenar el combo box: departamentos
        '''
        model =ModelDepartamento()
        departamentos_list =  model.baseDepartamentosAll()

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

        for fila in categorias_list:
            categoria = BaseCategorias(fila[0],fila[1])
            comboBox.addItem(categoria.categoria, categoria.idCategoria)
   