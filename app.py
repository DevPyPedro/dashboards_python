from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel('Vendas.xlsx')

fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")



app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),

    html.H2(children='''
        Grafico com o faturamento de todos os produtos separados por loja  
            '''),

    html.Div(children='''
        Obs: Esse grafico mosta o total vendido.
    '''),

    dcc.Dropdown(
        id='Lojas', # id do Dropdown
        options=[{'label': loja, 'value': loja} for loja in df['ID Loja'].unique()], # Lista de valores 
        value=df['ID Loja'].unique()[0]  # Valor inicial
    ),


    dcc.Graph(
        id='grafica_vendas',
        figure=fig
    ),

])
    
@callback(
    Output('grafica_vendas', 'figure'),
    Input('Lojas', 'value')
)
def update_output(value):
    filtered_df = df.loc[df['ID Loja'] == value, :]
    fig = px.bar(filtered_df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig


if __name__ == '__main__':
    app.run(debug=False)