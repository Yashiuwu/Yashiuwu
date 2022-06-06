import pyodbc

class Articulos:

    def abrir(self):
        server = "localhost"
        database = "tienda_jose"
        usr_name = "sa"
        usr_password = "2508@yuudai$"
        
        #es utulizado para realizar la conexion al servidor de base de datos
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+usr_name+';PWD'+usr_password)
        cursor = conexion.cursor() 

    
    def alta(self, datos):
        cursor.execute(""" """)

    def consulta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select description, precio from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select codigo, description, precio from articulos"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
