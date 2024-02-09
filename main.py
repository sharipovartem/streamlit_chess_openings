import streamlit as st
import plotly.express as px
import pandas as pd
import os
import time
import warnings
import data_req
import dashboards
warnings.filterwarnings("ignore")

st.set_page_config(page_title="Chess Openings Dashboard", layout="wide", page_icon=":chess_pawn:")
st.markdown("<style>div.block-container {padding-top: 2rem;}</style>", unsafe_allow_html=True)
st.title("Chess Opening Dashboard")

chess_website = st.selectbox(label="Select chess website", options=["chess.com", "lichess"])

username = st.text_input(label="Enter your username")

time_control = st.selectbox(label="Select time control", options=["Blitz", "Bullet", "Rapid", "All"])

if st.button("Submit"):
    with st.spinner("Loading your profile..."):
        time.sleep(5)
    data_req.data_request(username, chess_website)
    data_req.wait_for_file(username)
    data_req.convert_to_csv(username)
    st.success("Done!")
    print("Button clicked!")

