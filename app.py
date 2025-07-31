import streamlit as st
from login import login
from dashboard.main import run_dashboard  # This import works only if folder structure is correct

st.set_page_config(page_title="Solar Energy Tracker", layout="centered")

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Show login or dashboard based on session state
if not st.session_state.logged_in:
    login()
else:
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["📊 Dashboard"])

    if page == "📊 Dashboard":
        run_dashboard()

