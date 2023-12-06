import pymysql

import Models.connection as cn
from Models.global_variables import BdUsurio

class Usuario:
    def __init__(self, user, password):
        self.user = user
        self.password = password

class ModelUser:

    def ConsultaUsuario(self, login):
        self.c = cn.DataBase()
        try:  
          x="SELECT `ID_CEMPLEADO` FROM `Catalogo_Empleados` WHERE `ACTIVO`=TRUE AND `USUARIO`='"+ login.user +"' AND `CLAVE`='"+ login.password +"';"
          self.c.cursor.execute(x)
          self.c.connection.commit()
          r=self.c.cursor.fetchone()
          self.c.cursor.close()
          if  r != None :
            BdUsurio.idEmpleado = r[0]
            return True
          else :
            return False
        except  pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def infoUsuario(self):
        self.c = cn.DataBase()
        try:  
          #x="SELECT NOMBRE, ID_RHCDEPARTAMENTO , DEPARTAMENTO FROM OPS.Catalogo_Empleados AS C_Empleados INNER JOIN OPS.RH_Cat_Departamentos  as Departamentos ON C_Empleados.ID_RHCPUESTO =  Departamentos.ID_RHCDEPARTAMENTO where  C_Empleados.ID_CEMPLEADO="+str(BdUsurio.idEmpleado)+" ;"
          x='''SELECT NOMBRE,  Departamentos.ID_RHCDEPARTAMENTO , Departamentos.DEPARTAMENTO 
                FROM OPS.Catalogo_Empleados AS C_Empleados 
                INNER JOIN  OPS.RH_Cat_Puestos as C_PUESTO   ON C_Empleados.ID_RHCPUESTO =   C_PUESTO.ID_RHCPUESTO 
                INNER JOIN OPS.RH_Cat_Departamentos  as Departamentos  ON C_PUESTO.ID_RHCDEPARTAMENTO =  Departamentos.ID_RHCDEPARTAMENTO 
                where  C_Empleados.ID_CEMPLEADO='''+str(BdUsurio.idEmpleado)+''';'''
          self.c.cursor.execute(x)
          self.c.connection.commit()
          r=self.c.cursor.fetchone()
          if  r != None :
            BdUsurio.nombre = r[0]
            BdUsurio.id_departamento = r[1]
            BdUsurio.departamento = r[2]
            return r
        except  pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()
