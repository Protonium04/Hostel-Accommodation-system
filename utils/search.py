# utils/search.py
import streamlit as st
import pandas as pd

def searchable_table(df: pd.DataFrame, key_prefix: str):
    if df is None or df.empty:
        st.info("No data available.")
        return

    search_key = f"search_{key_prefix}"
    search = st.text_input("🔍 Search", key=search_key)

    if search:
        search = search.strip()
        df = df[df.apply(
            lambda row: row.astype(str).str.contains(search, case=False, na=False).any(),
            axis=1
        )]

    st.dataframe(df, use_container_width=True)
