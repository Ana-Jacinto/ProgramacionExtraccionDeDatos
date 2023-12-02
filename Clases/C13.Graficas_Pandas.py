import pandas as pd
import matplotlib.pyplot as plt

#LEER EL ARCHIVO Y HACER QUE PANDAS IDENTIFIQUE LAS FECHAS EN SU FORMATO "DATE" Y NO EN TEXTO NORMAL CON LA FUNCION "PARSE_DATES=TRUE"
#Y DE PREFERENCIA PONER LAS FECHAS EN FORMA DE INDICE CON LA FUNCION "INDEX_COL="DATE"".
data = pd.read_csv("Datasets/weekly_stocks.csv", parse_dates=True, index_col="Date")
#print(data.sample(5))

"""
GRAFICAR
"""
#GRAFICA LINEAL DE TODAS LAS COLUMNAS
data.plot()
#plt.show()

#GRAFICA LINEAL SOLO DE LA COLUMNA DE MICROSOFT
data.plot(y="MSFT")
#plt.show()

#MODIFICAR EL TAMAÑO DE LA GRAFICA CON "FIGSIZE"
data.plot(y="MSFT", figsize=(9,6))
#plt.show()

#CONFIRMAR EL TIPO DE GRAFICO QUE QUEREMOS. PONER UN TITULO AL GRAFICO. PONER NOMBRE A LA "X" Y "Y".
data.plot.line(y=["MSFT", "AAPL"], title="Microsoft and Apple stocks", ylabel="USD", xlabel="Week", color=["lightgreen", "pink"])
#plt.show()

#CAMBIAR EL TIPO DE GRAFICA A "CAJAS Y BIGOTES" EN HORIZONTAL
data.plot(kind="box", vert=False)
#plt.show()

#CAMBIAR EL TIPO DE GRAFICA A "AREAS" DE MICROSOFT.
data.plot(kind="area", y=["MSFT", "FB"])
#plt.show()

#GRAFICO DE AREA PERO QUE ESTEN APLILADAS CON LA FUNCION "STACKED".
data.plot(kind="area", stacked="False")
#plt.show()

#HACER UN GRAFICO DE BARRAS QUE ME CALCULE EL PROMEDIO DE LOS PRECIOS DE LAS ACCINES, TOMANDO EN CUENTA LOS ULTIMOS 3 MESES CON LA FUNCION "RULE="M" Y "MEAN".
data_3months = data.resample(rule="M").mean()[-3:]
data_3months.plot(kind="bar", ylabel="Price")
#plt.show()

#GRAFICA DE HISTOGRAMA CON UN NIVEL DE TRANSLUCIDO QUE VA DESDE EL 0 AL 1.
#HISTOGRAMA O TABLA DE FRECUENCIAS: EN ESTE CASO NOS DICE QUE TANTO OCURRIO ALGO. EJEMPLO: QUE TANTO LAS ACCIONES DE APPLE TUVO EL VALOR DE 150.
data.plot(kind="hist", alpha=0.6)


#LA GRAFICA DE SCATTER OBLIGA A PONER "X" Y "Y". ASI QUE PRIMERO SE DEBE DE REERTIR LAS FECHAS QUE ESTAN EN FORMA DE INDICE A COLUMNA. Y LUEGO HACER LA GRAFICA.
data2 = data.reset_index()
data2.plot(kind="scatter", x="Date", y="MSFT")

#GRAFICA DE BARRAS. AGARRAR EL VALOS DE LAS ACCIONES DE LOS ULTIMOS TRES MESES DE SOLO LA EMPRESA MSFT MOSTRANDO LOS PORCENTAJES. QUITANDO LAS LEYENDAS "LEGEND=FALSE".
data_3months = data.resample(rule="M").mean()[-3:]
data_3months.MSFT.plot(kind="pie", subplots=True, legend=False, figsize= (14, 7), autopct="%.f")
plt.show()