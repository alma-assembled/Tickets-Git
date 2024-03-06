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
                       id_empleado, id_folio, folio):
        self.c = cn.DataBase()
        x = ("INSERT INTO `OPS`.`Base_Ticket` (`ASUNTO`, `DESCRIPCION`, `PRIORIDAD`, `FECHA_CREACION`,"
             " `ID_BTICKETCATEGORIAS`, `ID_RHCDEPARTAMENTO`, `ID_CEMPLEADO`,`ID_BTICKETFOLIO`, `FOLIO`) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s );")
        v = (str(asunto), str(descripcion), str(prioridad), str(fecha_creacion), id_ticket_categoria,
             id_departameto, id_empleado, id_folio, str(folio))
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

    def select_tickets_dashboard_solicitante(self, id_empleado_solicitante):
        self.c = cn.DataBase()
        try:
            x = f"""
                SELECT *
                FROM (
                    SELECT DISTINCT
                        BT.ID_BTICKET,
                        F.ID_BTICKETFOLIO AS FOLIO,
                        BT.FECHA_CREACION AS FECHA,
                        BT.ASUNTO AS TITULO,
                        D.DEPARTAMENTO,
                        CE.NOMBRE AS RESPONSABLE,
                        BT.PRIORIDAD,
                        MAX(CASE WHEN LTT.FECHA = (SELECT MAX(FECHA) FROM Base_Ticket_Linea_Tiempo WHERE ID_BTICKET = BT.ID_BTICKET) THEN LTT.STATUS END) AS ULTIMO_STATUS
                    FROM OPS.Base_Ticket BT
                    INNER JOIN OPS.Base_Ticket_Folios F ON BT.ID_BTICKETFOLIO = F.ID_BTICKETFOLIO
                    INNER JOIN OPS.RH_Cat_Departamentos D ON F.ID_RHCDEPARTAMENTO = D.ID_RHCDEPARTAMENTO
                    INNER JOIN OPS.Base_Tickets_Categorias CA ON BT.ID_BTICKETCATEGORIAS = CA.ID_BTICKETCATEGORIAS
                    INNER JOIN OPS.Base_Ticket_Linea_Tiempo LTT ON BT.ID_BTICKET = LTT.ID_BTICKET 
                    INNER JOIN OPS.Catalogo_Empleados CE ON  LTT.ID_CEMPLEADO = CE.ID_CEMPLEADO
                    WHERE BT.ACTIVO = 1
                    AND LTT.ACTIVO = 1 
                    AND BT.ID_CEMPLEADO = {id_empleado_solicitante}
                    AND LTT.STATUS NOT IN ('CERRADO', 'CANCELADO')
                    GROUP BY BT.ID_BTICKET , F.ID_BTICKETFOLIO, BT.FECHA_CREACION, BT.ASUNTO, D.DEPARTAMENTO, CE.NOMBRE, BT.PRIORIDAD
                ) AS subquery
                WHERE ULTIMO_STATUS IS NOT NULL
                ORDER BY FECHA DESC;
                """

            self.c.cursor.execute(x)
            self.c.connection.commit()
            r = self.c.cursor.fetchall()
            return r
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def select_tickets_dashboard_responsable(self, id_empleado_responsable):
        self.c = cn.DataBase()
        try:
            x = f"""SELECT *
                    FROM (
                        SELECT DISTINCT
                            BT.ID_BTICKET,
                            F.ID_BTICKETFOLIO AS FOLIO,
                            BT.FECHA_CREACION AS FECHA,
                            BT.ASUNTO AS TITULO,
                            D.DEPARTAMENTO,
                            CE.NOMBRE AS RESPONSABLE,
                            BT.PRIORIDAD,
                            MAX(CASE WHEN LTT.FECHA = (SELECT MAX(FECHA) FROM Base_Ticket_Linea_Tiempo WHERE ID_BTICKET = BT.ID_BTICKET) THEN LTT.STATUS END) AS ULTIMO_STATUS
                        FROM OPS.Base_Ticket BT
                        INNER JOIN OPS.Base_Ticket_Folios F ON BT.ID_BTICKETFOLIO = F.ID_BTICKETFOLIO
                        INNER JOIN OPS.RH_Cat_Departamentos D ON F.ID_RHCDEPARTAMENTO = D.ID_RHCDEPARTAMENTO
                        INNER JOIN OPS.Base_Tickets_Categorias CA ON BT.ID_BTICKETCATEGORIAS = CA.ID_BTICKETCATEGORIAS
                        INNER JOIN OPS.Catalogo_Empleados CE ON BT.ID_CEMPLEADO = CE.ID_CEMPLEADO
                        INNER JOIN OPS.Base_Ticket_Linea_Tiempo LTT ON BT.ID_BTICKET = LTT.ID_BTICKET 
                        WHERE BT.ACTIVO = 1
                        AND LTT.ACTIVO = 1 
                        AND LTT.ID_CEMPLEADO = {id_empleado_responsable}
                        AND LTT.STATUS NOT IN ('CERRADO', 'CANCELADO')
                        GROUP BY BT.ID_BTICKET , F.ID_BTICKETFOLIO, BT.FECHA_CREACION, BT.ASUNTO, D.DEPARTAMENTO, CE.NOMBRE, BT.PRIORIDAD
                    ) AS subquery
                    WHERE ULTIMO_STATUS IS NOT NULL
                    ORDER BY FECHA DESC;
                    """

            self.c.cursor.execute(x)
            self.c.connection.commit()
            r = self.c.cursor.fetchall()
            return r
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def select_tickets_mis_tickets_solicitante(self, id_empleado_solicitante):
            self.c = cn.DataBase()
            try:
                x = f"""
                    SELECT *
                    FROM (
                       SELECT DISTINCT
                                BT.ID_BTICKET,
                                F.ID_BTICKETFOLIO AS FOLIO,
                                BT.FECHA_CREACION AS FECHA,
                                BT.ASUNTO AS TITULO,
                                D.DEPARTAMENTO,
                                CE.NOMBRE AS RESPONSABLE,
                                BT.PRIORIDAD,
                                MAX(CASE WHEN LTT.FECHA = (SELECT MAX(FECHA) FROM Base_Ticket_Linea_Tiempo WHERE ID_BTICKET = BT.ID_BTICKET) THEN LTT.STATUS END) AS ULTIMO_STATUS
                            FROM OPS.Base_Ticket BT
                            INNER JOIN OPS.Base_Ticket_Folios F ON BT.ID_BTICKETFOLIO = F.ID_BTICKETFOLIO
                            INNER JOIN OPS.RH_Cat_Departamentos D ON F.ID_RHCDEPARTAMENTO = D.ID_RHCDEPARTAMENTO
                            INNER JOIN OPS.Base_Tickets_Categorias CA ON BT.ID_BTICKETCATEGORIAS = CA.ID_BTICKETCATEGORIAS
                            INNER JOIN OPS.Base_Ticket_Linea_Tiempo LTT ON BT.ID_BTICKET = LTT.ID_BTICKET 
				    		INNER JOIN OPS.Catalogo_Empleados CE ON  LTT.ID_CEMPLEADO = CE.ID_CEMPLEADO
                            WHERE BT.ACTIVO = 1
                            AND LTT.ACTIVO = 1 
                            AND BT.ID_CEMPLEADO = {id_empleado_solicitante}
                            GROUP BY BT.ID_BTICKET , F.ID_BTICKETFOLIO, BT.FECHA_CREACION, BT.ASUNTO, D.DEPARTAMENTO, CE.NOMBRE, BT.PRIORIDAD
                    ) AS subquery
                    WHERE ULTIMO_STATUS IS NOT NULL
                    ORDER BY FECHA DESC;"""

                self.c.cursor.execute(x)
                self.c.connection.commit()
                r = self.c.cursor.fetchall()
                return r
            except pymysql.Error as e:
                print("Error:", e)
            finally:
                if hasattr(self, 'c'):
                    self.c.cursor.close()

    def select_tickets_mis_tickets_responsable(self, id_empleado_responsable):
        self.c = cn.DataBase()
        try:
            x = f"""
             SELECT *
                    FROM (
                SELECT DISTINCT
                    BT.ID_BTICKET,
                    F.ID_BTICKETFOLIO AS FOLIO,
                    BT.FECHA_CREACION AS FECHA,
                    BT.ASUNTO AS TITULO,
                    D.DEPARTAMENTO,
                    CE.NOMBRE AS RESPONSABLE,
                    BT.PRIORIDAD,
                    MAX(CASE WHEN LTT.FECHA = (SELECT MAX(FECHA) FROM Base_Ticket_Linea_Tiempo WHERE ID_BTICKET = BT.ID_BTICKET) THEN LTT.STATUS END) AS ULTIMO_STATUS
                FROM OPS.Base_Ticket BT
                INNER JOIN OPS.Base_Ticket_Folios F ON BT.ID_BTICKETFOLIO = F.ID_BTICKETFOLIO
                INNER JOIN OPS.RH_Cat_Departamentos D ON F.ID_RHCDEPARTAMENTO = D.ID_RHCDEPARTAMENTO
                INNER JOIN OPS.Base_Tickets_Categorias CA ON BT.ID_BTICKETCATEGORIAS = CA.ID_BTICKETCATEGORIAS
                INNER JOIN OPS.Catalogo_Empleados CE ON BT.ID_CEMPLEADO = CE.ID_CEMPLEADO
                INNER JOIN OPS.Base_Ticket_Linea_Tiempo LTT ON      BT.ID_BTICKET = LTT.ID_BTICKET 
                WHERE BT.ACTIVO = 1
                AND LTT.ACTIVO = 1 
                AND LTT.ID_CEMPLEADO = {id_empleado_responsable}
                GROUP BY BT.ID_BTICKET , F.ID_BTICKETFOLIO, BT.FECHA_CREACION, BT.ASUNTO, D.DEPARTAMENTO, CE.NOMBRE, BT.PRIORIDAD
                 ) AS subquery
                    WHERE ULTIMO_STATUS IS NOT NULL
                    ORDER BY FECHA DESC;"""

            self.c.cursor.execute(x)
            self.c.connection.commit()
            r = self.c.cursor.fetchall()
            return r
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()
 
    def select_ticket_resumen_by_id(self, id_ticket):
        self.c = cn.DataBase()
        try:
            x = f"""SELECT DISTINCT
                    BT.ID_BTICKET, 
                    F.ID_BTICKETFOLIO AS FOLIO,
                    LT.FECHA AS FECHA,
                    BT.ASUNTO AS TITULO, 
                    D.DEPARTAMENTO,
                    (SELECT NOMBRE 
                    FROM OPS.Catalogo_Empleados 
                    where ID_CEMPLEADO = LT.ID_CEMPLEADO) AS RESPONSABLE,
                    BT.PRIORIDAD, 
                    (SELECT STATUS 
                        FROM OPS.Base_Ticket_Linea_Tiempo LT2
                        WHERE LT2.ID_BTICKET = BT.ID_BTICKET AND LT2.ACTIVO = 1
                        ORDER BY LT2.FECHA  DESC
                        LIMIT 1 ) AS ULTIMO_STATUS,
                    COALESCE( BT.FECHA_SOLUCION, 'ASIGNA UNA FECHA') AS FECHA_SOLUCION
                    FROM 
                    OPS.RH_Cat_Departamentos D,
                    OPS.Base_Ticket_Folios F ,
                    OPS.Base_Tickets_Categorias CA,
                    OPS.Base_Ticket BT, 
                    OPS.Catalogo_Empleados EM,
                    OPS.Base_Ticket_Linea_Tiempo LT
                    WHERE 
                    LT.ACTIVO = 1
                    AND BT.ID_BTICKETFOLIO = F.ID_BTICKETFOLIO 
                    AND F.ID_RHCDEPARTAMENTO = D.ID_RHCDEPARTAMENTO 
                    AND BT.ID_BTICKETCATEGORIAS = CA.ID_BTICKETCATEGORIAS 
                    AND BT.ID_CEMPLEADO=EM.ID_CEMPLEADO 
                    AND BT.ID_BTICKET =  {id_ticket}
                    AND BT.ID_BTICKET = LT.ID_BTICKET ORDER BY LT.FECHA DESC LIMIT 1;"""

            self.c.cursor.execute(x)
            self.c.connection.commit()
            r = self.c.cursor.fetchone()
            return r
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def select_ticket_detalles_by_id(self, id_ticket):
        self.c = cn.DataBase()
        try:
            x = f"""SELECT DISTINCT
                BT.ID_BTICKET, 
                F.ID_BTICKETFOLIO AS FOLIO,
                LT.FECHA AS FECHA,
                 BT.ASUNTO AS TITULO, 
                 BT.DESCRIPCION ,
                 D.DEPARTAMENTO,
                 CA.DESCRIPCION AS CATEGORIA,
                  (SELECT NOMBRE 
                 FROM OPS.Catalogo_Empleados 
                 where ID_CEMPLEADO = LT.ID_CEMPLEADO) AS RESPONSABLE,
                 EM.NOMBRE AS AUTOR,
                 BT.PRIORIDAD, 
                COALESCE( BT.FECHA_SOLUCION, 'ASIGNA UNA FECHA') AS FECHA_SOLUCION,
                (SELECT STATUS 
                     FROM OPS.Base_Ticket_Linea_Tiempo LT2
                     WHERE LT2.ID_BTICKET = BT.ID_BTICKET  AND LT2.ACTIVO = 1
                     ORDER BY LT2.FECHA  DESC
                     LIMIT 1 ) AS ULTIMO_STATUS
                FROM 
                OPS.RH_Cat_Departamentos D,
                 OPS.Base_Ticket_Folios F ,
                 OPS.Base_Tickets_Categorias CA,
                 OPS.Base_Ticket BT, 
                 OPS.Catalogo_Empleados EM,
                 OPS.Base_Ticket_Linea_Tiempo LT
                WHERE 
                LT.ACTIVO = 1
                AND BT.ID_BTICKETFOLIO = F.ID_BTICKETFOLIO 
                AND F.ID_RHCDEPARTAMENTO = D.ID_RHCDEPARTAMENTO 
                AND BT.ID_BTICKETCATEGORIAS = CA.ID_BTICKETCATEGORIAS 
                AND BT.ID_CEMPLEADO=EM.ID_CEMPLEADO 
                AND BT.ID_BTICKET = {id_ticket}         
                AND BT.ID_BTICKET = LT.ID_BTICKET ORDER BY LT.FECHA DESC  LIMIT 1;"""

            self.c.cursor.execute(x)
            self.c.connection.commit()
            r = self.c.cursor.fetchone()
            return r
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def asignarFechaSolucion(self, fecha, id_ticket):
            self.c = cn.DataBase()
            x=f'''UPDATE `OPS`.`Base_Ticket` SET `FECHA_SOLUCION` = '{fecha}' WHERE (`ID_BTICKET` = '{id_ticket}');'''
            try:
                self.c.cursor.execute(x)
                self.c.connection.commit()
            except pymysql.Error as e: 
                print("Error: ", e)
            finally:
                if hasattr(self, 'c'):
                    self.c.cursor.close()

    def asignarFechaTermino(self, fecha, id_ticket):
            self.c = cn.DataBase()
            x=f'''UPDATE `OPS`.`Base_Ticket` SET `FECHA_TERMINO` = '{fecha}' WHERE (`ID_BTICKET` = '{id_ticket}');'''
            try:
                self.c.cursor.execute(x)
                self.c.connection.commit()
            except pymysql.Error as e: 
                print("Error: ", e)
            finally:
                if hasattr(self, 'c'):
                    self.c.cursor.close()

    def ticket_id_empleado_responsable(self, id_ticket):
        self.c = cn.DataBase()
        try:
            x=f'''SELECT  L.ID_CEMPLEADO FROM OPS.Base_Ticket_Linea_Tiempo L WHERE L.ID_BTICKET = {id_ticket} ORDER BY  L.FECHA  LIMIT 1;'''
            self.c.cursor.execute(x)
            self.c.connection.commit()
            r = self.c.cursor.fetchone()
            return r
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def asignarFechaCierre(self, fecha, id_ticket):
            self.c = cn.DataBase()
            x=f'''UPDATE `OPS`.`Base_Ticket` SET `FECHA_CIERRE` = '{fecha}' WHERE (`ID_BTICKET` = '{id_ticket}');'''
            try:
                self.c.cursor.execute(x)
                self.c.connection.commit()
            except pymysql.Error as e: 
                print("Error: ", e)
            finally:
                if hasattr(self, 'c'):
                    self.c.cursor.close()


    def count_estado_solicitante(self, id_empleado_solicitante, estado):
        self.c = cn.DataBase()
        try:
            x = f"""SELECT COUNT(*) AS total
                    FROM (
                        SELECT
                            LTT.ID_BTICKET,
                            MAX(CASE WHEN LTT.FECHA = (SELECT MAX(FECHA) FROM Base_Ticket_Linea_Tiempo WHERE BT.ID_BTICKET = ID_BTICKET)THEN LTT.STATUS END) AS ULTIMO_STATUS
                        FROM OPS.Base_Ticket_Linea_Tiempo LTT ,
                        OPS.Base_Ticket BT
                        WHERE
                            LTT.ACTIVO = 1 
                            AND BT.ACTIVO = TRUE
                            AND BT.ID_BTICKET = LTT.ID_BTICKET
                            AND BT.ID_CEMPLEADO = {id_empleado_solicitante}
                            AND LTT.STATUS = '{estado}'
                        GROUP BY LTT.ID_BTICKET
                    ) AS subquery 	
                    WHERE ULTIMO_STATUS IS NOT NULL;"""

            self.c.cursor.execute(x)
            self.c.connection.commit()
            r = self.c.cursor.fetchone()
            return r
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()
     
    def count_estado_responsable(self, id_empleado_responsable, estado):
        self.c = cn.DataBase()
        try:
            x = f"""SELECT COUNT(*) AS total
                    FROM (
                        SELECT
                            LTT.ID_BTICKET,
                            MAX(CASE WHEN LTT.FECHA = (SELECT MAX(FECHA) FROM Base_Ticket_Linea_Tiempo WHERE ID_BTICKET = LTT.ID_BTICKET)THEN LTT.STATUS END) AS ULTIMO_STATUS
                        FROM OPS.Base_Ticket_Linea_Tiempo LTT 
                        WHERE
                            LTT.ACTIVO = 1 
                            AND LTT.ID_CEMPLEADO = {id_empleado_responsable}
                            AND LTT.STATUS = '{estado}' 
                        GROUP BY LTT.ID_BTICKET
                    ) AS subquery
                    WHERE ULTIMO_STATUS IS NOT NULL;"""

            self.c.cursor.execute(x)
            self.c.connection.commit()
            r = self.c.cursor.fetchone()
            return r
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()
     

    def select_tickets_dashboard_solicitante_filtro(self, folio, id_empleado_solicitante, status, id_empleado_responsable, id_departamento,id_ticket_categoria, fecha ):
            self.c = cn.DataBase()
            try:
                x = f"""SELECT *
                FROM (
                    SELECT DISTINCT
                        BT.ID_BTICKET,
                        F.ID_BTICKETFOLIO AS FOLIO,
                        BT.FECHA_CREACION AS FECHA,
                        BT.ASUNTO AS TITULO,
                        D.DEPARTAMENTO,
                        CE.NOMBRE AS RESPONSABLE,
                        BT.PRIORIDAD,
                        MAX(CASE WHEN LTT.FECHA = (SELECT MAX(FECHA) FROM Base_Ticket_Linea_Tiempo WHERE ID_BTICKET = BT.ID_BTICKET) THEN LTT.STATUS END) AS ULTIMO_STATUS
                    FROM OPS.Base_Ticket BT
                    INNER JOIN OPS.Base_Ticket_Folios F ON BT.ID_BTICKETFOLIO = F.ID_BTICKETFOLIO
                    INNER JOIN OPS.RH_Cat_Departamentos D ON F.ID_RHCDEPARTAMENTO = D.ID_RHCDEPARTAMENTO
                    INNER JOIN OPS.Base_Tickets_Categorias CA ON BT.ID_BTICKETCATEGORIAS = CA.ID_BTICKETCATEGORIAS
                    INNER JOIN OPS.Base_Ticket_Linea_Tiempo LTT ON BT.ID_BTICKET = LTT.ID_BTICKET 
                    INNER JOIN OPS.Catalogo_Empleados CE ON  LTT.ID_CEMPLEADO = CE.ID_CEMPLEADO
                    WHERE BT.ACTIVO = 1
                    AND LTT.ACTIVO = 1 
                    AND BT.ID_CEMPLEADO = {id_empleado_solicitante}
                        """

                if fecha != "XXXX-XX-XX":
                        x+=f"AND DATE(BT.FECHA_CREACION) = '{fecha}'"

                if folio != "":
                        x+=f"AND BT.FOLIO LIKE '{folio}%'"

                if status != 0:
                    x += f" AND LTT.STATUS = '{status}' "
                
                if id_empleado_responsable != 0:
                    x += f"AND LTT.ID_CEMPLEADO = {id_empleado_responsable} "

                if id_departamento != 0 : 
                    
                    x += f" AND D.ID_RHCDEPARTAMENTO = {id_departamento} "
                
                if id_ticket_categoria != 0:
                    x += f" AND CA.ID_BTICKETCATEGORIAS  = {id_ticket_categoria} "
                x += """
                    AND LTT.STATUS NOT IN ('CERRADO', 'CANCELADO')
                    GROUP BY BT.ID_BTICKET , F.ID_BTICKETFOLIO, BT.FECHA_CREACION, BT.ASUNTO, D.DEPARTAMENTO, CE.NOMBRE, BT.PRIORIDAD
                ) AS subquery
                WHERE ULTIMO_STATUS IS NOT NULL
                ORDER BY FECHA DESC;"""

                self.c.cursor.execute(x)
                self.c.connection.commit()
                r = self.c.cursor.fetchall()
                return r
            except pymysql.Error as e:
                print("Error:", e)
            finally:
                if hasattr(self, 'c'):
                    self.c.cursor.close()


    def select_tickets_dashboard_responsable_filtro(self,folio,  id_empleado_solicitante, status, id_empleado_responsable, id_departamento, id_ticket_categoria, fecha):
            self.c = cn.DataBase()
            try:
                x = f"""SELECT *
                    FROM (
                        SELECT DISTINCT
                            BT.ID_BTICKET,
                            F.ID_BTICKETFOLIO AS FOLIO,
                            BT.FECHA_CREACION AS FECHA,
                            BT.ASUNTO AS TITULO,
                            D.DEPARTAMENTO,
                            CE.NOMBRE AS RESPONSABLE,
                            BT.PRIORIDAD,
                            MAX(CASE WHEN LTT.FECHA = (SELECT MAX(FECHA) FROM Base_Ticket_Linea_Tiempo WHERE ID_BTICKET = BT.ID_BTICKET) THEN LTT.STATUS END) AS ULTIMO_STATUS
                        FROM OPS.Base_Ticket BT
                        INNER JOIN OPS.Base_Ticket_Folios F ON BT.ID_BTICKETFOLIO = F.ID_BTICKETFOLIO
                        INNER JOIN OPS.RH_Cat_Departamentos D ON F.ID_RHCDEPARTAMENTO = D.ID_RHCDEPARTAMENTO
                        INNER JOIN OPS.Base_Tickets_Categorias CA ON BT.ID_BTICKETCATEGORIAS = CA.ID_BTICKETCATEGORIAS
                        INNER JOIN OPS.Catalogo_Empleados CE ON BT.ID_CEMPLEADO = CE.ID_CEMPLEADO
                        INNER JOIN OPS.Base_Ticket_Linea_Tiempo LTT ON BT.ID_BTICKET = LTT.ID_BTICKET 
                        WHERE BT.ACTIVO = 1
                        AND LTT.ACTIVO = 1 
                        AND LTT.ID_CEMPLEADO = {id_empleado_responsable}
                        """
                if fecha != "XXXX-XX-XX":
                        x+=f"AND DATE(BT.FECHA_CREACION) = '{fecha}'"

                if folio != "":
                        x+=f"AND BT.FOLIO LIKE '{folio}%'"

                if status != 0:
                    x += f" AND LTT.STATUS = '{status}' "
                
                if id_empleado_solicitante != 0:
                    x += f"AND BT.ID_CEMPLEADO = {id_empleado_solicitante} "

                if id_departamento != 0 : 
                    x += f" AND D.ID_RHCDEPARTAMENTO = {id_departamento} "
                
                if id_ticket_categoria != 0:
                    x += f"AND CA.ID_BTICKETCATEGORIAS  = {id_ticket_categoria} "

                x += """ AND LTT.STATUS NOT IN ('CERRADO', 'CANCELADO')
                        GROUP BY BT.ID_BTICKET , F.ID_BTICKETFOLIO, BT.FECHA_CREACION, BT.ASUNTO, D.DEPARTAMENTO, CE.NOMBRE, BT.PRIORIDAD
                    ) AS subquery
                    WHERE ULTIMO_STATUS IS NOT NULL
                    ORDER BY FECHA DESC; """

                self.c.cursor.execute(x)
                self.c.connection.commit()
                r = self.c.cursor.fetchall()
                return r
            except pymysql.Error as e:
                print("Error:", e)
            finally:
                if hasattr(self, 'c'):
                    self.c.cursor.close()

    def filtro_select_tickets_mis_tickets_solicitante(self, folio, id_empleado_solicitante,status, id_empleado_responsable, id_departamento,id_ticket_categoria, fecha):
                self.c = cn.DataBase()
                try:
                    x = f"""
                        SELECT *
                        FROM (
                        SELECT DISTINCT
                                    BT.ID_BTICKET,
                                    F.ID_BTICKETFOLIO AS FOLIO,
                                    BT.FECHA_CREACION AS FECHA,
                                    BT.ASUNTO AS TITULO,
                                    D.DEPARTAMENTO,
                                    CE.NOMBRE AS RESPONSABLE,
                                    BT.PRIORIDAD,
                                    MAX(CASE WHEN LTT.FECHA = (SELECT MAX(FECHA) FROM Base_Ticket_Linea_Tiempo WHERE ID_BTICKET = BT.ID_BTICKET) THEN LTT.STATUS END) AS ULTIMO_STATUS
                                FROM OPS.Base_Ticket BT
                                INNER JOIN OPS.Base_Ticket_Folios F ON BT.ID_BTICKETFOLIO = F.ID_BTICKETFOLIO
                                INNER JOIN OPS.RH_Cat_Departamentos D ON F.ID_RHCDEPARTAMENTO = D.ID_RHCDEPARTAMENTO
                                INNER JOIN OPS.Base_Tickets_Categorias CA ON BT.ID_BTICKETCATEGORIAS = CA.ID_BTICKETCATEGORIAS
                                INNER JOIN OPS.Base_Ticket_Linea_Tiempo LTT ON BT.ID_BTICKET = LTT.ID_BTICKET 
                                INNER JOIN OPS.Catalogo_Empleados CE ON  LTT.ID_CEMPLEADO = CE.ID_CEMPLEADO
                                WHERE BT.ACTIVO = 1
                                AND LTT.ACTIVO = 1 
                                AND BT.ID_CEMPLEADO = {id_empleado_solicitante}"""
                
                    if fecha != "XXXX-XX-XX":
                        x+=f" AND DATE(BT.FECHA_CREACION) = '{fecha}'"

                    if folio != "":
                        x+=f" AND BT.FOLIO LIKE '{folio}%'"

                    if status != 0:
                        x += f" AND LTT.STATUS = '{status}' "
                    
                    if id_empleado_responsable != 0:
                        x += f" AND LTT.ID_CEMPLEADO = {id_empleado_responsable} "

                    if id_departamento != 0 : 
                        x += f" AND D.ID_RHCDEPARTAMENTO = {id_departamento} "
                    
                    if id_ticket_categoria != 0:
                        x += f"AND  CA.ID_BTICKETCATEGORIAS  = {id_ticket_categoria} "

                    x += """GROUP BY BT.ID_BTICKET , F.ID_BTICKETFOLIO, BT.FECHA_CREACION, BT.ASUNTO, D.DEPARTAMENTO, CE.NOMBRE, BT.PRIORIDAD
                        ) AS subquery
                        WHERE ULTIMO_STATUS IS NOT NULL
                        ORDER BY FECHA DESC;"""

                    self.c.cursor.execute(x)
                    self.c.connection.commit()
                    r = self.c.cursor.fetchall()
                    return r
                except pymysql.Error as e:
                    print("Error:", e)
                finally:
                    if hasattr(self, 'c'):
                        self.c.cursor.close()

    def filtro_select_tickets_mis_tickets_reponsable(self, folio, id_empleado_solicitante,status, id_empleado_responsable, id_departamento,id_ticket_categoria, fecha):
                self.c = cn.DataBase()
                try:
                    x = f"""
                        SELECT *
                    FROM (
                SELECT DISTINCT
                    BT.ID_BTICKET,
                    F.ID_BTICKETFOLIO AS FOLIO,
                    BT.FECHA_CREACION AS FECHA,
                    BT.ASUNTO AS TITULO,
                    D.DEPARTAMENTO,
                    CE.NOMBRE AS RESPONSABLE,
                    BT.PRIORIDAD,
                    MAX(CASE WHEN LTT.FECHA = (SELECT MAX(FECHA) FROM Base_Ticket_Linea_Tiempo WHERE ID_BTICKET = BT.ID_BTICKET) THEN LTT.STATUS END) AS ULTIMO_STATUS
                FROM OPS.Base_Ticket BT
                INNER JOIN OPS.Base_Ticket_Folios F ON BT.ID_BTICKETFOLIO = F.ID_BTICKETFOLIO
                INNER JOIN OPS.RH_Cat_Departamentos D ON F.ID_RHCDEPARTAMENTO = D.ID_RHCDEPARTAMENTO
                INNER JOIN OPS.Base_Tickets_Categorias CA ON BT.ID_BTICKETCATEGORIAS = CA.ID_BTICKETCATEGORIAS
                INNER JOIN OPS.Catalogo_Empleados CE ON BT.ID_CEMPLEADO = CE.ID_CEMPLEADO
                INNER JOIN OPS.Base_Ticket_Linea_Tiempo LTT ON      BT.ID_BTICKET = LTT.ID_BTICKET 
                WHERE BT.ACTIVO = 1
                AND LTT.ACTIVO = 1 
                AND LTT.ID_CEMPLEADO = {id_empleado_responsable} """
                    
                    if fecha != "XXXX-XX-XX":
                        x+=f" AND DATE(BT.FECHA_CREACION) = '{fecha}'"
                    
                    if folio != "":
                        x+=f" AND BT.FOLIO LIKE '{folio}%'"

                    if status != 0:
                        x += f" AND LTT.STATUS = '{status}' "
                    
                    if id_empleado_solicitante != 0:
                        x += f" AND BT.ID_CEMPLEADO = {id_empleado_solicitante} "

                    if id_departamento != 0 : 
                        x += f" AND D.ID_RHCDEPARTAMENTO = {id_departamento} "
                    
                    if id_ticket_categoria != 0:
                        x += f" AND CA.ID_BTICKETCATEGORIAS  = {id_ticket_categoria} "

                    x += """ GROUP BY BT.ID_BTICKET , F.ID_BTICKETFOLIO, BT.FECHA_CREACION, BT.ASUNTO, D.DEPARTAMENTO, CE.NOMBRE, BT.PRIORIDAD
                 ) AS subquery
                    WHERE ULTIMO_STATUS IS NOT NULL
                    ORDER BY FECHA DESC;"""
                    print(x)
                    self.c.cursor.execute(x)
                    self.c.connection.commit()
                    r = self.c.cursor.fetchall()
                    return r
                except pymysql.Error as e:
                    print("Error:", e)
                finally:
                    if hasattr(self, 'c'):
                        self.c.cursor.close()
