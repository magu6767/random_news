import streamlit as st
from services import graph
from services import file_service, server_communication

ss = st.session_state

ss.setdefault("articles", None)

category = {
    "business": "ビジネス",
    "entertainment": "エンタメ",
    "health": "健康",
    "science": "科学",
    "sports": "スポーツ",
    "technology": "テクノロジー",
}

category_keys = list(category.keys())


def main():
    # タイトル
    st.title("一日一回ランダムニュース")

    # ラジオボタン
    selected_category = st.radio(
        "見たいカテゴリを選択",
        # selected_categoryに渡す値
        category_keys,
        # 表示名をkeyに対応するvalueに設定
        format_func=lambda key: category[key],
        horizontal=True,
    )

    # 取得ボタン
    if st.button("データを取得"):
        ss.articles = server_communication.get_article_data(selected_category)

    # 記事一覧
    if ss.articles is not None:
        for article in ss.articles:
            if any(
                article[key] is None for key in ["urlToImage", "title", "description"]
            ):
                continue

            st.markdown(
                f"""
                  <h5>{article["title"]}</h5>
                  <img src="{article["urlToImage"]}" width="300">
                  <br>
                  <br>
                  <p>{article["description"]}</p>
                  <a href="{article["url"]}">{article["url"]}</a>
                  <hr>        
                """,
                unsafe_allow_html=True,
            )

    # サイドバー
    with st.sidebar:
        if st.button("ニュースを読み終わった"):
            file_service.add_count(selected_category)
            st.success("記録が保存されました！")
            st.text(f"{selected_category} の記事を読みました！")

        st.markdown("## カテゴリデータ")
        # Streamlitで円グラフを表示
        st.plotly_chart(graph.get_pie_chart(), use_container_width=True)


if __name__ == "__main__":
    main()
