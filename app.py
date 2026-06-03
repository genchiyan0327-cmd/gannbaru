import streamlit as st
import pandas as pd
import urllib.parse

url = "https://raw.githubusercontent.com/genchiyan0327-cmd/gannbaru/main/3%E8%A8%80%E8%AA%9E.csv"
df = pd.read_csv(url)

st.title("語彙アプリ")

def make_tts(text, lang):
    return "https://translate.google.com/translate_tts?ie=UTF-8&tl=" + lang + "&client=tw-ob&q=" + urllib.parse.quote(text)

page_size = 50

if "page" not in st.session_state:
    st.session_state.page = 0

start = st.session_state.page * page_size
end = start + page_size

st.subheader("ロシア語一覧")

for idx, row in df.iloc[start:end].iterrows():

    st.write(f"{idx+1}. {row['Русский']}")

    col1, col2 = st.columns(2)

    with col1:
        st.audio(make_tts(row["Русский"], "ru"))

    if st.button("開く", key=str(idx)):

        st.markdown("---")
        st.write("🇩🇪", row["Deutsch"])
        st.audio(make_tts(row["Deutsch"], "de"))

        st.write("🇺🇸", row["English"])
        st.audio(make_tts(row["English"], "en"))

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
