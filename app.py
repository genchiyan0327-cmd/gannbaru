import streamlit as st
import pandas as pd

url = "https://raw.githubusercontent.com/genchiyan0327-cmd/gannbaru/main/3%E8%A8%80%E8%AA%9E.csv"
df = pd.read_csv(url)

df["No"] = range(1, len(df) + 1)

st.title("語彙アプリ")

page_size = 50

if "page" not in st.session_state:
    st.session_state.page = 0

start = st.session_state.page * page_size
end = start + page_size

st.subheader("ロシア語一覧")

for _, row in df.iloc[start:end].iterrows():
    st.markdown(f"### {row['No']}. {row['Русский']}")
    st.write("🇩🇪", row["Deutsch"])
    st.write("🇺🇸", row["English"])
    st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    if st.button("◀ 前へ"):
        if st.session_state.page > 0:
            st.session_state.page -= 1

with col2:
    if st.button("次へ ▶"):
        if (st.session_state.page + 1) * page_size < len(df):
            st.session_state.page += 1
