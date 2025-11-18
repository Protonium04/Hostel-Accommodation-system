import streamlit as st

USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "warden": {"password": "warden123", "role": "warden"}
}

def login():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    st.title("🔐 HostelAcc Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USERS and USERS[username]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.role = USERS[username]["role"]
            st.success("Login successful!")
            st.experimental_rerun()
        else:
            st.error("Invalid credentials")

    st.stop()

def secure_page(allowed_roles=["admin", "warden"]):
    if not st.session_state.get("logged_in"):
        login()
    if st.session_state.get("role") not in allowed_roles:
        st.error("🚫 Access Denied")
        st.stop()
