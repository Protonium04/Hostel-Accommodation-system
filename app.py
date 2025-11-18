# app.py
import streamlit as st
from utils.db import fetchone

st.set_page_config(page_title="Hostel Management", layout="wide")
st.title("📊 Hostel Dashboard")

# Basic stats
total_students = fetchone("SELECT COUNT(*) AS c FROM Student")["c"]
active_bookings = fetchone("SELECT COUNT(*) AS c FROM Booking WHERE Status='Active'")["c"]
total_rooms = fetchone("SELECT COUNT(*) AS c FROM Room")["c"]
available_rooms = fetchone("SELECT COUNT(*) AS c FROM Room WHERE Availability_Status='Available'")["c"]
total_revenue_row = fetchone("SELECT SUM(Amount) AS s FROM Payment")
total_revenue = float(total_revenue_row["s"] or 0)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Students", total_students)
c2.metric("Active Bookings", active_bookings)
c3.metric("Available Rooms", f"{available_rooms}/{total_rooms}")
c4.metric("Total Revenue (₹)", total_revenue)

st.write("---")
st.write("Use the sidebar to navigate: Students, Rooms, Bookings, Payments, Complaints, Checkout, Pending Dues.")
