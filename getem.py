import tweepy
import csv #Import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


#this is what makes our data look pretty and runs our server 
#must go to this site https://dash.plot.ly/installation and pip install the following below 
#pip install dash==0.36.0  # The core dash backend
#pip install dash-html-components==0.13.5  # HTML components
#pip install dash-core-components==0.43.0  # Supercharged components
#pip install dash-table==3.1.11  # Interactive DataTable component (new!)
#pip install dash-daq==0.1.0  # DAQ components (newly open-sourced!)

#this is the csv file that was wrote in from servedup.py with your data get ready to make it pretty 
df = pd.read_csv('hacked.csv')
#df = pd.read_csv('great.csv')


# up to 80,000 tweets can be posted 
def generate_table(dataframe, max_rows=80000):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

#this is a generic style sheet from dash examples you can create your own if you would like 
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='Twacked: Want to find out who is getting Hacked on twitter'),
    generate_table(df)
])
#this will actually auto update the server when you make changes to the file. 
if __name__ == '__main__':
    app.run_server(debug=True)

   
