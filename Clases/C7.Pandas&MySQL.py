import pandas as pd

#SQLALCHEMY: LIBRERIA QUE ME PERMITE CONECTAR CON MUCHAS BASES DE DATOS.
from sqlalchemy import create_engine
#UNA ENUMERACION ES UN OBJETO ESPECIAL PARA ENCERRAR EN CLASES LAS CONSTANTES (VALORES QUE NO VAN A CAMBIAR NUNCA).
from enum import Enum

#VALORES CONSTANTES: Servidor, Usuario, Contraseña... (LAS CONSTANTES VAN EN MAYUSCULAS DENTRO DE LAS CALSES)
class DataBD(Enum):
    USER = "root"
    PASSWORD = "1290"
    NAME_DB = "olimpiadas"
    SERVER = "localhost"


""""
#RECORRES TODAS LAS VARIABLES QUE ESTAN EN LA CLASE DataBD
for item in DataBD:
    print(item.name, item.value)
"""

#REALIZAR UNA CADENA QUE ME PERMITA CONECTARME CON MI BASE DE DATOS
cadena_conexion = (f"mysql+mysqlconnector://{DataBD.USER.value}:{DataBD.PASSWORD.value}"
                   f"@{DataBD.SERVER.value}/{DataBD.NAME_DB.value}")
#print(cadena_conexion)


engine = create_engine(cadena_conexion)
conexion = engine.connect()
#print(conexion)

#CREAR UNA BASE DE DATOS CON LOS DATOS QUE TENGO EN MI ARCHIVO "OLIMPIADAS"
datos_olimpiadas = pd.read_csv("Datasets/data_olimpiadas.csv", index_col=0)
#print(datos_olimpiadas.sample(5))

#Funcion UNIQUE() Elimina los datos duplicados
genders = datos_olimpiadas.gender.unique()
#print(genders)

df_genders = pd.DataFrame(genders, columns=["nombre"]) #El nombre de las columnas deben de coincidir con mi base de datos.
#print(df_genders)

#Pasar toda mi informacion a una tabla en sql con "to.sql()"
#"index=False" significa que ignore los indices que agrega python.
#df_genders.to_sql("genero", conexion, if_exists="append", index=False)

#query = "genero"
#query = "SELECT nombre FROM genero"
query = "SELECT nombre FROM genero WHERE nombre = %s"
parametro = ("female",)
resultados = pd.read_sql(query, conexion, params=parametro)
#print(resultados)
