import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# Load data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash(__name__)

# Create figures
scatter_fig = px.scatter(
    df, 
    x='gdpPercap', 
    y='lifeExp',
    color='continent',
    hover_name='country',
    title='GDP Per Capita vs Life Expectancy'
)

box_fig = px.box(
    df,
    y='lifeExp',
    x='continent',
    color='continent',
    title='Life Expectancy by Continent'
)

# App layout
app.layout = html.Div([
    html.Div(
        children=[
            html.H1('My First Dashboard', style={'color': 'red', 'textAlign': 'center'})
        ],
        style={
            'border': '1px black solid',
            'width': '100%',
            'height': '50px'
        }
    ),
    html.Div([
        html.Div(
            children=[dcc.Graph(figure=scatter_fig)],
            style={'border': '1px black solid', 'float': 'left', 'width': '49%', 'height': '400px'}
        ),
        html.Div(
            children=[dcc.Graph(figure=box_fig)],
            style={'border': '1px black solid', 'float': 'left', 'width': '49%', 'height': '400px'}
        )
    ])
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
