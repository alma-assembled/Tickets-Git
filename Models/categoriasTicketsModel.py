import pymysql
import Models.connection as cn


class BaseCategorias:
    def __init__(self, idcategoria, categoria):
        self.idcategoria = idcategoria
        self.categoria = categoria


class ModelCategoria:

    def __init__(self):
        self.c = cn.DataBase()

    def base_categorias_by_rhdepartanmento(self, ID_RHCDEPARTAMENTO):

        self.c = cn.DataBase()
        try:
            x = f"SELECT ID_BTICKETCATEGORIAS, DESCRIPCION FROM OPS.Base_Tickets_Categorias where activo=1  AND ID_RHCDEPARTAMENTO = {ID_RHCDEPARTAMENTO};"
            self.c.cursor.execute(x)
            self.c.connection.commit()
            r = self.c.cursor.fetchall()
            return r
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()
