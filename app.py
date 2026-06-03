import streamlit as st
import pandas as pd
import urllib.parse

url = "https://raw.githubusercontent.com/genchiyan0327-cmd/gannbaru/main/3%E8%A8%80%E8%AA%9E.csv"
df = pd.read_csv(url)

df["No"] = range(1, len(df) + 1)

st.title("語彙アプリ")

page_size = 50

if "page" not in st.session_state:
    st.session_state.page = 0

def make_tts_url(text, lang):
    base = "https://translate.google.com/translate_tts"
    params = f"?ie=UTF-8&tl={lang}&client=tw-ob&q={urllib.parse.quote(text)}"
    return base + params

start = st.session_state.page * page_size
end = start + page_size

for _, row in df.iloc[start:end].iterrows():

    st.markdown(f"### {row['No']}. {row['Русский']}")
    st.write("🇩🇪", row["Deutsch"])
    st.write("🇺🇸", row["English"])

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button(f"🔊 RU {row['No']}", key=f"ru{row['No']}"):
            st.audio(make_tts_url(row["Русский"], "ru"))

    with col2:
        if st.button(f"🔊 EN {row['No']}", key=f"en{row['No']}"):
            st.audio(make_tts_url(row["English"], "en"))

    with col3:
        if st.button(f"🔊 DE {row['No']}", key=f"de{row['No']}"):
            st.audio(make_tts_url(row["Deutsch"], "de"))

col1, col2 = st.columns(2)

with col1:
    if st.button("◀ 前へ"):
        if st.session_state.page > 0:
            st.session_state.page -= 1

with col2:
    if st.button("次へ ▶"):
        if (st.session_state.page + 1) * page_size < len(df):
            st.session_state.page += 1
