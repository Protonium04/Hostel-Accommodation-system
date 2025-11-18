import streamlit as st
import pandas as pd
from utils.db import fetchall

st.title("🚨 Pending Payments (Amount Based)")

MONTHLY_FEE = 15000  # Change here if needed

# Fetch bookings with student names
bookings = fetchall("""
    SELECT B.Booking_ID, S.Student_ID, S.Student_Name AS Full_Name
    FROM Booking B
    JOIN Student S ON B.Student_ID = S.Student_ID
""")

# Fetch all payments
payments = fetchall("""
    SELECT Booking_ID, Amount
    FROM Payment
""")

# Convert to DataFrame
df_bookings = pd.DataFrame(bookings)
df_payments = pd.DataFrame(payments)

if df_bookings.empty:
    st.info("No active bookings found.")
else:
    # Sum all payments per booking
    if not df_payments.empty:
        df_payment_summary = df_payments.groupby("Booking_ID")["Amount"].sum().reset_index()
    else:
        df_payment_summary = pd.DataFrame(columns=["Booking_ID", "Amount"])

    # Merge to calculate dues
    df = df_bookings.merge(df_payment_summary, on="Booking_ID", how="left")
    df["Amount"] = df["Amount"].fillna(0)
    df["Due"] = MONTHLY_FEE - df["Amount"]

    # Filter students who still owe money
    df_due = df[df["Due"] > 0]

    if df_due.empty:
        st.success("🎉 Everyone has cleared their full fee!")
    else:
        st.warning("🚨 Students with Pending Payments")
        df_due_display = df_due[["Student_ID", "Full_Name", "Amount", "Due"]]
        df_due_display.columns = ["Student ID", "Student Name", "Paid (₹)", "Pending (₹)"]
        st.table(df_due_display)
