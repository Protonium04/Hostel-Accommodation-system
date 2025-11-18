# pages/complaints.py
import streamlit as st
import pandas as pd
from utils.db import fetchall, fetchone, execute
from utils.search import searchable_table

st.title("🛠 Complaints")

complaints = pd.DataFrame(fetchall("SELECT * FROM Complaint ORDER BY Complaint_ID"))
searchable_table(complaints, key_prefix="complaints")

st.write("---")
st.subheader("➕ File Complaint")

students = fetchall("SELECT Student_ID, Student_Name, Room_ID FROM Student ORDER BY Student_ID")
if not students:
    st.info("Add students first.")
else:
    with st.form("add_complaint_form"):
        label = st.selectbox(
            "Student",
            [f"{s['Student_ID']} - {s['Student_Name']}" for s in students]
        )
        sid = int(label.split(" - ")[0])
        desc = st.text_area("Complaint Description")

        submit = st.form_submit_button("Submit Complaint")
        if submit:
            room_row = fetchone("SELECT Room_ID FROM Student WHERE Student_ID=%s", (sid,))
            room_id = room_row["Room_ID"] if room_row else None
            try:
                execute(
                    "INSERT INTO Complaint (Student_ID, Room_ID, Description, Status) VALUES (%s,%s,%s,'Pending')",
                    (sid, room_id, desc),
                )
                st.success("Complaint submitted.")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")

st.write("---")
st.subheader("✏️ Update / ❌ Delete Complaint")

clist = fetchall("SELECT Complaint_ID, Status FROM Complaint ORDER BY Complaint_ID")
if not clist:
    st.info("No complaints yet.")
else:
    opt = st.selectbox(
        "Select Complaint",
        [f"{c['Complaint_ID']} - {c['Status']}" for c in clist]
    )
    cid = int(opt.split(" - ")[0])
    action = st.radio("Action", ["Mark Resolved", "Delete"], horizontal=True)

    if action == "Mark Resolved":
        if st.button("Set Resolved"):
            try:
                execute("UPDATE Complaint SET Status='Resolved' WHERE Complaint_ID=%s", (cid,))
                st.success("Complaint resolved.")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        if st.button("Delete Complaint", type="primary"):
            try:
                execute("DELETE FROM Complaint WHERE Complaint_ID=%s", (cid,))
                st.success("Complaint deleted.")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")
