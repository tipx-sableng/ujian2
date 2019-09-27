import plotly
import plotly.graph_objects  as go
import plotly.express as px
from clean import data
import json

def count_type1():
    df = data()
    df_group= df['mpg'].value_counts()
    
    fig = go.Figure([
        go.Bar(x=df_group.index , y= df_group.values)
    ])
    fig_json = json.dumps(fig , cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
    # fig.show()

def dist_total():
    df= data()
    fig = px.box(df,x='x' , y='Count')
    fig_json = json.dumps(fig , cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
