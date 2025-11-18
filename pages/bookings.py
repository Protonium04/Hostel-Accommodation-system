# pages/bookings.py
import streamlit as st
import pandas as pd
from datetime import date
from utils.db import fetchall, fetchone, execute
from utils.search import searchable_table

st.title("📘 Bookings")

# -------- Show Bookings --------
bookings = pd.DataFrame(fetchall("""
SELECT Booking_ID, Student_ID, Room_ID, CheckIn_Date, CheckOut_Date, Status
FROM Booking ORDER BY Booking_ID
"""))
searchable_table(bookings, key_prefix="bookings")

st.write("---")
st.subheader("➕ Create Booking (Assign Room)")

students = fetchall("SELECT Student_ID, Student_Name, Hostel_ID FROM Student ORDER BY Student_ID")

if not students:
    st.info("No students available.")
else:
    student_select = st.selectbox(
        "Select Student",
        [f"{s['Student_ID']} - {s['Student_Name']}" for s in students]
    )
    student_id = int(student_select.split(" - ")[0])

    # Get hostel for selected student
    hostel_id = fetchone("SELECT Hostel_ID FROM Student WHERE Student_ID=%s", (student_id,))["Hostel_ID"]

    # Filter vacant rooms from same hostel
    rooms = fetchall("""
        SELECT Room_ID, Room_No FROM Room
        WHERE Hostel_ID=%s AND Availability_Status='Available'
    """, (hostel_id,))

    if not rooms:
        st.warning("No available rooms in student's hostel.")
    else:
        room_select = st.selectbox("Select Room",
                                   [f"{r['Room_ID']} - {r['Room_No']}" for r in rooms])
        room_id = int(room_select.split(" - ")[0])

        checkin = st.date_input("Check-in", value=date.today())
        checkout = st.date_input("Check-out", value=date.today())

        if st.button("Create Booking"):
            existing = fetchone("""
                SELECT Booking_ID FROM Booking
                WHERE Student_ID=%s AND Status='Active'
            """, (student_id,))

            if existing:
                st.error("This student already has an active booking.")
            else:
                execute("""
                    INSERT INTO Booking (Student_ID, Room_ID, CheckIn_Date, CheckOut_Date, Status)
                    VALUES (%s,%s,%s,%s,'Active')
                """, (student_id, room_id, checkin, checkout))

                execute("UPDATE Room SET Availability_Status='Occupied' WHERE Room_ID=%s", (room_id,))
                execute("UPDATE Student SET Room_ID=%s WHERE Student_ID=%s", (room_id, student_id))

                st.success("Booking created! Room assigned.")
                st.rerun()

st.write("---")
st.subheader("✏️ Update / ❌ Delete Booking")

booking_list = fetchall("SELECT Booking_ID, Student_ID FROM Booking ORDER BY Booking_ID")
if not booking_list:
    st.info("No bookings exist.")
else:
    selection = st.selectbox("Select Booking",
                             [f"{b['Booking_ID']} - Student {b['Student_ID']}" for b in booking_list])
    bid = int(selection.split(" - ")[0])
    action = st.radio("Choose Action:", ["Update Status", "Delete"], horizontal=True)

    if action == "Update Status":
        new_status = st.selectbox("New Status", ["Active", "Cancelled", "Completed"])
        if st.button("Update"):
            execute("UPDATE Booking SET Status=%s WHERE Booking_ID=%s", (new_status, bid))
            st.success("Booking updated.")
            st.rerun()

    else:  # Delete
        if st.button("Delete Booking", type="primary"):
            row = fetchone("SELECT Room_ID FROM Booking WHERE Booking_ID=%s", (bid,))
            room_id = row["Room_ID"]
            execute("DELETE FROM Booking WHERE Booking_ID=%s", (bid,))
            if room_id:
                execute("UPDATE Room SET Availability_Status='Available' WHERE Room_ID=%s", (room_id,))
                execute("UPDATE Student SET Room_ID=NULL WHERE Student_ID=(SELECT Student_ID FROM Booking WHERE Booking_ID=%s)", (bid,))
            st.success("Booking deleted & room freed!")
            st.rerun()
