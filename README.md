# 🏨 Hostel Accommodation & Management System

This project is a database-driven hostel management application that automates student management, room allocation, fee tracking, booking, complaint handling and pending dues monitoring. The application uses Python with Streamlit for the user interface and MySQL as the backend database, along with automated triggers, functions, views and stored procedures.

---

## 📌 Project Overview

The system is designed to replace manual hostel record maintenance with a digital management platform. It supports boys and girls hostels separately, maintains dynamic room status, automates payment tracking and allows the admin to manage complaints and student data effectively.

---

## 🎯 Objectives

• Implement a centralized digital hostel administration system  
• Automate booking, room occupancy, and checkout processes  
• Maintain secure and structured storage of student data  
• Track hostel payments and generate pending dues  
• Provide an interface for complaint registering and processing  
• Include dashboard analytics for decision making  

---

## 🚀 Features

• Admin-controlled student management  
• Boys and girls hostel room segregation  
• Real-time room availability display  
• Hostel booking and automatic room assignment  
• Auto-release room on checkout  
• Payment history and due calculation  
• Complaint logging and status updating  
• Reset module for admin testing  
• Search and filter for all database tables  

---

## 🛠️ Technology Used

Frontend: Streamlit  
Backend: Python  
Database: MySQL  
Design Tools: Draw.io / MySQL Workbench  
IDE: VS Code / PyCharm  
Supported OS: Windows / Linux  

---

## 📂 Project Folder Structure

.
├── app.py  
├── HostelAccommodation.sql  
├── pages  
│   ├── dashboard.py  
│   ├── students.py  
│   ├── rooms.py  
│   ├── bookings.py  
│   ├── payments.py  
│   ├── complaints.py  
│   ├── pending_dues.py  
│   └── admin_reset.py  
│  
├── utils  
│   ├── db.py  
│   ├── theme.py  
│   ├── auth.py  
│   ├── __init__.py  
│   └── search.py  
│  
├── requirements.txt  
└── README.md  

---

## 🧩 Relational Schema (Text Description)

Hostel  
• Hostel_ID (Primary Key)  
• Hostel_Name  
• Location  
• Gender  
• Total_Rooms  
• Rent  

Room  
• Room_ID (Primary Key)  
• Hostel_ID (Foreign Key to Hostel)  
• Room_No  
• Room_Type  
• Availability_Status  

Student  
• Student_ID (Primary Key)  
• Full_Name  
• Gender  
• Contact_No  
• Email  
• Hostel_ID (Foreign Key to Hostel)  
• Room_ID (Foreign Key to Room)  

Booking  
• Booking_ID (Primary Key)  
• Student_ID (Foreign Key to Student)  
• Room_ID (Foreign Key to Room)  
• Checkin_Date  
• Checkout_Date  
• Status  

Payment  
• Payment_ID (Primary Key)  
• Booking_ID (Foreign Key to Booking)  
• Amount  
• Payment_Date  
• Mode  

Complaint  
• Complaint_ID (Primary Key)  
• Student_ID (Foreign Key to Student)  
• Issue  
• Status  

---

## ▶️ How to Run This Project

1. Install Python and MySQL on your system.  
2. Import the SQL database file provided with the project.  
3. Install the required Python packages using the included requirements file.  
4. Configure database connection by entering your own MySQL username and password inside the project configuration files.  
5. Launch the application and open it in the browser to access all modules.  

---

## ⚠️ Important Configuration Note

During setup, the user must enter their own MySQL database username and password, as the project does not include default credentials. Using incorrect credentials will prevent successful database connection. Ensure your MySQL server is running before launching the app.

---

## 🔗 GitHub Repository Link

https://github.com/Protonium04/Hostel-Accommodation-system  

---

## 👥 Credits

Developers:  
• Prathama  
• Preksha  
