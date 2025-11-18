# pages/payments.py
import streamlit as st
import pandas as pd
from datetime import date
from utils.db import fetchall, execute
from utils.search import searchable_table

st.title("💳 Payments")

payments = pd.DataFrame(fetchall(
    """
    SELECT 
        P.Payment_ID,
        P.Booking_ID,
        S.Student_Name,
        P.Amount,
        P.Payment_Date,
        P.Mode
    FROM Payment P
    JOIN Booking B ON P.Booking_ID = B.Booking_ID
    JOIN Student S ON B.Student_ID = S.Student_ID
    ORDER BY P.Payment_ID
    """
))
searchable_table(payments, key_prefix="payments")

st.write("---")
st.subheader("➕ Add Payment")

active_bookings = fetchall(
    """
    SELECT B.Booking_ID, S.Student_Name
    FROM Booking B
    JOIN Student S ON B.Student_ID = S.Student_ID
    WHERE B.Status='Active'
    ORDER BY B.Booking_ID
    """
)

if not active_bookings:
    st.info("No active bookings.")
else:
    with st.form("add_payment_form"):
        label = st.selectbox(
            "Booking",
            [f"{b['Booking_ID']} - {b['Student_Name']}" for b in active_bookings]
        )
        booking_id = int(label.split(" - ")[0])

        amount = st.number_input("Amount (₹)", min_value=0.0, step=500.0, value=15000.0)
        pay_date = st.date_input("Payment Date", value=date.today())
        mode = st.selectbox("Mode", ["Online", "UPI", "Cash"])

        ok = st.form_submit_button("Record Payment")
        if ok:
            try:
                execute(
                    "INSERT INTO Payment (Booking_ID, Amount, Payment_Date, Mode) VALUES (%s,%s,%s,%s)",
                    (booking_id, amount, pay_date, mode),
                )
                st.success("Payment recorded.")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")

st.write("---")
st.subheader("✏️ Update / ❌ Delete Payment")

plist = fetchall("SELECT Payment_ID, Amount FROM Payment ORDER BY Payment_ID")
if not plist:
    st.info("No payments yet.")
else:
    opt = st.selectbox(
        "Select Payment",
        [f"{p['Payment_ID']} - ₹{p['Amount']}" for p in plist]
    )
    pid = int(opt.split(" - ")[0])
    action = st.radio("Action", ["Update Amount", "Delete"], horizontal=True)

    if action == "Update Amount":
        new_amount = st.number_input("New Amount (₹)", min_value=0.0, step=500.0)
        if st.button("Update Payment"):
            try:
                execute("UPDATE Payment SET Amount=%s WHERE Payment_ID=%s", (new_amount, pid))
                st.success("Payment updated.")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        if st.button("Delete Payment", type="primary"):
            try:
                execute("DELETE FROM Payment WHERE Payment_ID=%s", (pid,))
                st.success("Payment deleted.")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")
