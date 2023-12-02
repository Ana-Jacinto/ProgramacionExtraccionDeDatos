import pandas as pd

alumnos = {
    "nombre": ["Juan", "Maria", "Pedro", "Miguel", "Test"],
    "edad": [20, 19, 22, 18, 20],
    "carrera": ["IN", "C", "NI", "IN", ""],
    "promedio": [90, 85, 70, 100, 80]
}

df_alumnos = pd.DataFrame(alumnos)

#1. TECNICA FILTRADO DE DATOS
#Mostrar aquellos valores que cuentan con un promedio mayor a 80.
c1 = (df_alumnos.promedio > 80)
data_c1 = df_alumnos[c1]
#print(data_c1)

#Donde los alumnos tengna promedio mayor a 80 y los alumnos de la carrera sean de IN o de C. #ISIN Nos ahorra el poner "OR" (|).
c2 = (df_alumnos.promedio > 80) & (df_alumnos.carrera.isin(["IN", "C"]))
data_c2 = df_alumnos[c2]
#print(data_c2)

#Seleccionar solo el nombre y carrera de los alumnos de IN con un promedio mayor a 80.
data_c2 = df_alumnos[c2][["nombre", "carrera"]]
#print(data_c2)


#2. TECNICA BUSQUEDA POR QUERY
#Mostrar aquellos valores que cuentan con un promedio mayor a 80 en forma de cadena.
q1 = df_alumnos.query("promedio > 80")
#print(q1)

#Mostrar los alumnos tengna promedio mayor a 80 y los alumnos de la carrera sean de IN  o C en forma de cadena.
condicion = "promedio > 80 and carrera.isin(['IN', 'C'])"
columnas = ["nombre", "carrera"]
q2 = df_alumnos.query(condicion)
#print(q2[columnas])



