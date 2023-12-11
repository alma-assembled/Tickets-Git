import pymysql
import Models.connection as cn

class BaseCategorias:
    def __init__(self, idCategoria, categoria) :
        self.idCategoria= idCategoria
        self.categoria = categoria

class ModelCategoria:

    def baseCategoriasAll(self):
        self.c = cn.DataBase()
        try:  
          x="SELECT ID_BTICKETCATEGORIAS, DESCRIPCION FROM OPS.Base_Tickets_Categorias where activo=1;"
          self.c.cursor.execute(x)
          self.c.connection.commit()
          r=self.c.cursor.fetchall()
          return r
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()