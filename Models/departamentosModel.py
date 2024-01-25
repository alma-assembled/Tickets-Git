import pymysql
import Models.connection as cn


class BaseDepartamentos:
    def __init__(self, id_rhcatdepartamentos, departamento):
        self.id_departamento = id_rhcatdepartamentos
        self.departemanto = departamento


class ModelDepartamento:
    def __init__(self):
        self.c = cn.DataBase()
        pass

    def base_departamentosall(self):
        self.c = cn.DataBase()
        try:
            x = ("SELECT ID_RHCDEPARTAMENTO, DEPARTAMENTO, CLAVE  FROM OPS.RH_Cat_Departamentos where activo= 1 "
                 " and ID_RHCDEPARTAMENTO = 4 or ID_RHCDEPARTAMENTO= 15 order by DEPARTAMENTO;")
            self.c.cursor.execute(x)
            self.c.connection.commit()
            r = self.c.cursor.fetchall()
            return r
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def base_departamentos_by_name(self, txt_departamento):
        self.c = cn.DataBase()
        try:  
            x = ("SELECT ID_RHCDEPARTAMENTO FROM OPS.RH_Cat_Departamentos where DEPARTAMENTO="
                 "'") + txt_departamento + "' AND  activo= 1 ;"
            self.c.cursor.execute(x)
            self.c.connection.commit()
            r = self.c.cursor.fetchone()
            return r
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()
                