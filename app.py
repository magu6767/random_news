import streamlit as st
import pandas as pd
import requests
import plotly.graph_objs as go
import pandas as pd


def add_count(selected_category: str):
    df_loaded = pd.read_csv("data.csv")

    # データフレームのデータ型を確認
    df_loaded[selected_category] += 1

    # 変更後のデータをファイルに再書き込み
    df_loaded.to_csv("data.csv", index=False)


ss = st.session_state

ss.setdefault("articles", None)

st.title("一日一回ランダムニュース")

category = [
    "business",
    "entertainment",
    "health",
    "science",
    "sports",
    "technology",
]

selected_category = st.radio(
    "見たいカテゴリを選択",
    category,
    # captions=["ビジネス", "エンターテイメント", "全体"],
    horizontal=True,
)

headers = {"X-Api-Key": "9a6727a7ce2f4abe95ffdd2d9f441dd6"}

url = "https://newsapi.org/v2/top-headlines"
params = {
    "country": "jp",
    "category": selected_category,
    "pageSize": 10,
}

if st.button("データを取得"):
    response = requests.get(url, headers=headers, params=params)

    if response.ok:
        response_data = response.json()
        ss.articles = response_data["articles"]

if ss.articles is not None:
    for article in ss.articles:
        if any(article[key] is None for key in ["urlToImage", "title", "description"]):
            continue

        st.markdown(
            f"""
            ##### {article["title"]}

            <img src="{article["urlToImage"]}" width="300">

            {article["description"]}

            [{article["url"]}]({article["url"]})

            ---            
            """,
            unsafe_allow_html=True,
        )

with st.sidebar:
    if st.button("ニュースを読み終わった"):
        add_count(selected_category=selected_category)
        st.success("記録が保存されました！")
        st.text(f"{selected_category} の記事を読みました！")

st.sidebar.markdown("## カテゴリデータ")

# 円グラフの作成
df_loaded = pd.read_csv("data.csv")
fig = go.Figure(data=[go.Pie(labels=df_loaded.columns, values=df_loaded.iloc[0])])
fig.update_layout(
    showlegend=False, height=200, margin={"l": 20, "r": 60, "t": 0, "b": 0}
)
fig.update_traces(textinfo="label+percent")

# Streamlitで円グラフを表示
st.sidebar.plotly_chart(fig, use_container_width=True)
