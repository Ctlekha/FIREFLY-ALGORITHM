import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
st.set_page_config(page_title="Firefly Quest 2.0",page_icon="✨",layout="wide",initial_sidebar_state="collapsed")
st.markdown("""<style>header[data-testid="stHeader"]{display:none}.block-container{padding:0!important;max-width:none!important}iframe{height:100dvh!important;display:block} [data-testid="stAppViewContainer"]{overflow:hidden}</style>""",unsafe_allow_html=True)
components.html(Path(__file__).with_name("game.html").read_text(encoding="utf-8"),height=800,scrolling=False)
