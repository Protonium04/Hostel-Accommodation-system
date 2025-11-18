# utils/db.py
import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",          # change if needed
    "password": "Pratham@oct1",          # put your MySQL password
    "database": "Hostelacc", # make sure DB name matches
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def fetchall(query, params=None):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute(query, params or ())
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def fetchone(query, params=None):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute(query, params or ())
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def execute(query, params=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, params or ())
    conn.commit()
    cur.close()
    conn.close()
