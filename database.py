import sqlite3
from datetime import datetime

DB_NAME = "reviews.db"


# Creates the database file and the reviews table if they don't already exist
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL,
            language TEXT NOT NULL,
            review TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


# Saves a single review to the database
def save_review(code, language, review):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reviews (code, language, review, created_at)
        VALUES (?, ?, ?, ?)
    """, (code, language, review, datetime.now().isoformat()))
    conn.commit()
    conn.close()
