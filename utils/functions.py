import streamlit as st

def navigate_to(page_name):
    st.session_state['current_page'] = page_name