import pandas as pd
import numpy as np

data = pd.read_csv("Datasets/data_olimpiadas.csv", index_col=0)
#print(data.sample(5))

#AGRUPACION DE LOS DATOS
datos_agrupados = data.groupby(["gender", "country"])
#print(datos_agrupados.get_group("female"))
#print(datos_agrupados.count())
columnas = ["gold", "silver", "bronze"]
res = datos_agrupados[columnas].sum()
#print(res)

#MOSTRAR LOS PAISES MOSTRANDO LAS MEDALLAS QUE HA GANADO.
#print(data.country.value_counts().head(25))

#ORDENAR EL VALOR DE "AÑO" DE MANERA ASCENDENTE
#print(data.sort_values("year", ascending=False))

#SACAR EL PROMEDIO DE UN ARCHIVO QUE CONTENGA TEXTO SIN FILTRAR LAS COLUMNAS QUE SOLO SON NUMERICAS.
#print(data.mean(numeric_only=True))

#DESCRIBIR LAS COLUMNAS
#print(data.describe().transpose())

#MOSTRAR EL PROMEDIO DE MEDALLAS DE ORO POR PAIS
grupos_gender = data.groupby(["gender", "country"])
#print(grupos_gender.sample(5))
#print(grupos_gender.gold.mean().unstack())

#AGRUPACION EN TABLAS PIBOTE. MOSTRAR EL PROMEDIO DE MEDALLAS DE ORO POR PAIS JUNTO CON EL PROMEDIO DE CADA UNO.
#print(data.pivot_table("gold", index="gender", columns="country",margins=True, aggfunc=np.sum))


