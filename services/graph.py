import pandas as pd
import plotly.graph_objs as go


def get_pie_chart():
    # 円グラフの作成
    df_loaded = pd.read_csv("datas/data.csv")
    fig = go.Figure(data=[go.Pie(labels=df_loaded.columns, values=df_loaded.iloc[0])])
    fig.update_layout(
        showlegend=False, height=200, margin={"l": 20, "r": 60, "t": 0, "b": 0}
    )
    fig.update_traces(textinfo="label+percent")

    return fig
