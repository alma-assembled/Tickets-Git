import pymysql
import Models.connection as cn

class BaseTicket:
    def __init__(self, ID_RHCATDEPARTAMENTOS, departamento) :
        self.idDepartamento= ID_RHCATDEPARTAMENTOS
        self.departemanto = departamento

class ModelTickets:
    
    def guardarTicket(self, asunto, descripcion, folio, prioridad, fecha_Creacion, id_ticket_categoria, id_departameto, id_empleado):
        self.c = cn.DataBase()
        x="INSERT INTO `OPS`.`Base_Ticket` (`ASUNTO`, `DESCRIPCION`, `FOLIO`, `PRIORIDAD`, `FECHA_CREACION`,  `ID_BTICKETCATEGORIAS`, `ID_RHCDEPARTAMENTO`, `ID_CEMPLEADO`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        v=(str(asunto),str(descripcion),str(folio),str(prioridad), str(fecha_Creacion),id_ticket_categoria, id_departameto, id_empleado)
        try:
            self.c.cursor.execute(x,v)
            self.c.connection.commit()
            #obtener el id registrado
            id_ticket = self.c.cursor.lastrowid
            return id_ticket
        except pymysql.Error as e:
            print("Error: ", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def guardarLineaTiempo(self, status, fecha, idTicket, idEmpledo):
        self.c = cn.DataBase()
        x="INSERT INTO `OPS`.`Base_Ticket_Linea_Tiempo` (`STATUS`, `FECHA`, `ID_BTICKET`, `ID_CEMPLEADO`) VALUES (%s, %s, %s, %s);"
        v=(str(status),str(fecha),idTicket, idEmpledo)
        try:
            self.c.cursor.execute(x,v)
            self.c.connection.commit()
            #obtener el id registrado
            id = self.c.cursor.lastrowid
            return id
        except pymysql.Error as e:
            print("Error: ", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()
