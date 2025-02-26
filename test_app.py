# imports
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

pd.read_csv('https://github.com/bdishionn/panel_test/blob/a98422a8f5cf05cee98861e5a553cbd983a5dd34/Netflix%20Engagement%20Dataset.csv')

app = Dash()

# App layout
app.layout = html.Div([
    html.Div(children='My First App with Data and a Graph'),
    dash_table.DataTable(data=df.to_dict('Daily Watch Time (Hours)'), page_size=10),
    dcc.Graph(figure=px.histogram(df, x='Region', y='Customer Satisfaction Score (1-10)	', histfunc='avg'))
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)