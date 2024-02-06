import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(page_title="Chess Openings Dashboard", layout="wide", page_icon=":chess_pawn:")
st.title("Chess Opening Dashboard")