import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO

# CSV読み込み
url = "https://raw.githubusercontent.com/genchiyan0327-cmd/gannbaru/main/3%E8%A8%80%E8%AA%9E.csv"
df = pd.read_csv(url)

# 音声生成（安定版）
def make_audio(text, lang):
    tts = gTTS(text=str(text), lang=lang)
    fp = BytesIO()
    tts.write_to_fp(fp)
    return fp.getvalue()

st.title("語彙アプリ（ロシア語・ドイツ語・英語）")

page_size = 50

if "page" not in st.session_state:
    st.session_state.page = 0

start = st.session_state.page * page_size
end = start + page_size

# 単語表示
for idx, row in df.iloc[start:end].iterrows():

    with st.expander(f"{idx + 1}. {row.iloc[0]}"):

        # ロシア語
        st.write("🇷🇺", row.iloc[0])
        if st.button(f"🔊 再生（RU {idx}）"):
            st.audio(make_audio(row.iloc[0], "ru"), format="audio/mp3")

        # ドイツ語
        st.write("🇩🇪", row.iloc[1])
        if st.button(f"🔊 再生（DE {idx}）"):
            st.audio(make_audio(row.iloc[1], "de"), format="audio/mp3")

        # 英語
        st.write("🇺🇸", row.iloc[2])
        if st.button(f"🔊 再生（EN {idx}）"):
            st.audio(make_audio(row.iloc[2], "en"), format="audio/mp3")

# ページ送り
col1, col2 = st.columns(2)

with col1:
    if st.button("◀ 前へ"):
        if st.session_state.page > 0:
            st.session_state.page -= 1
            st.rerun()

with col2:
    if st.button("次へ ▶"):
        if (st.session_state.page + 1) * page_size < len(df):
            st.session_state.page += 1
            st.rerun()
