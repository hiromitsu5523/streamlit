
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルをアップロードするファイル選択ウィジェットを作成
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# CSVファイルがアップロードされたら、pandasデータフレームに読み込む
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # データフレームを表示する
    st.write(df)

    # データフレームの統計情報を表示する
    st.write(df.describe())

    # 各カラムごとにヒストグラムを表示する
    for column in df.columns:
        fig, ax = plt.subplots()
        ax.hist(df[column], bins=20)
        ax.set_xlabel(column)
        ax.set_ylabel('Frequency')
        st.pyplot(fig)
