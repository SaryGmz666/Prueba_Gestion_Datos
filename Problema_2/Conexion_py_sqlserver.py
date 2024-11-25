import pandas as pd
import pyodbc
from datetime import datetime

#Usamos este tipo de conector ya que se cuenta con Windows Autentication
try: 
    conexion=pyodbc.connect('DRIVER={SQL Server};SERVER=(local);DATABASE=EMISOR;Trusted_Connection=yes;')
    print("Conexión exitosa")
    cursor=conexion.cursor()
    
except Exception as ex:
    print("La conexión no fue exitosa")

# Cargar los archivos .txt en DataFrames
clientes_df = pd.read_csv("Datos_Tb_Clientes.txt", sep='\t', encoding='utf-8')
productos_df = pd.read_csv("Datos_Tb_Productos.txt", sep='\t', encoding='utf-8')
operativa_df = pd.read_csv("Datos_Tb_Operativa.txt", sep='\t', encoding='utf-8')
