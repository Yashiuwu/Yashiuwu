import pyodbc 

server = "localhost"
database = "tienda_jose"
usr_name = "sa"
usr_password = "2508@yuudai$"
     
#es utulizado para realizar la conexion al servidor de base de datos
conexion = pyodbc.connect('DRIVER={python3-pyodbc};SERVER='+server+';DATABASE='+database+';UID='+usr_name+';PWD'+usr_password)
cursor = conexion.cursor() 


nombre = str(input("Nombre del articulo: "))

precio = int(input("Precio: "))

codigo = float(input("Codigo: "))

#Sample insert query
count = cursor.execute("""
INSERT INTO ARTICULOS (NOMBRE, PRECIO, CODIGO) 
VALUES (?,?,?)""",
'SQL Server Express New 20', 'SQLEXPRESS New 20', 0, 0, nombre, precio, codigo).rowcount
conexion.commit()
print('Rows inserted: ' + str(count))