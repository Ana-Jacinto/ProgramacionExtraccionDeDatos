import pandas as pd

#CREAR DICCIONARIO
datos = {
    "Nombre": ["Maria", "Luis", "Carmen"],
    "Materias": ["Matematicas", "Programacion", "Mercadotecnia"],
    "Promedios": [80, 90, 100]
}

#CONVERTIR EL DICCIONARIO A UN DATA FRAME
df_alumnos = pd.DataFrame(datos)
#print(df_alumnos)

#De una pagina "csv" bajarla a python en forma de data frame (se ddebe de hacer una limpieza si los datos no estan separados por ",").
df_colesterol = pd.read_csv("https://raw.githubusercontent.com/asalber/"
"manual-python/master/datos/colesteroles.csv", sep=";", decimal=",")

#print(df_colesterol)

#ALGUNAS FUNCIONES BASICAS QUE SE PUEDEN HACER EN UN DATAFRAME.
#Imprimir los primeros 5 datos de forma aleatoria
#print(df_colesterol.sample(5))
#Conocer las columnas que hay en el DF, el tipo de datos y si hay valores nulos.
#print(df_colesterol.info())
#Descripcion matematica rapida de los datos.
#print(df_colesterol.describe())
#Seleccionar las columnas que se quieren visualizar.
#print(df_colesterol[["nombre", "edad", "colesterol"]])

#Mismas funciones de una lista np.array se pueden realizar con pandas en un DF.
""""
print(df_colesterol.shape)
print(df_colesterol.size)
print(df_colesterol.columns)
print(df_colesterol.dtypes)
print(df_colesterol.index)

"""



