import pandas as pd

alumnos = {
    "nombre": ["Juan", "Maria", "Pedro", "Miguel", "Juan"],
    "edad": [20, 19, 22, 18, 20],
    "carrera": ["IN", "C", "NI", "IN", "AE"],
    "promedio": [90, 85, 70, 100, 80]
}

df_alumnos = pd.DataFrame(alumnos)

#CAMBIAR LOS NOMBRES COMO INDICES EN EL DATAFRAME.
df_alumnos_index = df_alumnos.set_index(df_alumnos.nombre)
#print(df_alumnos_index)

#BORRAR LA COLUMNA NOMBRE PARA QUE SOLO APAREZCA COMO INDICE.
df_alumnos_index = df_alumnos.set_index("nombre", drop=True)
#print(df_alumnos_index)

#PONER COMO INDICE DOS O MAS VARIABLES. UTILIZADO PARA LAS LLAVES PRIMARIAS COMPUESTAS.
#df_alumnos_index = df_alumnos.set_index(["nombre", "edad"], drop=True)
#print(df_alumnos_index)

#REGRESAR EL DATAFRAME A SU ESTADO ANTERIOR. EN ESTE CASO QUITAR LOS INDEX DE NOMBRES.
df_reset = df_alumnos_index.reset_index()
#print(df_reset)

#BUSCAR TODOS LOS DATOS DADO UN INDICE.
#print(df_alumnos_index.loc["Juan"])

#SOLO TRAER LOS DATOS DE PROMEDIO Y CARRERA DADO UN INDICE.
#print(df_alumnos_index.loc["Juan", ["promedio", "carrera"]])

#SOLO TRAER LOS DATOS DE PROMEDIO Y CARRERA DADO DOS O MAS INDICE.
#print(df_alumnos_index.loc[["Juan", "Maria"], ["promedio", "carrera"]])

#CON "ILOC" ES LO MISMO QUE LOC SOLO QUE AQUI SE UTILIZAN EXCLUSIVAMENTE NUMEROS. "NOMBRE_DF.ILOC[#INDICE, [#COLUMNAS]]"
print(df_alumnos_index.iloc[2, [1, 2]])
print(df_alumnos_index.iloc[0:2, 1:3])