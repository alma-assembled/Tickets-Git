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
                       id_empleado, id_folio):
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

    def select_tickets_dasboard(self):
        self.c = cn.DataBase()
        try:
            x = """SELECT 
                BT.ID_BTICKET, 
                F.ID_BTICKETFOLIO AS FOLIO,
                BT.FECHA_CREACION AS FECHA,
                EM.NOMBRE AS AUTOR,
                 BT.ASUNTO AS TITULO, 
                 D.DEPARTAMENTO,
                 CA.DESCRIPCION  CATEGORIA,
                 BT.PRIORIDAD,
                (SELECT STATUS 
                     FROM OPS.Base_Ticket_Linea_Tiempo LT2
                     WHERE LT2.ID_BTICKET = BT.ID_BTICKET
                     ORDER BY LT2.FECHA DESC
                     LIMIT 1) AS ULTIMO_STATUS
                FROM 
                OPS.RH_Cat_Departamentos D,
                 OPS.Base_Ticket_Folios F ,
                 OPS.Base_Tickets_Categorias CA,
                 OPS.Base_Ticket BT, 
                 OPS.Catalogo_Empleados EM,
                  OPS.Base_Ticket_Linea_Tiempo LT
                WHERE 
                BT.ID_BTICKETFOLIO = F.ID_BTICKETFOLIO 
                AND F.ID_RHCDEPARTAMENTO = D.ID_RHCDEPARTAMENTO 
                AND BT.ID_BTICKETCATEGORIAS = CA.ID_BTICKETCATEGORIAS 
                AND BT.ID_CEMPLEADO = EM.ID_CEMPLEADO
                AND BT.ID_BTICKET = LT.ID_BTICKET ORDER BY BT.FECHA_CREACION DESC;"""

            self.c.cursor.execute(x)
            self.c.connection.commit()
            r = self.c.cursor.fetchall()
            return r
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def select_mis_tickets_solicitante(self, id_empleado_solicitante):
        self.c = cn.DataBase()
        try:
            x = f"""SELECT DISTINCT
                    BT.ID_BTICKET, 
                    F.ID_BTICKETFOLIO AS FOLIO,
                    BT.FECHA_CREACION AS FECHA,
                     BT.ASUNTO AS TITULO, 
                     D.DEPARTAMENTO,
                     CA.DESCRIPCION AS CATEGORIA,
                      (SELECT NOMBRE 
                     FROM OPS.Catalogo_Empleados 
                     where ID_CEMPLEADO = LT.ID_CEMPLEADO) AS RESPONSABLE,
                     BT.PRIORIDAD, 
                    (SELECT STATUS 
                         FROM OPS.Base_Ticket_Linea_Tiempo LT2
                         WHERE LT2.ID_BTICKET = BT.ID_BTICKET
                         ORDER BY LT2.FECHA DESC
                         LIMIT 1) AS ULTIMO_STATUS
                    FROM 
                    OPS.RH_Cat_Departamentos D,
                     OPS.Base_Ticket_Folios F ,
                     OPS.Base_Tickets_Categorias CA,
                     OPS.Base_Ticket BT, 
                     OPS.Catalogo_Empleados EM,
                     OPS.Base_Ticket_Linea_Tiempo LT
                    WHERE 
                    BT.ID_BTICKETFOLIO = F.ID_BTICKETFOLIO 
                    AND F.ID_RHCDEPARTAMENTO = D.ID_RHCDEPARTAMENTO 
                    AND BT.ID_BTICKETCATEGORIAS = CA.ID_BTICKETCATEGORIAS 
                    AND BT.ID_CEMPLEADO={id_empleado_solicitante}
                    AND BT.ID_CEMPLEADO=EM.ID_CEMPLEADO 
                    AND BT.ID_BTICKET = LT.ID_BTICKET;"""

            self.c.cursor.execute(x)
            self.c.connection.commit()
            r = self.c.cursor.fetchall()
            return r
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def select_mis_tickets_responsable(self, id_empleado_responsable):
        self.c = cn.DataBase()
        try:
            x = f"""SELECT  DISTINCT
                    BT.ID_BTICKET, 
                    F.ID_BTICKETFOLIO AS FOLIO,
                    BT.FECHA_CREACION AS FECHA,
                    EM.NOMBRE AS AUTOR,
                     BT.ASUNTO AS TITULO, 
                     D.DEPARTAMENTO,
                     CA.DESCRIPCION,
                     BT.PRIORIDAD,
                    (SELECT STATUS 
                         FROM OPS.Base_Ticket_Linea_Tiempo LT2
                         WHERE LT2.ID_BTICKET = BT.ID_BTICKET
                         ORDER BY LT2.FECHA DESC
                         LIMIT 1) AS ULTIMO_STATUS
                    FROM 
                    OPS.RH_Cat_Departamentos D,
                     OPS.Base_Ticket_Folios F ,
                     OPS.Base_Tickets_Categorias CA,
                     OPS.Base_Ticket BT, 
                     OPS.Catalogo_Empleados EM,
                     OPS.Base_Ticket_Linea_Tiempo LT
                    WHERE 
                    BT.ID_BTICKETFOLIO = F.ID_BTICKETFOLIO 
                        AND F.ID_RHCDEPARTAMENTO = D.ID_RHCDEPARTAMENTO 
                        AND BT.ID_BTICKETCATEGORIAS = CA.ID_BTICKETCATEGORIAS 
                        AND BT.ID_CEMPLEADO = EM.ID_CEMPLEADO
                        AND BT.ID_BTICKET = LT.ID_BTICKET
                        AND LT.ID_CEMPLEADO = {id_empleado_responsable} ;"""

            self.c.cursor.execute(x)
            self.c.connection.commit()
            r = self.c.cursor.fetchall()
            return r
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()
