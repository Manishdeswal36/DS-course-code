import numpy as np
import pandas as pd
import plotly.graph_objects as go

from dash import Dash, html, dcc, Input, Output

# External CSS stylesheet
external_stylesheets = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-uCw98/SfnGE*ft3GXwEOngsV77t27NXFoao4pmYm81iuXoPkF)jBERdknLPMO',
        'crossorigin': 'anonymous'
    }
]

patients_df = pd.read_csv('covid_19_india.csv')
active_cases = patients_df['Confirmed'].sum()
recovered_cases = patients_df['Cured'].sum()
death_cases = patients_df['Deaths'].sum()
total = active_cases + death_cases + recovered_cases


our_options = [
    {'label': 'All','value': 'All'},
    {'label': 'Confirmed','value': 'Confirmed'},
    {'label': 'Cured','value': 'Cured'},
    {'label': 'Deaths','value': 'Deaths'},
    
]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1("Covid-19 Virus Dashboard",style={'color': 'white', 'text-align': 'center'}),
    
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total Cases',className='text-light'),
                    html.H4(total,className='text-light')
                    ],className='card-body')
                ], className='card bg-danger')
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Active Cases',className='text-light'),
                    html.H4(active_cases,className='text-light')
                    ],className='card-body')
                ], className='card bg-info')
            ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Recovered',className='text-light'),
                    html.H4(recovered_cases,className='text-light')
                    ],className='card-body')
                ], className='card bg-warning')
            ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Deaths',className='text-light'),
                    html.H4(death_cases,className='text-light')
                    ],className='card-body')
                ], className='card bg-success')
            ],className='col-md-3'),
        
        ],className='row'),
    html.Div([],className='row'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id = 'picker',options=our_options,value='All'),
                    dcc.Graph(id='bar',)
                ],className='card-body')
            ],className='card')
        ],className='col-md-12')
    ],className='row'),
    
    
], className='container')

# first connect to dropdown second to grpah

@app.callback(Output('bar', 'figure'), [Input('picker', 'value')])
def update_graph(selected_type):
    if selected_type == 'Confirmed':
        df_grouped = patients_df.groupby('State/UnionTerritory')['Confirmed'].sum().sort_values(ascending=False).reset_index()
        return {
            'data': [go.Bar(x=df_grouped['State/UnionTerritory'], y=df_grouped['Confirmed'])],
            'layout': go.Layout(title='State wise Confirmed Cases')
        }
    elif selected_type == 'Deaths':
        df_grouped = patients_df.groupby('State/UnionTerritory')['Deaths'].sum().sort_values(ascending=False).reset_index()
        return {
            'data': [go.Bar(x=df_grouped['State/UnionTerritory'], y=df_grouped['Deaths'])],
            'layout': go.Layout(title='State wise Death Cases')
        }
    elif selected_type == 'Cured':
        df_grouped = patients_df.groupby('State/UnionTerritory')['Cured'].sum().sort_values(ascending=False).reset_index()
        return {
            'data': [go.Bar(x=df_grouped['State/UnionTerritory'], y=df_grouped['Cured'])],
            'layout': go.Layout(title='State wise Recovered Cases')
        }
    elif selected_type == 'All':
        df_grouped = patients_df.groupby('State/UnionTerritory')[['Confirmed', 'Deaths', 'Cured']].sum().reset_index()
        return {
            'data': [
                go.Bar(name='Confirmed', x=df_grouped['State/UnionTerritory'], y=df_grouped['Confirmed']),
                go.Bar(name='Deaths', x=df_grouped['State/UnionTerritory'], y=df_grouped['Deaths']),
                go.Bar(name='Cured', x=df_grouped['State/UnionTerritory'], y=df_grouped['Cured'])
            ],
            'layout': go.Layout(title='State wise Cases (All)', barmode='stack')
        }
    else:
        return {
            'data': [],
            'layout': go.Layout(title='No data to display')
        }

    
        



if __name__ == '__main__':
    app.run(debug=True)
