import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(page_title="Chess Openings Dashboard", layout="wide", page_icon=":chess_pawn:")
st.markdown("<style>div.block-container {padding-top: 2rem;}</style>", unsafe_allow_html=True)
st.title("Chess Opening Dashboard")
st.selectbox(label="Select time column", options=["Blitz", "Bullet", "Rapid", "All"])
st.selectbox(label="Select chess website", options=["chess.com", "lichess.org"])

st.text_input(label="Enter your username")
st.text("OR")
st.file_uploader(label="Upload PGN", type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")