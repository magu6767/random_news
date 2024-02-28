import streamlit as st
import pandas as pd
import requests
import time


st.title("一日一回ランダムニュース")

category = st.radio(
    "見たいジャンルを選択",
    [
        "business",
        "entertainment",
        "health",
        "science",
        "sports",
        "technology",
    ],
    # captions=["ビジネス", "エンターテイメント", "全体"],
    horizontal=True,
)


headers = {"X-Api-Key": "9a6727a7ce2f4abe95ffdd2d9f441dd6"}

url = "https://newsapi.org/v2/top-headlines"
params = {
    "country": "jp",
    "category": category,
    "pageSize": 10,
}

if st.button("データを取得"):
    response = requests.get(url, headers=headers, params=params)

    if response.ok:
        # response_data = response.json()
        # df = pd.DataFrame(response_data["articles"])
        # for data in df[["urlToImage", "title", "url"]]:
        #     st.text(data["urlToImage"])
        if response.ok:
            response_data = response.json()
            articles = response_data["articles"]
            for article in articles:
                # 各記事の'urlToImage'キーを使用して画像のURLにアクセス
                if article["urlToImage"] is None:
                    st.error("画像を取得できませんでした")
                else:
                    st.image(article["urlToImage"])

        # st.dataframe(
        #     df[["title", "url"]],
        #     column_config={
        #         "url": st.column_config.LinkColumn(
        #             # 表示するカラム名
        #             "URL",
        #             width="medium",
        #             # 表示データのテキスト
        #             display_text="https:\/\/([^\/]+)",
        #         )
        #     },
        # )

st.text("おめでとう！今日も頑張ったね")
with st.sidebar:
    st.text_area("乙")
    with st.echo():
        st.write("This code will be printed to the sidebar.")
    st.success("Done!")
