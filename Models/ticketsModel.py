import pymysql
import Models.connection as cn


class BaseTicket:
    def __init__(self, id_rhcatdepartamentos, departamento):
        self.id_departamento = id_rhcatdepartamentos
        self.departemanto = departamento


class ModelTickets:
    def __init__(self):
        self.c = cn.DataBase()
        pass

    def guardar_ticket(self, asunto, descripcion, prioridad, fecha_creacion, id_ticket_categoria, id_departameto,
                       id_empleado,id_folio):
        self.c = cn.DataBase()
        x = ("INSERT INTO `OPS`.`Base_Ticket` (`ASUNTO`, `DESCRIPCION`, `PRIORIDAD`, `FECHA_CREACION`,"
             " `ID_BTICKETCATEGORIAS`, `ID_RHCDEPARTAMENTO`, `ID_CEMPLEADO`,`ID_BTICKETFOLIO`) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s);")
        v = (str(asunto), str(descripcion), str(prioridad), str(fecha_creacion), id_ticket_categoria,
             id_departameto, id_empleado, id_folio)
        try:
            self.c.cursor.execute(x, v)
            self.c.connection.commit()
            # obtener el id registrado
            id_ticket = self.c.cursor.lastrowid
            return id_ticket
        except pymysql.Error as e:
            print("Error: ", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def guardar_lineatiempo(self, status, fecha, idticket, idempledo):
        self.c = cn.DataBase()
        x = ("INSERT INTO `OPS`.`Base_Ticket_Linea_Tiempo` (`STATUS`, `FECHA`, `ID_BTICKET`,"
             " `ID_CEMPLEADO`) VALUES (%s, %s, %s, %s);")
        v = (str(status), str(fecha), idticket, idempledo)
        try:
            self.c.cursor.execute(x, v)
            self.c.connection.commit()
            # obtener el id registrado
            _id = self.c.cursor.lastrowid
            return _id
        except pymysql.Error as e:
            print("Error: ", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()
