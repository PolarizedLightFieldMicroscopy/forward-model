'''User interface using the Streamlit package'''
# Enter the following into the command line the refresh browser to see updates:
# pip install streamlit
# streamlit run User_Interface.py


######################################################################
import streamlit as st
# from VolumeRaytraceLFM.abstract_classes import *
# from plotting_tools import *
import plotting_tools

st.set_page_config(
    page_title="Hello Rudolf",
    page_icon="👋",
    layout="wide", # centered
)

st.title("Polarization Simulations")

st.markdown("*Click around to explore*")

