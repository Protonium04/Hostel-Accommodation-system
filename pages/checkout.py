# pages/checkout.py
import streamlit as st
from utils.db import fetchall, fetchone, execute

st.title("🚪 Checkout (End Booking)")

active = fetchall(
    """
    SELECT B.Booking_ID, S.Student_Name, B.Room_ID
    FROM Booking B
    JOIN Student S ON B.Student_ID = S.Student_ID
    WHERE B.Status='Active'
    ORDER BY B.Booking_ID
    """
)

if not active:
    st.info("No active bookings.")
else:
    label = st.selectbox(
        "Select Booking to Checkout",
        [f"{b['Booking_ID']} - {b['Student_Name']} (Room {b['Room_ID']})" for b in active]
    )
    bid = int(label.split(" - ")[0])

    if st.button("Checkout"):
        try:
            row = fetchone("SELECT Room_ID FROM Booking WHERE Booking_ID=%s", (bid,))
            room_id = row["Room_ID"] if row else None
            execute("UPDATE Booking SET Status='Completed' WHERE Booking_ID=%s", (bid,))
            if room_id:
                execute("UPDATE Room SET Availability_Status='Available' WHERE Room_ID=%s", (room_id,))
            st.success("Checkout completed and room freed.")
            st.rerun()
        except Exception as e:
            st.error(f"Error: {e}")
