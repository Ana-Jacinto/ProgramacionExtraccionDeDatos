import pandas as pd

alumnos = {
    "nombre": ["Juan", "Maria", "Pedro", "Miguel", "Test"],
    "edad": [20, 19, 22, 18, 20],
    "carrera": ["IN", "C", "NI", "IN", ""],
    "promedio": [90, 85, 70, 100, 80]
}

df_alumnos = pd.DataFrame(alumnos)

carrera = {
    "nombre": ["IN", "C", "NI", "A", "I"],
    "alumnos": [190, 1000, 300, 2000, 60],
    "creditos": [352, 350, 360, 326, 340]
}

df_carrera = pd.DataFrame(carrera)

#TIPOS DE JOIN (UNIONES ENTRE TABLAS):
#MERGE: DEL DF ALUMNOS SELECCIONAR LA TABLA QUE SE LLAMA CARRERA Y DEL DF CARRERA LA TABLA QUE SE LLAMA NOMBRE Y UNIR SOLO AQUELLOS QUE COINCIDAN.
data = pd.merge(df_alumnos, df_carrera, how="inner", left_on="carrera", right_on="nombre")
#print(data)
#MOSTRAR LOS DATOS DE LA DERECHA O SEA DE DF_CARREA AUNQUE EN EL DF ALUMNOS NOS MUESTRE NA.
data = pd.merge(df_alumnos, df_carrera, how="right", left_on="carrera", right_on="nombre")
#print(data)
#MOSTAR LOS DATOS DE LA IZQUIERDA O DEK DF ALUMNOS.
data = pd.merge(df_alumnos, df_carrera, how="left", left_on="carrera", right_on="nombre")
#print(data)
#MOSTRAR TODOS LOS DATOS DE ALUMNOS Y CARRERA
data = pd.merge(df_alumnos, df_carrera, how="outer", left_on="carrera", right_on="nombre", suffixes=("_alumnos", "_carrera"))
#print(data)

#CONCATENATION
alumnos2 = {
    "nombre": ["Juan", "Maria", "Pedro", "Miguel", "Test"],
    "edad": [20, 19, 22, 18, 20],
    "carrera": ["IN", "C", "NI", "IN", ""],
    "promedio": [90, 85, 70, 100, 80]
}

df_alumnos2 = pd.DataFrame(alumnos2)

#CONCATENAR DOS DATAFRAMES UNO ABAJO DEL OTRO ("index"). ES IMPORTANTE QUE COINCIDAN CON EL NUMERO DE COLUMNAS.
concatenar = pd.concat([df_alumnos, df_alumnos2], axis="index", ignore_index=True)
#print(concatenar)

#CONCATENAR DOS DATAFRAMES UNO A LADO DE OTRO ("columns"). ES IMPORTANTE QUE COINCIDAD CON EL NUMERO DE RENGLONES.
concatenar2 = pd.concat([df_alumnos, df_alumnos2], axis="columns")
#print(concatenar2)

#CALCULAR EL PROMEDIO DE LA LOS DOS DATAFRAMES CONCATENADOS DE LA TABLA "PROMEDIO".
#print(concatenar.promedio.mean())

#CALCULAR EL PROMEDIO DE AQUELLAS COLUMNAS CONCATENADAS QUE SEAN DE TIPO NUMERICO SOLAMENTE.
#print(concatenar.mean(numeric_only=True))

