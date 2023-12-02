import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, dash_table, callback, Input, Output

# dcc -----> Dash Core Components
# html -----> Dash html Components


#Variable global
data = pd.read_csv("Datasets/data_olimpiadas.csv", index_col=0)

def dashboard(): #funcuion hecha automaticamente por python
    data_Pais = data.groupby("country", as_index=False).sum(numeric_only=True)
    g1 = px.line(data_Pais, x="country", y=["gold", "silver", "bronze"])

    body = html.Div([ #Divs: Contenedores
        html.H2("Datos Olimpiadas"),  #"H": son Titulos
        html.P("Objetivo DashBoard: Mostrar los resultados de las medallas de los paises."), #"P": Parrafo
        html.Hr(), #"Hr()": Es un separador.
        dash_table.DataTable(data=data.to_dict("records"), page_size=10), #"page_size": Cantidad de elementos por pagina
        dcc.Dropdown(options=["all", "gold", "silver", "bronze"], #"dcc.Dropdown()": Hacer una lista desplegable
                     value="all",
                     id="ddMedal"),  #se le pone un "id" al dropdown porque es quien dispara un evento.
        dcc.Graph(figure=g1, id="figMedal")  #"Graph": Poner graficas.
    ])
    return body

@callback(
    Output(component_id="figMedal", component_property="figure"), #Componente a quien se le va hacer el update al momento de seleccionar un input.
    Input(component_id="ddMedal", component_property="value")
)

def update_grafica(value_chosen): #Por cada input se necesita un parametro en la funcion, entonces lo que este en la variable ddMedal se asigna a la variable value_chosen
    data_Pais = data.groupby("country", as_index=False). sum(numeric_only=True)
    col_chosen = value_chosen
    if value_chosen == "all":
        col_chosen = ["gold", "silver", "bronze"]
    fig = px.line(data_Pais, x="country", y=col_chosen)
    return fig

#DEJAR EN CLARO DONDE ESTA EL "INICIO" EL PROYECTO. ESTO SE UTILIZA EN PROYECTOS GRANDES.
if __name__ == "__main__":
    app = Dash(__name__)
    #layaout: para poner contenido en el dashboard.
    app.layout = dashboard()
    app.run(debug=True) #mandar a correr mi inicio. el "debug" permite ver los errores que tiene el proyecto.

