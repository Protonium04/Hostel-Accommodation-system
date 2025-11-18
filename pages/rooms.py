# pages/rooms.py
import streamlit as st
import pandas as pd
from utils.db import fetchall, execute
from utils.search import searchable_table

st.title("🏠 Rooms (Boys / Girls)")

boys = pd.DataFrame(fetchall(
    """
    SELECT Room_ID, Hostel_ID, Room_No, Room_Type, Availability_Status
    FROM Room WHERE Hostel_ID = 1 ORDER BY Room_ID
    """
))
girls = pd.DataFrame(fetchall(
    """
    SELECT Room_ID, Hostel_ID, Room_No, Room_Type, Availability_Status
    FROM Room WHERE Hostel_ID = 2 ORDER BY Room_ID
    """
))

tab1, tab2 = st.tabs(["👦 Boys Hostel", "👧 Girls Hostel"])

with tab1:
    st.subheader("Boys Hostel Rooms")
    searchable_table(boys, key_prefix="boys_rooms")

with tab2:
    st.subheader("Girls Hostel Rooms")
    searchable_table(girls, key_prefix="girls_rooms")

st.write("---")
st.subheader("Manual Room Status Update")

rid = st.number_input("Room ID", min_value=0, step=1)
new_status = st.selectbox("Set status", ["Available", "Occupied"])

if st.button("Update Room Status"):
    if rid:
        try:
            execute("UPDATE Room SET Availability_Status=%s WHERE Room_ID=%s", (new_status, rid))
            st.success("Room status updated.")
            st.rerun()
        except Exception as e:
            st.error(str(e))
