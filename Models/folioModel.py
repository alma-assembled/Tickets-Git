import pymysql
import Models.connection as cn


class ModelFolio:
    def __init__(self):
        self.c = cn.DataBase()
        pass

    def create_folio(self, numero, id_rhdepartamento):
        """
        :param numero:numero consecutivo
        :param id_rhdepartamento: id departameto
        :return: id_folio recien creado
        """
        self.c = cn.DataBase()
        x = ("INSERT INTO `OPS`.`Base_Ticket_Folios` (`FOLIO`, `ID_RHCDEPARTAMENTO`) "
             "VALUES (%s, %s);")
        v = (numero, id_rhdepartamento)
        try:
            self.c.cursor.execute(x, v)
            self.c.connection.commit()
            # obtener el id registrado
            _id_folio = self.c.cursor.lastrowid
            return _id_folio
        except pymysql.Error as e:
            print("Error: ", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def generar_numero_foliodepartamento(self, id_rhdepartamento):
        """
        :param id_rhdepartamento:
        :return: numero consecutivo ticket
        """
        self.c = cn.DataBase()
        try:
            x = ("SELECT FOLIO FROM OPS.Base_Ticket_Folios where ID_RHCDEPARTAMENTO=" +str(id_rhdepartamento) + " AND"
                 " ACTIVO=1  ORDER BY ID_BTICKETFOLIO   DESC LIMIT 1; ")
            self.c.cursor.execute(x)
            self.c.connection.commit()
            r = self.c.cursor.fetchone()
            if r is not None:

                return int(r[0]) + 1
            else:
                print("000001")
                return 1
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def obtener_folio_byid(self, id_ticket):
        """
        :param id_ticket: id_folio
        :return:  folio generardo apartir de la id_folio
        """
        self.c = cn.DataBase()
        try:
            x = ("SELECT D.CLAVE,  F.FOLIO AS FOLIO FROM OPS.RH_Cat_Departamentos D, OPS.Base_Ticket_Folios F WHERE "
                 "F.ID_BTICKETFOLIO = "+str(id_ticket) + " AND F.ID_RHCDEPARTAMENTO = D.ID_RHCDEPARTAMENTO;")
            self.c.cursor.execute(x)
            self.c.connection.commit()
            r = self.c.cursor.fetchone()
            if r is not None:
                clave = r[0]
                numero = str(r[1])

                if len(numero) < 5:
                    contador = 5 - len(numero)
                    n = ""
                    for _ in range(contador):
                        n += "0"
                    numero = n + numero
                return clave + numero
            else:
                return "FOLIO NO GENERADO"
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()
