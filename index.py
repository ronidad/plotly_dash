import dash
from dash import dcc
from dash import html

# import dash_core_components as dcc
# import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from apps import app1, app2




app.layout = html.Div([
    dcc.Link('Drugs', href='/'),
    html.Br(),
    dcc.Link('charts"', href='/apps/app2'),

    html.H2("Drug abuse in Africa", style={'text-align': 'left'}),

    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)