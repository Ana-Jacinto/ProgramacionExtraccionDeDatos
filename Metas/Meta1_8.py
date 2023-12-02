import pandas as pd

empleados = {"salario": [20000, 10000, 40000, 25000, 60000],
            "edad": [20, 18, 35, 40, 45]}

dataframe = pd.DataFrame(empleados)

# Nombre: Ana Beatriz Jacinto Cano     Grupo: 951     Fecha: 20 de agosto de 2023
# Problema: Realizar una función que normalice los datos usando min-max que reciba como parámetro un DataFrame y otro parámetro que sea una lista de columnas a normalizar.
# Retornar el DataFrame con los datos normalizados.
def min_max(dataframe, list):
    dataframe["min-max_salario"] = dataframe[list] - dataframe[list].min() / (dataframe[list].max() - dataframe[list].min())
    return dataframe

data = dataframe
list = ["salario"]

#print(min_max(data, list))


# Nombre: Ana Beatriz Jacinto Cano     Grupo: 951     Fecha: 20 de agosto de 2023
# Problema: Realizar una función que normalice los datos usando Z-Score que reciba como parámetro un DataFrame y otro parámetro que sea una lista de columnas a normalizar.
# Retornar el DataFrame con los datos normalizados.
def z_score(dataframe, list):
    dataframe["zscore"] = (dataframe[list] - dataframe[list].mean()) / dataframe[list].std()
    return dataframe

data = dataframe
list = ["salario"]

#print(z_score(data, list))


# Nombre: Ana Beatriz Jacinto Cano     Grupo: 951     Fecha: 20 de agosto de 2023
# Problema: Realizar una función que normalice los datos usando escalado simple que reciba como parámetro un DataFrame y otro parámetro que sea una lista de columnas a normalizar.
# Retornar el DataFrame con los datos normalizados.
def escalado_simple(dataframe, list):
    dataframe["escalado"] = data[list] / dataframe[list].max()
    return dataframe

data = dataframe
list = ["salario"]

#print(escalado_simple(data, list))

