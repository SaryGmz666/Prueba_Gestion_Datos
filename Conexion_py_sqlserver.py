import pyodbc

try: 
    conexion=pyodbc.connect('DRIVER={SQL Server};SERVER=(local);DATABASE=EMISOR;Trusted_Connection=yes;')
    print("Conexión exitosa")
except Exception as ex:
    print("La conexión no fue exitosa")
