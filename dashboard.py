import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
import data_req
warnings.filterwarnings("ignore")

st.set_page_config(page_title="Chess Openings Dashboard", layout="wide", page_icon=":chess_pawn:")
st.markdown("<style>div.block-container {padding-top: 2rem;}</style>", unsafe_allow_html=True)
st.title("Chess Opening Dashboard")

chess_website = st.selectbox(label="Select chess website", options=["chess.com", "lichess"])

username = st.text_input(label="Enter your username")

time_control = st.selectbox(label="Select time control", options=["Blitz", "Bullet", "Rapid", "All"])
st.text("OR")

input_pgn_file = st.file_uploader(label="Upload PGN", type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")


#button = mr.Button(label="Submit", style="primary"

if st.button("Submit"):
    data_req.data_request(username, chess_website)
    print("Button clicked!")

