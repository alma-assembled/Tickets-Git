from Models.departamentosModel import BaseDepartamentos, ModelDepartamento


class ControllerComun:
    def __init__(self):
     pass   

    def llenarCbDepartameto(self, comboBox):
        '''
        Llenar el combo box: departamentos
        '''
        self.model =ModelDepartamento()
        departamentos_list =  self.model.baseDepartamentosAll()

        for fila in departamentos_list:
            departamento = BaseDepartamentos(fila[0],fila[1])
            comboBox.addItem(departamento.departemanto) 

   