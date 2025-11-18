# pages/students.py
import streamlit as st
import pandas as pd
from utils.db import fetchall, fetchone, execute
from utils.search import searchable_table

st.title("🧑‍🎓 Student Management")

# ------------------------ SHOW STUDENTS TABLE ------------------------
students_data = fetchall("""
SELECT Student_ID, Student_Name, Gender, Contact_No, Email, Hostel_ID, Room_ID
FROM Student ORDER BY Student_ID
""")
students_df = pd.DataFrame(students_data)
searchable_table(students_df, key_prefix="student_table")

st.write("---")
st.subheader("➕ Add Student")

with st.form("add_student_form"):

    name = st.text_input("Full Name")
    gender = st.selectbox("Gender", ["Male", "Female"])
    contact = st.text_input("Contact No")
    email = st.text_input("Email")

    # -------------------- HOSTEL DROPDOWN (SHOW ALL) --------------------
    hostels = fetchall("SELECT Hostel_ID, Hostel_Name FROM Hostel")

    if not hostels:
        st.error("❌ No hostels available. Please add hostels first.")
        hostel_id = None
    else:
        hostel_map = {h["Hostel_Name"]: h["Hostel_ID"] for h in hostels}
        hostel_name_selected = st.selectbox("Select Hostel", list(hostel_map.keys()))
        hostel_id = hostel_map.get(hostel_name_selected)

    submit_student = st.form_submit_button("Save")

    if submit_student:
        if not name or not hostel_id:
            st.error("⚠️ Please enter full details.")
        else:
            execute("""
                INSERT INTO Student (Student_Name, Gender, Contact_No, Email, Hostel_ID, Room_ID)
                VALUES (%s, %s, %s, %s, %s, NULL)
            """, (name, gender, contact, email, hostel_id))

            st.success("🎉 Student added successfully! Assign room in Booking page.")
            st.rerun()

# ----------------------------------------------------------------------
st.write("---")
st.subheader("✏️ Update / ❌ Delete Student")

student_list = fetchall("SELECT Student_ID, Student_Name FROM Student ORDER BY Student_ID")

if not student_list:
    st.info("No students added yet.")
else:
    selected_student = st.selectbox(
        "Select Student",
        [f"{s['Student_ID']} - {s['Student_Name']}" for s in student_list],
        key="modify_student_dropdown"
    )

    student_id = int(selected_student.split(" - ")[0])
    action = st.radio("Action", ["Update", "Delete"], horizontal=True)

    # ---------------------- UPDATE STUDENT ----------------------
    if action == "Update":
        student_data = fetchone("SELECT * FROM Student WHERE Student_ID=%s", (student_id,))
        with st.form("update_student_form"):
            new_name = st.text_input("Full Name", value=student_data["Student_Name"])
            new_contact = st.text_input("Contact No", value=student_data["Contact_No"] or "")
            new_email = st.text_input("Email", value=student_data["Email"] or "")
            update_btn = st.form_submit_button("Save Changes")

            if update_btn:
                execute("""
                    UPDATE Student SET Student_Name=%s, Contact_No=%s, Email=%s
                    WHERE Student_ID=%s
                """, (new_name, new_contact, new_email, student_id))

                st.success("✔ Student details updated!")
                st.rerun()

    # ---------------------- DELETE STUDENT ----------------------
    if action == "Delete":
        if st.button("Delete Student", type="primary"):
            # Free room if assigned
            room_info = fetchone("SELECT Room_ID FROM Student WHERE Student_ID=%s", (student_id,))
            room_id = room_info["Room_ID"]

            # Delete student record
            execute("DELETE FROM Student WHERE Student_ID=%s", (student_id,))

            if room_id:
                execute("UPDATE Room SET Availability_Status='Available' WHERE Room_ID=%s", (room_id,))

            st.success("🗑 Student deleted successfully!")
            st.rerun()
