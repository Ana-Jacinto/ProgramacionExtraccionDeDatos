import pandas as pd

datos = pd.read_csv("Datasets/surveys.csv")
#print(datos.sample)

"""
IDENTIFAR VALORES NULOS
"""
#ISNULL(): VERIFICAR LOS VALORES NULOS EXISTENTES. TRUE = EXISTE UN VALOR NULO.
nulos = datos.isnull()
#print(nulos)

#ANY(): EN UNA COLUMNA EXISTA CON QUE EXISTA 1 DATO NULO, LA COLUMNA TE LA AGREGA COMO "TRUE".
#print(nulos.any())

#SUM(): SUMAR CUANTOS DATOS NULOS TENGO POR COLUMNA.
#print(nulos.sum())

#SUM().SUM(): TOTAL DE VALORES NULOS QUE TENGO DENTRO DEL ARCHIVO.
#print(nulos.sum().sum())

#CONOCER EL PORCENTAJE DE VALORES NUELOS QUE TENGO EN CADA COLUMNA. UN ALTO DE PORCENTAJE NO ME CONVIENE, ASI QUE SEPUEDE EKIMINAR LA COLUMNA.
#print(nulos.sum()/len(nulos))


"""
ELIMINAR COLUMNAS
"""
#DROP(): FUNCION PARA ELIMINAR VALORES. PERO SOLO DEL ARCHIVO COPIA QUE PANDAS HACE AUTOMATICAMENTE.
datos_eliminados = datos.drop(["day", "month"], axis="columns")
#print(datos_eliminados.columns)
#EIMINAR LAS COUMNAS DE MI ARCHIVO ORIGINAL.
datos.drop(["day", "month"], axis="columns", inplace=True)
#print(datos.columns)

#ELIMINAR RENGLONES
row_eliminados = datos.drop([2,3,4], axis="index")
#print(row_eliminados.head(10))

#ELIMINAR NULOS, PUEDE ELIMAR COLUMNAS O RENGLONES EN DONDE SINO SE EXPECIFICA(thres) SOLO CON UN VALOR NULO TE ELIMANA.
datos_nonull = datos.dropna(axis="index", thresh=4)

#ELIMINAR LOS VALORES NULOS SOLO EN LAS COLUMNAS ESPECIFICADAS
datos_nonull = datos.dropna(axis="index", subset="hindfoot_length")
#print(len(datos))
#print(len(datos_nonull))

"""
RELLENAR VALORES FALTANTES
"""
#RELLENAR VALORES NULOS
#datos_llenos = datos.fillna("Sin datos")
#print(datos_llenos)

#RELLENAR LOS VALORES NULOS CON EL PROMEDIO DE LOS VALORES DE DETERMINADAS COLUMNAS.
columnas = ["hindfoot_length","weight"]
promedio = datos[columnas].mean()
#print(promedio)
datos_llenos = datos.fillna(promedio)
#print(datos_llenos)

#BFILL(): RELLENAR LOS VALORES NULOS AGARRANDO EL VALOR QUE ESTA ABAJO DEL VALOR NULO.
datos_bfill = datos.bfill()
#print(datos_bfill)

#FFILL(): RELLENAR LOS VALORES NUELOS CON EL VALOR QUE ESTA ARRIBA DE ELLOS.
datos_ffill = datos.ffill()
#print(datos_ffill)

#RELLENAR LOS DATOS PRIMEROS CON CON BFILL() Y LOS DATOS QUE QUEDEN NULOS AUN ASI RELLENARLOS CON FFILL().
datos_mix = datos.bfill().ffill()
#print(datos_mix)


"""
DUPLICADOS
"""
#VERIFICAR DATOS DUPLICADOS. SE VA POR RENGLON. Y SI EN TODAS LAS COLUMNAS DEL RENGLON HAY HAY DUPLICADOS ARROJA UN "TRUE".
duplicados = datos.duplicated()
#print(duplicados)

duplicados_forzado = datos.duplicated(subset=["sex", "weight"])
#print(duplicados_forzado)

#ELIMINAR DUPLICADOS
eliminar_duplicados = datos.drop_duplicates()
#print(eliminar_duplicados)

eliminar_duplicados_forzado = datos.drop_duplicates(subset=["sex", "weight"])
#print(len(eliminar_duplicados_forzado))


