import streamlit as st

# Dummy credentials
USER_CREDENTIALS = {
    "admin": "admin123",
    "user": "password123"
}

def login():
    st.title("🔐 Login - Solar Energy Tracker")
    st.write("Please login to access the dashboard and ROI calculator.")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.success("✅ Login successful!")
            st.session_state.logged_in = True
            st.rerun()  # ✅ Use st.rerun() (for Streamlit ≥1.25)
        else:
            st.error("❌ Invalid username or password.")



