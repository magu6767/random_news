import pandas as pd


def add_count(selected_category: str):
    df_loaded = pd.read_csv("datas/data.csv")

    # データフレームのデータ型を確認
    df_loaded[selected_category] += 1

    # 変更後のデータをファイルに再書き込み
    df_loaded.to_csv("datas/data.csv", index=False)
