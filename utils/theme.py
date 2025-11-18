import streamlit as st

def load_neon_theme():
    st.markdown("""
    <style>
        body { background-color: #0f0f0f !important; }
        .stApp { background: #0f0f0f; color: #e6e6e6; }

        /* neon heading */
        h1, h2, h3, h4 {
            color: #00ffff !important;
            text-shadow: 0px 0px 10px #00ffff;
        }

        /* buttons */
        .stButton button {
            background: linear-gradient(90deg,#00c6ff,#0072ff);
            color: white !important;
            border-radius: 8px;
        }

        /* input fields */
        .stTextInput>div>div>input,
        .stNumberInput>div>input,
        textarea, select {
            background-color: #1a1a1a !important;
            color: #fff !important;
        }

        table, th, td {
            color: #e6e6e6 !important;
        }
    </style>
    """, unsafe_allow_html=True)
