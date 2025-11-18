# pages/admin_reset.py
import streamlit as st
from utils.db import execute

st.title("⚠️ Admin Reset Panel")
st.warning("This will delete all user-generated records. Proceed only if you are admin.")

if st.button("Reset Database", type="primary"):
    try:
        # Disable FK temporarily
        execute("SET FOREIGN_KEY_CHECKS = 0")

        # Delete in correct dependency order
        execute("DELETE FROM Payment")
        execute("DELETE FROM Complaint")
        execute("DELETE FROM Booking")
        execute("DELETE FROM Student")

        # Reset room status
        execute("UPDATE Room SET Availability_Status='Available'")

        # Re-enable FK
        execute("SET FOREIGN_KEY_CHECKS = 1")

        st.success("Database reset successful! Everything is clean now 🙌")
        st.balloons()

    except Exception as e:
        st.error(f"Error: {e}")
