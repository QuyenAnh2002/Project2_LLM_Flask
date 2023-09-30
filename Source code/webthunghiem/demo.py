import sqlite3

conn = sqlite3.connect('user_data.db')

cursor = conn.cursor()

sql_create_table ="""
    CREATE TABLE IF NOT EXISTS img_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL UNIQUE,
        path VARCHAR(255) NOT NULL
    )
"""


try:
    cursor.execute(sql_create_table)
    conn.commit()
except:
    print("lỗi")
conn.close()

