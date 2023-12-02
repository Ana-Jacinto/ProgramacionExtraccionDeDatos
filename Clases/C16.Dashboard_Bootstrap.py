import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, dash_table, callback, Input, Output
import dash_bootstrap_components as dbc

#Variable global
data = pd.read_csv("Datasets/data_olimpiadas.csv", index_col=0)


def tarjeta_filtros():
    control = dbc.Card([
        html.Div([
            dbc.Label("Gender:"),
            dcc.Dropdown(options=["All", "Male", "Female"], value="All")
        ]),
        html.Div([
            dbc.Label("Medal:"),
            dcc.Dropdown(options=["all", "gold", "silver", "bronze"], value="all", id="ddMedal"),
        ]),
        html.Div([
            dbc.Label("Year:"),
            dbc.Input(type="number")
        ])
    ])
    return control

def dashboard(): #funcuion hecha automaticamente por python
    data_Pais = data.groupby("country", as_index=False).sum(numeric_only=True)
    g1 = px.line(data_Pais, x="country", y=["gold", "silver", "bronze"])

    body = html.Div([ #Divs: Contenedores
        html.H2("Datos Olimpiadas"),  #"H": son Titulos
        html.P("Objetivo DashBoard: Mostrar los resultados de las medallas de los paises."), #"P": Parrafo
        html.Hr(), #"Hr()": Es un separador.
        dbc.Row( #"Row": Para columnas
            [
                dbc.Col(
                    html.Div([
                        html.H3("Filtros"),
                        tarjeta_filtros()
                    ]), width=4 #"width": Para el amañano del ojeto. En este caso estamos dando la instruccion de que abarque 3 columnas de 12.
                ),
                dbc.Col(
                    html.Div([
                        dbc.Row(dcc.Graph(figure=g1, id="figMedal")),
                        dbc.Row(dash_table.DataTable(data=data.to_dict("records"), page_size=10),)
                    ]), width=8
                ),
             ]
        ),
    ])
    return body


#INICIALIZACION DEL PROYECTO
if __name__ == "__main__":
    app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG]) #Declarar un objeto. "external_stylesheets": Para pasar diseños de otras partes.
    app.layout = dashboard()
    app.run(debug=True)

