import pandas as pd
import numpy as np

#Nombre: Ana Beatriz Jacinto Cano     Grupo: 951     Fecha: 27 de agosto de 2023
#Problema: Escribir un programa que genere y muestre por pantalla un DataFrame con los datos de la tabla.
datos = {
    "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
    "Ventas": [30500, 35600, 28300, 33900],
    "Gastos": [22000, 23400, 18100, 20700]
}
df_finanzas = pd.DataFrame(datos)

print(df_finanzas)

#Nombre: Ana Beatriz Jacinto Cano     Grupo: 951     Fecha: 27 de agosto de 2023
#Problema: Escribir una función que reciba un DataFrame con el formato del ejercicio anterior, una lista de meses
# y devuelva el balance (ventas - gastos) total en los meses indicados.
def calcular_balance(df, meses):
    #Seleccionar la columna "Mes" del df_finanzas para despues seleccionar el mes dado en la lista de meses con la funcion ".isin"
    filtro = df['Mes'].isin(meses)
    #Acceder a filas y columnas especificadas con la funcion ".loc"
    balance = (df.loc[filtro, 'Ventas'] - df.loc[filtro, 'Gastos']).sum()
    return balance

meses_deseados = ['Enero', 'Febrero', 'Marzo', 'Abril']
balance_total = calcular_balance(df_finanzas, meses_deseados)
print(f"El balance total en los meses {', '.join(meses_deseados)} es de: ${balance_total}")


#Nombre: Ana Beatriz Jacinto Cano     Grupo: 951     Fecha: 27 de agosto de 2023
#Problema: El archivo cotizacion.csv contiene las cotizaciones de las empresas del IBEX35. Construir una función que construya un DataFrame
# a partir del archivo con el formato anterior y devuelve otro DataFrame con el mínimo, el máximo y la media de cada columna.
def construccion_DF():
    df_cotitaciones = pd.read_csv("https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/cotizacion.csv", sep=";", decimal=",")
    """print(df_cotitaciones)"""
    #Seleccionar solo las columnas con tipo de datos numericos para despues hacer calculos con ellos.
    selec_columns = df_cotitaciones.select_dtypes(include=[np.number])
    df_estadisticas = pd.DataFrame({
        "Minimo": selec_columns.min(),
        "Maximo": selec_columns.max(),
        "Promedio": selec_columns.mean()
    })
    return df_estadisticas

archivo = construccion_DF()
print(archivo)


#Nombre: Ana Beatriz Jacinto Cano     Grupo: 951     Fecha: 27 de agosto de 2023
#Problema: El archivo titanic.csv contiene información sobre los pasajeros del Titanic. Escribir un programa con los siguientes requisitos:
# a)Generar un DataFrame con los datos del archivo.
df_titanic = pd.read_csv("https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/titanic.csv")
print(df_titanic)
# b)Mostrar por pantalla las dimensiones del DataFrame.
print(f"Las dimensiones del DataFrame Titanic son de: {df_titanic.shape}")
# c)Mostrar el número de datos que contiene, los nombres de sus columnas.
print(df_titanic.info())
# d)Mostrar las 10 primeras filas y las 10 últimas filas.
print(df_titanic.head(10))
print(df_titanic.tail(10))
# e)Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
sobrevivientes = df_titanic['Survived'].mean() * 100
muertes = 100 - sobrevivientes.__round__()
print(f"El porcentaje de sobrevivientes es de: {sobrevivientes.__round__()}% \nY el procentaje de personas que murieron es de: {muertes}%")
# f)Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
sobrev_clase = (df_titanic.groupby("Pclass")["Survived"].mean() * 100).__round__()
print(sobrev_clase)
