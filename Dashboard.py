from dash import Dash, html, dcc 
import plotly.express as px
import pandas as pd
import plotly
import plotly.graph_objects as go
from dash.dependencies import Input, Output

Data_general_buses = pd.read_csv('Parque automotor BUSES fusa.csv', delimiter=';')

app = Dash(__name__)
app.layout = html.Div(
        children = [
        html.Div(
            className = "app-header",
            children = [
                html.Div('Parque automotor Buses Fusa', className="app-header--title"),
                ] 
        ),
        html.Div(
            children=[
                dcc.Dropdown(Data_general_buses['EMPRESA'].unique(), 'Empresas de buses en Fusa', id = 'xaxis-column')
            ]
        ),
        html.Div(
            className = 'graficoPastel',
            children=[
                html.H3('Distribución de empresas'),
                dcc.Graph(id = 'Gráfico de pastel', figure={}),
            ]
        ),
        html.Div(
            className = 'graficoBarras',
            children = [
                html.H3('Tipo de combustible utilizado'),
                dcc.Graph(id = 'Gráfico de barras', figure={}),
            ]
        ),
        html.Div(
            className = 'graficoPastelCarroceria',
            children = [
                html.H3('Tipo de combustible utilizado'),
                dcc.Graph(id = 'Gráfico de barras carroceria', figure={}),
            ]
        ),
        html.Div(
            className = 'graficoLineas',
            children=[
                html.H3('Año de modelo'),
                dcc.Graph(id = 'Gráfico de Lineas', figure={}),
            ]
        ),
])

@app.callback(Output("Gráfico de pastel", "figure"), [Input("xaxis-column","value")])
def actualizacion_en_vivo_grafico_pastel(value):
    fig = px.pie(
    Data_general_buses, 
    names='EMPRESA')
    return fig 

@app.callback(Output("Gráfico de barras", "figure"), [Input("xaxis-column","value")])
def actualizacion_grafico_barras(value):
    fig = px.bar(
    Data_general_buses, 
    x = 'COMBUSTIBLE',
    y='CAPACIDAD DE PASAJEROS SENTADOS',
    )
    return fig 

@app.callback(Output("Gráfico de barras carroceria", "figure"), [Input("xaxis-column","value")])
def actualizacion_en_vivo_grafico_pastel(value):
    fig = px.pie(
    Data_general_buses, 
    names='TIPO DE CARROCERIA')
    return fig 

@app.callback(Output("Gráfico de Lineas", "figure"), [Input("xaxis-column","value")])
def actualizacion_grafico_barras(value):
    fig = px.line(
    Data_general_buses, 
    x = 'ANO MODELO',
    y='MARCA',
    )
    return fig 

if __name__ == '__main__':
     app.run_server(debug = True)