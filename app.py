import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re

st.title("🔐 Windows Security Log Dashboard")

st.write("WindowsイベントログのCSVをアップロードして、ログオンイベントを分析します。")

uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])

if uploaded_file is not None:
    # CSV読み込み
    df = pd.read_csv(uploaded_file)

    # イベントビューアCSVの列ズレ対策
    df = df.reset_index()

    # 列名を付け直す
    df.columns = [
        "キーワード",
        "日付と時刻",
        "ソース",
        "イベント ID",
        "タスクのカテゴリ",
        "詳細"
    ]

    # 日付変換
    df["日付と時刻"] = pd.to_datetime(
        df["日付と時刻"],
        format="%Y/%m/%d %H:%M:%S",
        errors="coerce"
    )

    # 変換できない行を除外
    df = df.dropna(subset=["日付と時刻"])

    st.subheader("📄 データ確認")
    st.dataframe(df.head())

    st.subheader("📊 基本情報")
    st.write("ログ件数:", len(df))
    st.write("イベントID一覧:")
    st.write(df["イベント ID"].value_counts())

    # 1時間ごとの件数
    hourly = df.resample("h", on="日付と時刻").size()

    st.subheader("⏰ 時間ごとのイベント件数")

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(hourly.index, hourly.values, marker="o")
    ax.set_title("Events per Hour")
    ax.set_xlabel("Time")
    ax.set_ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig)

    # ログオンタイプ抽出
    def extract_logon_type(text):
        match = re.search(r"ログオン タイプ:\s*(\d+)", str(text))
        if match:
            return int(match.group(1))
        return None

    df["ログオンタイプ"] = df["詳細"].apply(extract_logon_type)

    logon_counts = df["ログオンタイプ"].value_counts().sort_index()

    if len(logon_counts) > 0:
        st.subheader("🔎 ログオンタイプ分布")

        fig2, ax2 = plt.subplots(figsize=(8, 5))
        logon_counts.plot(kind="bar", ax=ax2)
        ax2.set_title("Logon Type Distribution")
        ax2.set_xlabel("Logon Type")
        ax2.set_ylabel("Count")
        plt.tight_layout()

        st.pyplot(fig2)

        st.write("ログオンタイプ件数:")
        st.write(logon_counts)

    # 4625ログオン失敗検知
    failed = df[df["イベント ID"].astype(str) == "4625"]

    st.subheader("🚨 ログオン失敗検知")

    if len(failed) > 0:
        st.error(f"ログオン失敗イベントを {len(failed)} 件検知しました。")
        st.dataframe(failed[["日付と時刻", "イベント ID", "詳細"]])
    else:
        st.success("ログオン失敗イベントは検知されませんでした。")