import pandas as pd
import plotly.express as px

data = pd.read_csv("Datasets/weekly_stocks.csv", parse_dates=True)
#print(data.head())

#GRAFICA DE LINEAS
fig = px.line(data, x="Date", y=["MSFT", "FB"], title="Microsoft Stocks")
#fig.show()

#GRAFICA DE BIGOTES
fif_box = px.box(data, y="MSFT", title="Grafica de Caja y Bigotes")
#fif_box.show()

#GRAFICA DE AREA
fig_area = px.area(data, x="Date", y=["FB", "AAPL", "MSFT"], title="Grafica de Area")
#fig_area.show()


#TRANSFORMAR LA COLUMNA "DATE" A TIPO DE DATO FECHA.
data["Date"] = pd.to_datetime(data["Date"])
data2 = data.set_index("Date")
#print(data2)
data_3months = data2.resample(rule="M").mean()[-3:]
data_3months = data_3months.reset_index()
#print(data_3months)

#GRAFICA DE COLUMNAS
columnas = ["MSFT", "FB", "AAPL"]
fig_bar = px.bar(data_3months, x="Date", y=columnas)
#Antes de graficar poder realizar modificaciones a la grafica utilizando el metodo "update_layout()"
fig_bar.update_layout(xaxis_title="Mes", yaxis_title="Dolar($)",
                      title="Stocks Mensuales")
#fig_bar.show()

#GRAFICA DE HSTOGRAMA
fig_hist = px.histogram(data, x="Date", y="MSFT", nbins=20)
#fig_hist.show()

#GRAFICA DE PUNTOS
fig_scatter = px.scatter(data, x="Date", y="MSFT", size="MSFT", color="Date")
#fig_scatter.show()


#DATO EXTRA: EN PYTHON PUEDES UTILIZAR DATAFRAMES DE DIFERENTES DATOS.
df_iris = px.data.iris()
fig_iris = px.scatter(df_iris, x="species", y="petal_width")
#fig_iris.show()

df_tips = px.data.tips()
#print(df_tips.sample(5))
fig_pie = px.pie(df_tips, values="total_bill", names="day")
#fig_pie.show()


